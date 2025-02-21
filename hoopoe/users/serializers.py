from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from hoopoe.users.models import User, Profile
from hoopoe.utils.validations.validators import check_field_is_unique

class InputRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def validate_email(self, email):
        return check_field_is_unique(email, User, field="email")
        
    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise ValidationError("confirm password is not equal to password.")

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


class OutputProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            "bio",
            "image",
            "username"
        ]



class InputChangePassword(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        new_password = attrs["new_password"]
        confirm_password = attrs["confirm_password"]

        if new_password != confirm_password:
            raise ValidationError("confirm password is not equal to password.")

        return attrs