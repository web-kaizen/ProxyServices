from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.Route import Route


class __BaseUserOperationView(APIView):
    """Base class for users registration and login"""

    route_class: Any = Route
    endpoint: str = None

    def __send_request(self, request: Request) -> Response:
        response = Route(request=request).send(endpoint=self.endpoint)
        return Response(data=response.json(), status=response.status_code, headers=response.headers)

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        return self.__send_request(request=request)

    def post(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        return self.__send_request(request=request)


class UserRegistrationView(__BaseUserOperationView):
    """Registers User in the third-party service"""

    endpoint = 'users'


class LoginView(__BaseUserOperationView):
    """Logins User in the third-party service"""

    endpoint = 'users/login'


class LogoutView(__BaseUserOperationView):
    """Logouts User in the third-party service"""

    endpoint = 'users/logout'


class EmailVerificationCheckView(__BaseUserOperationView):
    """Checks Email Verification status"""

    endpoint = 'users/email-verification/check'


class EmailVerificationResendView(__BaseUserOperationView):
    """Resends Email Verification"""

    endpoint = 'users/email-verification/resend'


class EmailVerificationVerifyView(__BaseUserOperationView):
    """Verifies Email"""

    endpoint = 'users/email-verification/verify'
