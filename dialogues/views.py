from typing import Any
from urllib.request import Request

from rest_framework.response import Response
from rest_framework.views import APIView


class DialoguesView(APIView):
    """View for dialogues CRUD opeartions"""

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        pass
