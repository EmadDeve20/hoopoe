from django.urls import include, path

urlpatterns = [
    path("", include(("hoopoe.users.urls", "users"))),
    path("", include(("hoopoe.authentication.urls", "authentication"))),
    path("", include(("hoopoe.chat_messages.urls", "chat_messages"))),
]
