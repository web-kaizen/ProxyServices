from overrides import override

from common.Route import Route


class UserLogin(Route):
    """User login route"""

    @override
    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        super().send(endpoint=endpoint, method=method, kwargs=kwargs)
