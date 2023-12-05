import os


class Logger:
    NEED_LOGGER: bool = bool(os.getenv("NEED_LOGGER"))

    def __init__(self):
        self._method: str = None
        self._url: str = None
        self._headers: str = None
        self._body: str = None
        self._status_code: int = None
        # self.log_entry = Log()


    def set_proxy_method(self, method):
        self._method = method

    def set_core_method(self, method):
        self._method = method


    def set_proxy_url(self, url):
        self._url = url

    def set_core_url(self, url):
        self._url = url

    def set_proxy_request_headers(self, headers):
        self._headers = headers

    def set_core_request_headers(self, headers):
        self._headers = headers

    def set_proxy_request_body(self, body):
        self._body = body

    def set_core_request_body(self, body):
        self._body = body

    def set_proxy_response_headers(self, headers):
        self._headers = headers

    def set_core_response_headers(self, headers):
        self._headers = headers

    def set_proxy_response_body(self, body):
        self._body = body

    def set_core_response_body(self, body):
        self._body = body

    def set_proxy_response_status_code(self, status_code):
        self._status_code = status_code

    def set_core_response_status_code(self, status_code):
        self._status_code = status_code

    def write(self):
        if self.NEED_LOGGER:
            pass