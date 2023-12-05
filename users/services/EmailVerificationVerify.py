from common.CustomRoute import CustomRoute
from requests import Response


class EmailVerificationVerify(CustomRoute):

    def send(self, endpoint: str, method: str, **kwargs: dict) -> Response:
        return super().send(endpoint=endpoint, method=method)

