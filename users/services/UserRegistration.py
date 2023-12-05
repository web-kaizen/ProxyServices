from common.CustomRoute import CustomRoute
from requests import Response


class UserRegistration(CustomRoute):
    """User registration route"""
    def send(self, endpoint: str, method: str, **kwargs: dict) -> Response:
        return super().send(endpoint=endpoint, method=method)
