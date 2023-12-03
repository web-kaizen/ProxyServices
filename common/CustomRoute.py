from overrides import overrides
from rest_framework.response import Response

from common.Route import Route


class CustomRoute(Route):

    @overrides
    def set_response(self, response: Response, status: str = None):
        if 'result' in response:
            super().set_response(response['result'], status)
            response['result'] = super().get_response()
        if 'error' in response:
            super().set_response(response['error'], status)
            response['error'] = super().get_response()
        self._response = response
