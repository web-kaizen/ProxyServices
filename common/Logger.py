import os
from datetime import datetime
from .LogModel import Log

class Logger:
    NEED_LOGGER: bool = bool(os.getenv("NEED_LOGGER"))

    def __init__(self):
        self.log_entry = Log()


    def set_proxy_method(self, method):
        self.log_entry.proxy_method = method

    def set_core_method(self, method):
        self.log_entry.core_method = method

    def set_proxy_url(self, url):
        self.log_entry.proxy_url = url

    def set_core_url(self, url):
        self.log_entry.core_url = url

    def set_proxy_request_headers(self, headers):
        self.log_entry.proxy_request_headers = headers

    def set_core_request_headers(self, headers):
        self.log_entry.core_request_headers = headers

    def set_proxy_request_body(self, body):
        self.log_entry.proxy_request_body = body

    def set_core_request_body(self, body):
        self.log_entry.core_request_body = body

    def set_proxy_response_headers(self, headers):
        self.log_entry.proxy_response_headers = headers

    def set_core_response_headers(self, headers):
        self.log_entry.core_response_headers = headers

    def set_proxy_response_body(self, body):
        self.log_entry.proxy_response_body = body

    def set_core_response_body(self, body):
        self.log_entry.core_response_body = body

    def set_proxy_response_status_code(self, status_code):
        self.log_entry.proxy_response_status_code = status_code

    def set_core_response_status_code(self, status_code):
        self.log_entry.core_response_status_code = status_code

    def write(self):
        if self.NEED_LOGGER:
            self.log_entry.created_at = datetime.now().isoformat()
            self.log_entry.save()