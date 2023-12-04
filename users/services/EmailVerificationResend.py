from common.CustomRoute import CustomRoute


class EmailVerificationResend(CustomRoute):

    def send(self, endpoint: str, method: str, **kwargs: dict) -> None:
        return super().send(endpoint=endpoint, method=method)

