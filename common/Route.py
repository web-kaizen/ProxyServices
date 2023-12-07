import requests
from django.conf import settings
from requests import Response


class Route:
    """Base Route for communication with third-party services"""

    __APP_ID: str = settings.APP_ID
    _parameters: dict = {}
    _response: Response = None
    _headers: dict = {}

    def set_headers(self, headers: dict) -> None:
        self._headers = headers

    def get_headers(self) -> dict:
        return self._headers

    def set_parameters(self, params: dict) -> None:
        self._parameters = params

    def get_parameters(self) -> dict:
        return self._parameters

    def set_response(self, response: Response, status: int = None) -> None:
        if status is not None:
            if 200 <= status < 300:
                response = self.on_success(response)
            if 400 <= status <= 500:
                response = self.on_error(response)
        self._response = response

    def get_response(self) -> Response:
        return self._response

    def send(self, endpoint: str, method: str, **kwargs: dict) -> Response:
        response = requests.request(
            method=method,
            url=f'{settings.THIRD_PARTY_APP_URL}/{self.__APP_ID}/{endpoint}/',
            json=self.get_parameters(),
            # headers=self.get_headers(),
            **kwargs
        )
        del response.headers["Connection"]
        del response.headers["Keep-Alive"]
        return response

    @staticmethod
    def on_success(response: Response) -> Response:
        return response

    @staticmethod
    def on_error(response: Response) -> Response:
        return response
