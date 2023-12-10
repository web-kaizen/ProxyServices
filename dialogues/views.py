from typing import Any
from urllib.request import Request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.Route import Route
from dialogues.serializers import DialoguesSerializer

from drf_yasg.utils import swagger_auto_schema


class DialoguesView(APIView):
    """View for dialogues CRUD operations"""

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        """
        offset -- A first parameter
        limit -- A second parameter
        """
        dialogue_id = kwargs.get('dialogue_id')
        endpoint = f'dialogues/{dialogue_id}' if dialogue_id else 'dialogues'
        response = Route(request=request).send(endpoint=endpoint)
        return Response(data=response.json(), status=response.status_code, headers=response.headers)

    @swagger_auto_schema(request_body=DialoguesSerializer)
    def post(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        return self.__handle_request(request=request, kwargs=kwargs)

    @swagger_auto_schema(request_body=DialoguesSerializer)
    def put(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        return self.__handle_request(request=request, kwargs=kwargs)

    @swagger_auto_schema(request_body=DialoguesSerializer)
    def patch(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        return self.__handle_request(request=request, kwargs=kwargs)

    def delete(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        return self.__handle_request(request=request, kwargs=kwargs)

    def __handle_request(self, request, **kwargs):
        dialogue_id = kwargs.get('dialogue_id')
        endpoint = f'dialogues/{dialogue_id}' if dialogue_id else 'dialogues'

        if request.method in ('PUT', 'PATCH',):
            serializer = DialoguesSerializer(data=request.data, partial=(request.method == 'PATCH'))
            if not serializer.is_valid():
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        response = Route(request=request).send(endpoint=endpoint)
        return Response(data=response.json(), status=response.status_code, headers=response.headers)
