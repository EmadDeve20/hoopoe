from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from hoopoe.api.mixins import ApiAuthMixin
from hoopoe.users.selectors import get_my_profile
from .services import register_user
from .serializers import (
InputRegisterSerializer,
OutPutRegisterSerializer,
OutputProfileSerializer
)
from drf_spectacular.utils import extend_schema

class MyProfileApi(ApiAuthMixin, APIView):
    @extend_schema(
        tags=["Profile"],
        responses=OutputProfileSerializer
    )
    def get(self, request):
        my_profile = get_my_profile(request=request)
        output_serializer = OutputProfileSerializer(my_profile,
                                                    context={"request":request})

        return Response(output_serializer.data)


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

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

