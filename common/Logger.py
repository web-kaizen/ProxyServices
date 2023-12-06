import os
from datetime import datetime
from django.conf import settings
from .models import Log

class Logger:
    NEED_LOGGER: bool = settings.NEED_LOGGER

    def __init__(self, options: dict =None):

        self.__log_entry = Log()
        self._set_proxy_method(method=options.get("proxy_method"))
        self._set_core_method(method=options.get('core_method'))
        self._set_proxy_url(url=options.get('proxy_url'))
        self._set_core_url(url=options.get('core_url'))
        self._set_proxy_request_headers(headers=options.get('proxy_request_headers'))
        self._set_core_request_headers(headers=options.get('core_request_headers'))
        self._set_proxy_request_body(body=options.get('proxy_request_body'))
        self._set_core_request_body(body=options.get('core_request_body'))
        self._set_proxy_response_headers(headers=options.get('proxy_response_headers'))
        self._set_core_response_headers(headers=options.get('core_response_headers'))
        self._set_proxy_response_body(body=options.get('proxy_response_body'))
        self._set_core_response_body(body=options.get('core_response_body'))
        self._set_proxy_response_status_code(status_code=options.get('proxy_response_status_code'))
        self._set_core_response_status_code(status_code=options.get('core_response_status_code'))


    def _set_proxy_method(self, method: str) -> None:
        self.__log_entry.proxy_method = method

    def _set_core_method(self, method: str) -> None:
        self.__log_entry.core_method = method

    def _set_proxy_url(self, url: str) -> None:
        self.__log_entry.proxy_url = url

    def _set_core_url(self, url: str) -> None:
        self.__log_entry.core_url = url

    def _set_proxy_request_headers(self, headers: dict) -> None:
        self.__log_entry.proxy_request_headers = headers

    def _set_core_request_headers(self, headers: dict) -> None:
        self.__log_entry.core_request_headers = headers

    def _set_proxy_request_body(self, body: dict) -> None:
        self.__log_entry.proxy_request_body = body

    def _set_core_request_body(self, body: dict) -> None:
        self.__log_entry.core_request_body = body

    def _set_proxy_response_headers(self, headers: dict) -> None:
        self.__log_entry.proxy_response_headers = headers

    def _set_core_response_headers(self, headers: dict) -> None:
        self.__log_entry.core_response_headers = headers

    def _set_proxy_response_body(self, body: dict) -> None:
        self.__log_entry.proxy_response_body = body

    def _set_core_response_body(self, body: dict) -> None:
        self.__log_entry.core_response_body = body

    def _set_proxy_response_status_code(self, status_code: int) -> None:
        self.__log_entry.proxy_response_status_code = status_code

    def _set_core_response_status_code(self, status_code: int) -> None:
        self.__log_entry.core_response_status_code = status_code

    def write(self):
        if self.NEED_LOGGER:
            self.__log_entry.created_at = datetime.now().isoformat()
            self.__log_entry.save()


            self._clear_fields()

    def _clear_fields(self):
        for field in self.__log_entry._meta.fields():
            setattr(self.__log_entry, field.attname, None)