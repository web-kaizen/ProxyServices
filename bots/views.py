from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from bots.services import BotDetails, BotList


class __BaseBotsOperationView(APIView):
    """Base class for bots list and details"""

    route_class: Any = None
    endpoint: str = None

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        bot_list_route = self.route_class()
        bot_list_route.set_headers(request.headers)
        response = bot_list_route.send(
            endpoint=f"{self.endpoint}{kwargs.get('bot_id') if kwargs.get('bot_id') is not None else ''}",
            method=request.method,
            headers=request.headers
        )
        return Response(
            data=response.json(),
            status=response.status_code,
        )


class BotListView(__BaseBotsOperationView):
    """Returns the list of existed bots"""

    route_class = BotList.BotList
    endpoint = 'bots'


class BotDetailsView(__BaseBotsOperationView):
    """Returns the list of existed bots"""

    route_class = BotList.BotList
    endpoint = "bots/"


