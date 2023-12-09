import requests
from django.conf import settings
from requests import Response

from rest_framework.request import Request


class Route:
    """Base Route for communication with third-party services"""

    def __init__(self, request: Request) -> None:
        self.request = request
        self.__APP_ID: str = settings.APP_ID

    @property
    def request_method(self) -> str:
        return self.request.method

    @property
    def request_data(self) -> property:
        return self.request.data

    @property
    def request_headers(self) -> dict:
        return self.request.headers

    @property
    def request_query_params(self) -> property:
        return self.request.query_params

    def send(self, endpoint: str, **kwargs: dict) -> Response:
        response = requests.request(
            method=self.request_method,
            url=f'{settings.THIRD_PARTY_APP_URL}/{self.__APP_ID}/{endpoint}/',
            data=self.request_data,
            # headers=self.request_headers,
            params=self.request_query_params,
            **kwargs
        )
        del response.headers['Connection']
        del response.headers['Keep-Alive']
        return response
