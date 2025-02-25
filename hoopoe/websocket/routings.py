from django.urls import path

from hoopoe.websocket.middleware.jwt_auth import AdminJWTAuthMiddlewareStack
from hoopoe.websocket.consumer_chat import ChatConsumer

app_name = "websocket"

websocket_urlpatterns = [
    path(
        "ws/chat-socket/",
        AdminJWTAuthMiddlewareStack(ChatConsumer.as_asgi()),
        name="chat_socket"
    )
]