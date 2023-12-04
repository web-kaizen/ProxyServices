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
        # route.send(endpoint=self.endpoint, method=request.method)
        response, status_code = bot_list_route.send(endpoint=f"{self.endpoint}{kwargs.get('bot_id') if kwargs.get('bot_id') is not None else ''}", method=request.method, kwargs=None)
        return Response(
            data=response,
            status=status_code
        )


class BotListView(__BaseBotsOperationView):
    """Returns the list of existed bots"""

    route_class = BotList.BotList
    endpoint = 'bots'


class BotDetailsView(__BaseBotsOperationView):
    """Returns the list of existed bots"""

    route_class = BotList.BotList
    endpoint = "bots/"



#
#
# class BotListView(APIView):
#     """Returns the list of existed bots"""
#
#     @staticmethod
#     def get(request: Request, *args: Any, **kwargs: dict) -> Response:
#         bot_list_route = BotList()
#         bot_list_route.send(endpoint='bots', method=request.method)
#         return Response(
#             data=bot_list_route.get_response().json(),
#             status=bot_list_route.get_response().status_code
#         )
#
#
# class BotDetailsView(APIView):
#     """Returns detailed info about bot"""
#
#     @staticmethod
#     def get(request: Request, *args: Any, **kwargs: dict) -> Response:
#         bot_details_route = BotDetails()
#         bot_details_route.send(endpoint=f'bots/{kwargs.get("bot_id")}', method=request.method)
#         return Response(
#             data=bot_details_route.get_response().json(),
#             status=bot_details_route.get_response().status_code
#         )
