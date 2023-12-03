import requests
from django.conf import settings
from requests import Response


class Route:
    """Base Route for communication with third-party services"""

    __APP_ID: str = settings.APP_ID
    _parameters: dict = {}
    _response: Response = None

    def set_parameters(self, params: dict) -> None:
        self._parameters = params

    def get_parameters(self) -> dict:
        return self._parameters

    def set_response(self, response: Response) -> None:
        self._response = response

    def get_response(self) -> Response:
        return self._response

    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        response = requests.request(
            method=method,
            url=f'{settings.THIRD_PARTY_APP_URL}/{self.__APP_ID}/{endpoint}',
            data=self._parameters,
            **kwargs
        )
        self.set_response(response=response)
