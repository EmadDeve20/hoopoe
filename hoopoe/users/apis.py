from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from hoopoe.api.mixins import ApiAuthMixin
from hoopoe.users.selectors import get_my_profile, get_profile_by_username
from hoopoe.users.serializers import (
    InputChangeMyProfile,
    InputChangePassword,
    InputRegisterSerializer,
    OutputProfileSerializer,
    OutPutRegisterSerializer,
)
from hoopoe.users.services import (
    change_my_password,
    change_my_profile,
    delete_my_account,
    register_user,
)


class MyProfileApi(ApiAuthMixin, APIView):
    parser_classes = [MultiPartParser]

    @extend_schema(tags=["My Profile"], responses=OutputProfileSerializer)
    def get(self, request):
        my_profile = get_my_profile(user=request.user)
        output_serializer = OutputProfileSerializer(
            my_profile, context={"request": request}
        )

        return Response(output_serializer.data)

    @extend_schema(
        tags=["My Profile"],
        responses=OutputProfileSerializer,
        request=InputChangeMyProfile,
    )
    def patch(self, request):
        serializer = InputChangeMyProfile(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        image = serializer.validated_data.get("image")
        bio = serializer.validated_data.get("bio")
        username = serializer.validated_data.get("username")

        new_profile = change_my_profile(
            user=user, bio=bio, username=username, image=image
        )

        output_serializer = OutputProfileSerializer(
            new_profile, context={"request": request}
        )
        return Response(output_serializer.data)

    @extend_schema(tags=["My Profile"])
    def delete(self, request):
        delete_my_account(request=request)

        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersProfile(ApiAuthMixin, APIView):
    @extend_schema(tags=["Users Profile"], responses=OutputProfileSerializer)
    def get(self, request, username):
        profile = get_profile_by_username(username=username)

        output_serializer = OutputProfileSerializer(profile)

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


class ChangeMyPassword(ApiAuthMixin, APIView):
    @extend_schema(tags=["My Profile"], request=InputChangePassword)
    def post(self, request):
        serializer = InputChangePassword(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        password = serializer.validated_data.get("password")
        new_password = serializer.validated_data.get("new_password")

        change_my_password(
            request=request,
            user_requester=user,
            password=password,
            new_password=new_password,
        )

        return Response(status=status.HTTP_200_OK)
