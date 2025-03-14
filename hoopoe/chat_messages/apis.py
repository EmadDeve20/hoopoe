from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from hoopoe.api.mixins import ApiAuthMixin
from hoopoe.chat_messages.selectors import get_contacts_by_user_model
from hoopoe.chat_messages.serializers import MyContactsOutputSerializer


class ListMyContactsApi(ApiAuthMixin, APIView):
    @extend_schema(tags=["MyContacts"], responses=MyContactsOutputSerializer)
    def get(self, request):
        my_user = request.user

        my_contacts = get_contacts_by_user_model(user=my_user)

        output_serializer = MyContactsOutputSerializer(my_contacts)

        return Response(output_serializer.data)
