from json.decoder import JSONDecodeError
from rest_framework.response import Response
from rest_framework import status



def handle_json_decode_error(request):
    def _wrapped_view(*args, **kwargs):
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
