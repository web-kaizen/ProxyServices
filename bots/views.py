from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from bots.services.BotDetails import BotDetails
from bots.services.BotList import BotList


class BotListView(APIView):
    """Returns the list of existed bots"""

    @staticmethod
    def get(request: Request, *args: Any, **kwargs: dict) -> Response:
        bot_list_route = BotList()
        bot_list_route.send(endpoint='bots', method=request.method)
        return Response(
            data=bot_list_route.get_response().json(),
            status=bot_list_route.get_response().status_code
        )


class BotDetailsView(APIView):
    """Returns detailed info about bot"""

    @staticmethod
    def get(request: Request, *args: Any, **kwargs: dict) -> Response:
        bot_details_route = BotDetails()
        bot_details_route.send(endpoint=f'bots/{kwargs.get("bot_id")}', method=request.method)
        return Response(
            data=bot_details_route.get_response().json(),
            status=bot_details_route.get_response().status_code
        )
