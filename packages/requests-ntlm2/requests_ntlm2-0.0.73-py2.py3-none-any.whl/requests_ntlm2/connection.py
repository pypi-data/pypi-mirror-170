import logging
import re
import select
import socket

from requests.packages.urllib3.connection import DummyConnection
from requests.packages.urllib3.connection import HTTPConnection as _HTTPConnection
from requests.packages.urllib3.connection import HTTPSConnection as _HTTPSConnection
from requests.packages.urllib3.connection import VerifiedHTTPSConnection as _VerifiedHTTPSConnection
from six.moves.http_client import PROXY_AUTHENTICATION_REQUIRED, LineTooLong

from .core import NtlmCompatibility, get_ntlm_credentials, noop
from .dance import HttpNtlmContext


IO_WAIT_TIMEOUT = 0.1


logger = logging.getLogger(__name__)

# maximal line length when calling readline().
_MAXLINE = 65536

_ASSUMED_HTTP09_STATUS_LINES = (
    ("HTTP/0.9", 200, ""),
    ("HTTP/0.9", 200, "OK"),
)

_TRACKED_HEADERS = (
    "proxy-authenticate",
    "proxy-support",
    "cache-control",
    "date",
    "server",
    "proxy-connection",
    "connection",
    "content-length",
    "content-type",
)

HTTP_VERSION_11 = "HTTP/1.1"
HTTP_VERSION_10 = "HTTP/1.0"
DEFAULT_HTTP_VERSION = HTTP_VERSION_10


class HTTPConnection(_HTTPConnection):
    pass


class HTTPSConnection(_HTTPSConnection):
    pass


