import os
from datetime import datetime
from django.conf import settings
from .models import Log

class Logger:
    NEED_LOGGER: bool = settings.NEED_LOGGER

    def __init__(self,
                 proxy_method=None,
                 core_method=None,
                 proxy_url=None,
                 core_url=None,
                 proxy_request_headers=None,
                 core_request_headers=None,
                 proxy_request_body=None,
                 core_request_body=None,
                 proxy_response_headers=None,
                 core_response_headers=None,
                 proxy_response_body=None,
                 core_response_body=None,
                 proxy_response_status_code=None,
                 core_response_status_code=None,
                 ):
        self.__log_entry = Log()
        self._set_proxy_method(method=proxy_method)
        self._set_core_method(method=core_method)
        self._set_proxy_url(url=proxy_url)
        self._set_core_url(url=core_url)
        self._set_proxy_request_headers(headers=proxy_request_headers)
        self._set_core_request_headers(headers=core_request_headers)
        self._set_proxy_request_body(body=proxy_request_body)
        self._set_core_request_body(body=core_request_body)
        self._set_proxy_response_headers(headers=proxy_response_headers)
        self._set_core_response_headers(headers=core_response_headers)
        self._set_proxy_response_body(body=proxy_response_body)
        self._set_core_response_body(body=core_response_body)
        self._set_proxy_response_status_code(status_code=proxy_response_status_code)
        self._set_core_response_status_code(status_code=core_response_status_code)


    def _set_proxy_method(self, method):
        self.__log_entry.proxy_method = method

    def _set_core_method(self, method):
        self.__log_entry.core_method = method

    def _set_proxy_url(self, url):
        self.__log_entry.proxy_url = url

    def _set_core_url(self, url):
        self.__log_entry.core_url = url

    def _set_proxy_request_headers(self, headers):
        self.__log_entry.proxy_request_headers = headers

    def _set_core_request_headers(self, headers):
        self.__log_entry.core_request_headers = headers

    def _set_proxy_request_body(self, body):
        self.__log_entry.proxy_request_body = body

    def _set_core_request_body(self, body):
        self.__log_entry.core_request_body = body

    def _set_proxy_response_headers(self, headers):
        self.__log_entry.proxy_response_headers = headers

    def _set_core_response_headers(self, headers):
        self.__log_entry.core_response_headers = headers

    def _set_proxy_response_body(self, body):
        self.__log_entry.proxy_response_body = body

    def _set_core_response_body(self, body):
        self.__log_entry.core_response_body = body

    def _set_proxy_response_status_code(self, status_code):
        self.__log_entry.proxy_response_status_code = status_code

    def _set_core_response_status_code(self, status_code):
        self.__log_entry.core_response_status_code = status_code

    def write(self):
        if self.NEED_LOGGER:
            self.__log_entry.created_at = datetime.now().isoformat()
            self.__log_entry.save()
