from typing import Any
from urllib.request import Request

from rest_framework.response import Response
from rest_framework.views import APIView

from common.Route import Route


class BotView(APIView):
    """Returns the list of existing bots or details for a specific bot"""

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        bot_id = kwargs.get('bot_id')
        if bot_id is None:
            response = Route(request=request).send(endpoint='bots')
        else:
            response = Route(request=request).send(endpoint=f'bots/{bot_id}')

        return Response(data=response.json(), status=response.status_code, headers=response.headers)
