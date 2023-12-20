from json.decoder import JSONDecodeError
from typing import Callable, Any

from rest_framework import status
from rest_framework.response import Response


def handle_json_decode_error(request: Callable) -> Any:
    def _wrapped_view(*args: Any, **kwargs: dict) -> Response:
        try:
            response = request(*args, **kwargs)

            if response.content:
                data = response.json()
                return Response(data=data, status=response.status_code, headers=response.headers)
            else:
                return Response(status=response.status_code, headers=response.headers)

        except JSONDecodeError:
            return Response(data={'error': 'Invalid JSON response'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return _wrapped_view
