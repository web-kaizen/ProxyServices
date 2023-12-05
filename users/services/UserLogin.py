from common.CustomRoute import CustomRoute
from requests import Response


class UserLogin(CustomRoute):
    """User login route"""
    def send(self, endpoint: str, method: str, **kwargs: dict) -> Response:
        return super().send(endpoint=endpoint, method=method)

