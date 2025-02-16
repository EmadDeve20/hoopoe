from django.urls import path, include

urlpatterns = [
    path('', include(('hoopoe.users.urls', 'users')))
]
