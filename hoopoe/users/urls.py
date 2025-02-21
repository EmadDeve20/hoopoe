from django.urls import path
from hoopoe.users import apis

app_name = "users"

urlpatterns = [
    path('register/', apis.RegisterApi.as_view(),name="register"),
    path('profile/', apis.MyProfileApi.as_view(),name="profile"),
]