class VerifiedHTTPSConnection(_VerifiedHTTPSConnection):
    ntlm_compatibility = NtlmCompatibility.NTLMv2_DEFAULT
    ntlm_strict_mode = False

    def __init__(self, *args, **kwargs):
        super(VerifiedHTTPSConnection, self).__init__(*args, **kwargs)
        self._continue_reading_headers = True
        if self.ntlm_compatibility is None:
            self.ntlm_compatibility = NtlmCompatibility.NTLMv2_DEFAULT

    @classmethod
    def set_ntlm_auth_credentials(cls, username, password):
        cls._ntlm_credentials = get_ntlm_credentials(username, password)

    @classmethod
    def set_http_version(cls, http_version):
        if http_version in (HTTP_VERSION_10, HTTP_VERSION_11):
            cls._http_version = http_version
        else:
            logger.info(
                "unsupported http-version %r, setting the default %r",
                http_version,
                DEFAULT_HTTP_VERSION
            )
            cls._http_version = DEFAULT_HTTP_VERSION

    @classmethod
    def clear_http_version(cls):
        cls._http_version = None
        del cls._http_version

    @classmethod
    def clear_ntlm_auth_credentials(cls):
        cls._ntlm_credentials = None
        del cls._ntlm_credentials

    @staticmethod
    def _is_line_blank(line):
        # for sites which EOF without sending a trailer
        if not line or line in (b"\r\n", b"\n", b"") or not line.strip():
            return True
        return False

    @staticmethod
    def _read_response_line_if_ready(response):
        (ready, _, _) = select.select([response.fp], (), (), IO_WAIT_TIMEOUT)
        if ready:
            return response.fp.readline()

    @staticmethod
    def _flush_response_buffer(response):
        logger.info('* flushing the response buffer')
        (ready, _, _) = select.select([response.fp], (), (), IO_WAIT_TIMEOUT)
        if ready:
            response.fp.read()
        logger.info('* successfully flushed the response buffer')

    def handle_http09_response(self, response):
        status_line_regex = re.compile(
            br"(?P<version>HTTP/\d\.\d)\s+(?P<status>\d+)\s+(?P<message>.+)",
            re.DOTALL
        )

        while True:
            line = response.fp.readline()
            if not line:
                self._continue_reading_headers = False
                break
            match = status_line_regex.search(line)
            if match:
                status_line = match.groupdict()
                logger.info("< %r", "{version} {status} {message}".format(**status_line))
                return status_line["version"], int(status_line["status"]), status_line["message"]
        return None

    def _get_response(self):
        logger.info('* getting response')
        response = self.response_class(self.sock, method=self._method)
        version, code, message = response._read_status()

        if (version, code, message) in _ASSUMED_HTTP09_STATUS_LINES:
            logger.warning("server response used outdated HTTP version: HTTP/0.9")
            status_line = self.handle_http09_response(response)
            if status_line:
                old_status_line = version, code, message
                version, code, message = status_line
                logger.info("changed status line from %s, to %s", old_status_line, status_line)
            else:
                logger.warning("could not handle HTTP/0.9 server response")
                logger.info("HTTP/0.9: version=%s", version)
                logger.info("HTTP/0.9: code=%s", code)
                logger.info("HTTP/0.9: message=%s", message)
        else:
            logger.info("< %r", "{} {} {}".format(version, code, message))
        return version, code, message, response

    def _get_http_version(self):
        if getattr(self, "_http_version", None):
            return self._http_version
        return DEFAULT_HTTP_VERSION

    def _get_header_bytes(self, proxy_auth_header=None):
        host, port = self._get_hostport(self._tunnel_host, self._tunnel_port)
        http_connect_string = "CONNECT {host}:{port} {http_version}\r\n".format(
            host=host,
            port=port,
            http_version=self._get_http_version()
        )
        logger.info("> %r", http_connect_string)
        header_bytes = http_connect_string
        if proxy_auth_header:
            self._tunnel_headers["Proxy-Authorization"] = proxy_auth_header
        self._tunnel_headers["Proxy-Connection"] = "Keep-Alive"
        self._tunnel_headers["Host"] = "{}:{}".format(host, port)

        for header in sorted(self._tunnel_headers):
            value = self._tunnel_headers[header]
            header_byte = "%s: %s\r\n" % (header, value)
            logger.info("> %r", header_byte)
            header_bytes += header_byte
        header_bytes += "\r\n"
        return header_bytes.encode("latin1")

    def _tunnel(self):
        username, password, domain = self._ntlm_credentials
        logger.info("* attempting to open tunnel using HTTP CONNECT")
        logger.info("* username=%r, domain=%r", username, domain)
        content_length = None

        try:
            workstation = socket.gethostname().upper()
        except (AttributeError, TypeError, ValueError):
            workstation = None

        logger.info("* workstation=%r", workstation)

        ntlm_context = HttpNtlmContext(
            username,
            password,
            domain=domain,
            workstation=workstation,
            auth_type="NTLM",
            ntlm_compatibility=self.ntlm_compatibility,
            ntlm_strict_mode=self.ntlm_strict_mode
        )

        negotiate_header = ntlm_context.get_negotiate_header()
        header_bytes = self._get_header_bytes(proxy_auth_header=negotiate_header)
        self.send(header_bytes)
        version, code, message, response = self._get_response()
        logger.info('* version=%r, code=%r, message=%r', version, code, message)

        if code == PROXY_AUTHENTICATION_REQUIRED:
            authenticate_hdr = None
            match_string = "Proxy-Authenticate: NTLM "
            content_length_match_string = "Content-Length:"
            previous_line = None
            content_length_header = None
            body_length = None
            while True:
                logger.info('* reading a new line')
                line = self._read_response_line_if_ready(response)

                logger.info('* successfully read a new line')
                this_line_is_blank = self._is_line_blank(line)
                logger.info('* is this line blank? %s', this_line_is_blank)

                if body_length is None and this_line_is_blank:
                    body_length = 0
                    previous_line = line
                    logger.info('* skipping back to the top because this line is blank')  # noqa
                    continue
                else:
                    if body_length is None:
                        body_length = len(line)
                    else:
                        body_length += len(line)

                    logger.info('* body length read so far: %s', body_length)
                    if content_length is not None and body_length >= content_length_header:
                        break
                    elif content_length is None:
                        # we never had content length
                        if (
                            this_line_is_blank
                            and previous_line is not None
                            and self._is_line_blank(previous_line)
                        ):
                            line = self._read_response_line_if_ready(response)
                            if self._is_line_blank(line):
                                break

                if line.decode("utf-8").startswith(match_string):
                    logger.info("< %r", line)
                    line = line.decode("utf-8")
                    previous_line = line
                    ntlm_context.set_challenge_from_header(line)
                    authenticate_hdr = ntlm_context.get_authenticate_header()
                    logger.info('* authenticate header: %r', authenticate_hdr)
                    continue
                elif line.decode("utf-8").startswith(content_length_match_string):
                    logger.info("< %r", line)
                    line = line.decode("utf-8")
                    line = line.replace(content_length_match_string, "").strip()
                    try:
                        content_length_header = int(line)
                    except (ValueError, TypeError):
                        pass

                if len(line) > _MAXLINE:
                    logger.error('* this line is too long: %r', line)
                    raise LineTooLong("header line")

                # for header in _TRACKED_HEADERS:
                #     if line.decode("utf-8").lower().startswith("{}:".format(header)):
                logger.info("< %r", line)
                previous_line = line

            header_bytes = self._get_header_bytes(proxy_auth_header=authenticate_hdr)
            logger.info('* sending authenticate header: %r', header_bytes)
            self.send(header_bytes)
            logger.info('* authenticate header sent!')
            version, code, message, response = self._get_response()
            logger.info('* version=%r, code=%r, message=%r', version, code, message)

        if code != 200:
            self.close()
            logger.error("* Tunnel connection failed: %s %s", code, message.strip())
            raise socket.error(
                "Tunnel connection failed: %d %s" % (code, message.strip())
            )
        while self._continue_reading_headers:
            line = response.fp.readline()
            logger.info('* header: %r', line)
            if len(line) > _MAXLINE:
                raise LineTooLong("header line")
            if self._is_line_blank(line):
                break
        logger.info('* last line of the _tunnel function')


try:
    noop()  # for testing purposes
    import ssl  # noqa

    # Make a copy for testing.
    UnverifiedHTTPSConnection = HTTPSConnection
    HTTPSConnection = VerifiedHTTPSConnection
except ImportError:
    HTTPSConnection = DummyConnection
