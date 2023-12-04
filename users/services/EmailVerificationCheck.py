from common.CustomRoute import CustomRoute


class EmailVerificationCheck(CustomRoute):

    def send(self, endpoint: str, method: str, **kwargs: dict) -> tuple:
        return super().send(endpoint=endpoint, method=method)

