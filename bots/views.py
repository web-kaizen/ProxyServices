from typing import Any
from urllib.request import Request

from rest_framework.response import Response
from rest_framework.views import APIView

from common.Route import Route


class BotListView(APIView):
    """Returns the list of existed bots"""

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        response = Route(request=request).send(endpoint='bots')
        return Response(
            data=response.json(),
            status=response.status_code,
            headers=response.headers
        )


class BotDetailsView(APIView):
    """Returns details for a specific bot"""

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        response = Route(request=request).send(endpoint=f'bots/{kwargs.get("bot_id")}')
        return Response(
            data=response.json(),
            status=response.status_code,
            headers=response.headers
        )
