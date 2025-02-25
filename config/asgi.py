"""
ASGI config for hoopoe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

import django

django.setup()
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from hoopoe.websocket import routings as websock_routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.local")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": URLRouter(websock_routing.websocket_urlpatterns),
    }
)
