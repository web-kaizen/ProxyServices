from common.CustomRoute import CustomRoute
from requests import Response


class BotList(CustomRoute):
    """Bots list route"""
    def send(self, endpoint: str, method: str, **kwargs: dict) -> Response:
        return super().send(endpoint=endpoint, method=method)
