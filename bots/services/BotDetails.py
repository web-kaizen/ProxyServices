from overrides import override

from common.Route import Route


class BotDetails(Route):
    """Bot details route"""

    @override
    def send(self, endpoint: str, method: str) -> None:
        super().send(endpoint=endpoint, method=method)
