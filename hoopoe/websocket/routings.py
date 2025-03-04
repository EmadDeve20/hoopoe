from django.urls import path

from hoopoe.websocket.consumer_chat import ChatConsumer
from hoopoe.websocket.middleware.jwt_auth import AdminJWTAuthMiddlewareStack

app_name = "websocket"

websocket_urlpatterns = [
    path(
        "ws/chat-socket/",
        AdminJWTAuthMiddlewareStack(ChatConsumer.as_asgi()),
        name="chat_socket",
    )
]
