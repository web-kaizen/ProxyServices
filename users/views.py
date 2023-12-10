from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from common.Route import Route
from users.serializers import UserLoginRegisterSerializer


class __BaseUserOperationView(APIView):
    """Base class for users registration and login"""

    route_class: Any = Route
    endpoint: str = None

    def _get_route(self, request: Request) -> Any:
        route = self.route_class(request=request)
        return route

    def _send_request(self, route: Any, request: Request, params: dict = None) -> Response:
        method = request.method
        response = route.send(endpoint=self.endpoint, method=method, kwargs=params)
        return Response(data=response.json(), status=response.status_code, headers=response.headers)

    def get(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        route = self._get_route(request)
        return self._send_request(route, request)

    @swagger_auto_schema(request_body=UserLoginRegisterSerializer)
    def post(self, request: Request, *args: Any, **kwargs: dict) -> Response:
        route = self._get_route(request)
        route.set_parameters(params=request.data)
        return self._send_request(route, request)


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
