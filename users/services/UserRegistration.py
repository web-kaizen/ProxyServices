from common.CustomRoute import CustomRoute


class UserRegistration(CustomRoute):
    """User registration route"""

    def send(self, endpoint: str, method: str, **kwargs: dict) -> tuple:
        return super().send(endpoint=endpoint, method=method)
