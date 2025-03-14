from django.urls import path

from hoopoe.chat_messages import apis

app_name = "chat_messages"

urlpatterns = [
    path("my-contacts/", apis.ListMyContactsApi.as_view(), name="my_contacts")
]
