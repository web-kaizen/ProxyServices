from requests import Response

from common.CustomRoute import CustomRoute


class EmailVerificationResend(CustomRoute):

    def send(self, endpoint: str, method: str, **kwargs: dict) -> Response:
        return super().send(endpoint=endpoint, method=method)

