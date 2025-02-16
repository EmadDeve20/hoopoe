from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User

class InputRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    # TODO: Complte this function
    # Check this email used or not
    def validate_email(self, email):
        return email

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError("confirm password is not equal to password")

        return data


class OutPutRegisterSerializer(serializers.ModelSerializer):
    class TokenSerializer(serializers.Serializer):
        access = serializers.CharField()
        refresh = serializers.CharField()

        class Meta:
            ref_name = "RegisterToken"

    token = serializers.SerializerMethodField("get_token")

    class Meta:
        model = User 
        fields = ["email", 
                  "token"]

    def get_token(self, user:User) -> TokenSerializer:
        return user.get_token()

