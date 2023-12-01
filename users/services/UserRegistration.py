from typing import Any

from overrides import override

from common.Route import Route


class UserRegistration(Route):
    """User registration route"""

    @override
    def send(self, endpoint: str, method: str) -> None:
        super().send(endpoint=endpoint, method=method)
