from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# from hoopoe.api.mixins import ApiAuthMixin
# from hoopoe.users.selectors import get_profile
from .services import register_user
from .serializers import (
InputRegisterSerializer,
OutPutRegisterSerializer,
)
from drf_spectacular.utils import extend_schema

# TODO: Create this API to get My Profile Info
# class ProfileApi(ApiAuthMixin, APIView):

#     class OutPutSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Profile 
#             fields = ("bio", "posts_count", "subscriber_count", "subscription_count")

#     @extend_schema(responses=OutPutSerializer)
#     def get(self, request):
#         query = get_profile(user=request.user)
#         return Response(self.OutPutSerializer(query, context={"request":request}).data)


class RegisterApi(APIView):

    @extend_schema(
        tags=["Register"],
        request=InputRegisterSerializer,
        responses=OutPutRegisterSerializer,
    )
    def post(self, request):
        serializer = InputRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = register_user(
                email=serializer.validated_data.get("email"),
                password=serializer.validated_data.get("password"),
            )
        output_serializer = OutPutRegisterSerializer(user)

        return Response(output_serializer.data)

