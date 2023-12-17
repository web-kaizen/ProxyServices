import requests
from django.conf import settings
from requests import Response
from rest_framework.request import Request


class Route:
    """Base Route for communication with third-party services"""

    def __init__(self, request: Request) -> None:
        self.request = request
        self.__APP_ID: str = settings.APP_ID
        self._allowed_client_headers = ('Authorization', 'Content-Type',)
        self._headers_for_delete = ('Connection', 'Keep-Alive',)

    def request_method(self) -> str:
        return self.request.method

    def request_data(self) -> dict | list:
        return self.request.data

    def request_query_params(self) -> dict:
        return self.request.query_params

    def send(self, endpoint: str) -> Response:
        prepared_request = requests.Request(
            method=self.request_method(),
            url=f'{settings.THIRD_PARTY_APP_URL}/{self.__APP_ID}/{endpoint}/',
            data=self.request_data(),
            params=self.request_query_params(),
        ).prepare()

        headers = dict(self.request.headers)
        prepared_request.headers = {k: v for k, v in headers.items() if k in self._allowed_client_headers}

        response = requests.Session().send(request=prepared_request)
        filtered_headers = {k: v for k, v in response.headers.items() if k not in self._headers_for_delete}
        response.headers = filtered_headers

        return response
