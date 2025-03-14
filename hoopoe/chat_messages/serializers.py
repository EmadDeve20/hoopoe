from rest_framework import serializers

from hoopoe.chat_messages.models import Contacts
from hoopoe.users.serializers import OutputProfileSerializer


class MyContactsOutputSerializer(serializers.ModelSerializer):
    profiles = OutputProfileSerializer(many=True)

    class Meta:
        model = Contacts
        fields = ["profiles"]
