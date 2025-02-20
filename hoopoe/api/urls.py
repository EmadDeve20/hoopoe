from django.urls import path, include

urlpatterns = [
    path('', include(('hoopoe.users.urls', 'users'))),
    path('', include(('hoopoe.authentication.urls', 'authentication'))),
]
