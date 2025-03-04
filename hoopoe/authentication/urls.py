from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path(
        "jwt/",
        include(
            (
                [
                    path("login/", TokenObtainPairView.as_view(), name="login"),
                    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
                ]
            )
        ),
        name="jwt",
    ),
]
