from django.urls import path
from hoopoe.users import apis

app_name = "users"

urlpatterns = [
    path('register/', apis.RegisterApi.as_view(),name="register"),
    path('my-profile/', apis.MyProfileApi.as_view(),name="my_profile"),
    path('users-profile/<str:username>/', apis.UsersProfile.as_view(),name="users_profile"),

]
