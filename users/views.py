from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserLoginRegisterSerializer
from users.services.UserLogin import UserLogin
from users.services.UserRegistration import UserRegistration


class __BaseUserOperationView(APIView):
    """Base class for users registration and login"""

    route_class: Any = None
    endpoint: str = None

    @swagger_auto_schema(request_body=UserLoginRegisterSerializer)
    def post(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        serializer = UserLoginRegisterSerializer(data=request.data)
        if serializer.is_valid():
            route = self.route_class()
            route.set_parameters(params=serializer.validated_data)
            route.send(endpoint=self.endpoint, method=request.method, kwargs=None)
            return Response(
                data=route.get_response().json(),
                status=route.get_response().status_code
            )
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(__BaseUserOperationView):
    """Registers User in the third-party service"""

    route_class = UserRegistration
    endpoint = 'users'


class LoginView(__BaseUserOperationView):
    """Logins User in the third-party service"""

    route_class = UserLogin
    endpoint = 'users/login'
