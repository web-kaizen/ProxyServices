from common.CustomRoute import CustomRoute


class BotList(CustomRoute):
    """Bots list route"""

    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        return super().send(endpoint=endpoint, method=method)
