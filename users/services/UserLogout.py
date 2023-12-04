from common.CustomRoute import CustomRoute


class UserLogout(CustomRoute):
    """User logout route"""

    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        return super().send(endpoint=endpoint, method=method)

