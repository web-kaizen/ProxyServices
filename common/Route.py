import requests
from django.conf import settings
from requests import Response, PreparedRequest
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
    def allowed_client_headers(self) -> tuple:
        allowed_client_headers = ('Authorization', 'Content-Type',)
        return allowed_client_headers

    @property
    def request_headers(self) -> dict:
        headers = dict(self.request.headers)
        for header in headers:
            if header not in self.allowed_client_headers:
                headers.pop(header)
        return headers

    @property
    def request_query_params(self) -> property:
        return self.request.query_params

    def __prepare_request(self, endpoint: str, **kwargs) -> PreparedRequest:
        prepared_request = requests.Request(
            method=self.request_method,
            url=f'{settings.THIRD_PARTY_APP_URL}/{self.__APP_ID}/{endpoint}/',
            data=self.request_data,
            params=self.request_query_params,
            **kwargs
        ).prepare()

        headers = dict(self.request.headers)
        for k, v in headers.items():
            if k in self.allowed_client_headers:
                prepared_request.headers[k] = v

        return prepared_request

    # ToDo: debug headers, handle errors from Yadro
    def send(self, endpoint: str, **kwargs: dict) -> Response:
        request = self.__prepare_request(endpoint=endpoint, **kwargs)
        response = requests.Session().send(request=request)
        response.headers.pop('Connection')
        response.headers.pop('Keep-Alive')
        return response
