from common.CustomRoute import CustomRoute


class UserLogin(CustomRoute):
    """User login route"""

    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        return super().send(endpoint=endpoint, method=method)

