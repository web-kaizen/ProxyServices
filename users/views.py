from typing import Any

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.route import Route
from logger.services.Logger import Logger
from proxy.decorators import handle_json_decode_error


class __BaseUserOperationView(APIView):
    """Base class for users registration and login"""

    route_class: Any = Route
    endpoint: str = None

    @handle_json_decode_error
    def __send_request(self, request: Request) -> Response:
        response = Route(request=request).send(endpoint=self.endpoint)
        Logger().log_proxy_response_to_client(response=response)
        Logger().save_to_db()
        return response

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
