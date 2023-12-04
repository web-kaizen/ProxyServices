from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserLoginRegisterSerializer
from users.services import UserLogin, UserRegistration, UserLogout, EmailVerificationCheck, EmailVerificationResend, EmailVerificationVerify


class __BaseUserOperationView(APIView):
    """Base class for users registration and login"""

    route_class: Any = None
    endpoint: str = None

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        route = self.route_class()
        route.set_headers(request.headers)
        # route.send(endpoint=self.endpoint, method=request.method)
        response, status_code = route.send(endpoint=self.endpoint, method=request.method, kwargs=None)
        return Response(
            data=response,
            status=status_code
        )


    @swagger_auto_schema(request_body=UserLoginRegisterSerializer)
    def post(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        serializer = UserLoginRegisterSerializer(data=request.data)
        if serializer.is_valid():
            route = self.route_class()
            route.set_headers(request.headers)
            route.set_parameters(params=serializer.validated_data)
            # route.send(endpoint=self.endpoint, method=request.method, kwargs=None)
            response, status_code = route.send(endpoint=self.endpoint, method=request.method, kwargs=None)
            return Response(
                data=response,
                status=status_code
            )
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(__BaseUserOperationView):
    """Registers User in the third-party service"""

    route_class = UserRegistration.UserRegistration
    endpoint = 'users'


class LoginView(__BaseUserOperationView):
    """Logins User in the third-party service"""

    route_class = UserLogin.UserLogin
    endpoint = 'users/login'


class LogoutView(__BaseUserOperationView):
    """Logins User in the third-party service"""

    route_class = UserLogout.UserLogout
    endpoint = 'users/logout'


class EmailVerificationCheckView(__BaseUserOperationView):

    route_class = EmailVerificationCheck.EmailVerificationCheck
    endpoint = "users/email-verification/check"


class EmailVerificationResendView(__BaseUserOperationView):

    route_class = EmailVerificationResend.EmailVerificationResend
    endpoint = "users/email-verification/resend"


class EmailVerificationVerifyView(__BaseUserOperationView):

    route_class = EmailVerificationVerify.EmailVerificationVerify
    endpoint = "users/email-verification/verify"
