from common.CustomRoute import CustomRoute


class BotDetails(CustomRoute):
    """Bot details route"""
    
    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        return super().send(endpoint=endpoint, method=method)
