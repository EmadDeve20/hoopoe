from urllib.parse import parse_qs

from channels.auth import AuthMiddlewareStack
from django.db import close_old_connections
from django_channels_jwt_auth_middleware.auth import (
    JWTAuthMiddleware as _JWTAuthMiddleware,
)
from jwt import DecodeError, ExpiredSignatureError, InvalidSignatureError


class AdminJWTAuthMiddleware(_JWTAuthMiddleware):
    async def __call__(self, scope, receive, send):
        try:
            jwt_token = None
            query_string = scope["query_string"].decode("utf-8")
            query_string = parse_qs(query_string)
            if "token" in query_string and query_string["token"]:
                jwt_token = query_string["token"][0]
            if jwt_token:
                jwt_payload = self.get_payload(jwt_token)
                user_credentials = self.get_user_credentials(jwt_payload)
                user = await self.get_logged_in_user(user_credentials)
                scope["user"] = user
                scope["message"] = None
            else:
                scope["message"] = "Authentication credentials were not provided."

        except (
            InvalidSignatureError,
            KeyError,
            ExpiredSignatureError,
            DecodeError,
        ) as ex:
            scope["message"] = f"{ex}"
        except Exception as ex:
            scope["message"] = f"{ex}"
        return await self.app(scope, receive, send)


def AdminJWTAuthMiddlewareStack(app):
    return AdminJWTAuthMiddleware(AuthMiddlewareStack(app))
