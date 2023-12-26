from django.conf import settings
from requests import Response

from logger.models import LogModel


class Logger:

    def __init__(self, response: Response) -> None:
        self.response = response

    def write(self) -> None:
        if settings.IS_NEED_LOGGER:
            log = LogModel(
                proxy_method=self.response.request.method,
                proxy_url=self.response.request.url,
                proxy_request_headers=self.response.request.headers,
                proxy_request_body=self.response.request.body.decode('utf-8'),
                core_url=self.response.url,
                core_response_headers=self.response.headers,
                core_response_body=self.response.text,
                core_response_status_code=self.response.status_code,
            )
            log.save()
