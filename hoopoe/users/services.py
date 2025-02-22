from django.db import transaction
from django.contrib.auth import authenticate
from django.core.files.uploadedfile import InMemoryUploadedFile



from rest_framework.request import Request 
from rest_framework.exceptions import ValidationError

from hoopoe.users.models import User, Profile


@transaction.atomic
def create_profile(*, user:User) -> Profile:
    """
    function to create a profile for a user

    Args:
        user (User): user object
    
    Returns:
        Profile: return created Profile object.
    """

    username = user.email.split("@")[0]
    return Profile.objects.create(user=user, username=username)


@transaction.atomic
def register_user(*, email:str, password:str) -> User:
    """
    register user is a function to create User object.

    Args:
        email (str): user email.
        password (str): user password.

    Returns:
        User: return Created User object
    """

    user = User.objects.create(email=email)
    user.set_password(password)
    create_profile(user=user)

    return user


# TODO: Get User better than request
@transaction.atomic
def delete_my_account(request:Request):
    """
    delete my account

    Args:
        request (Request): request object of user request.
    """

    user = request.user
    user.delete()


# TODO: Get User better than request
@transaction.atomic
def change_my_password(*, request:Request, user_requester:User,
password:str, new_password:str):
    """
    change password of user

    Args:
        user_requester (User): user object want to change his password
        password (str): correct password
        new_password (str): new password to change password

    Raises:
        ValidationError: raise validation error if password for user is not
        correct.
    """

    if not authenticate(username=user_requester.email, password=password):
        raise ValidationError("Password incorrect!")

    user_requester.set_password(new_password)

    user_requester.save()


# TODO: Remove Old iamge if image updated.
def change_my_profile(*, user:User, bio:str|None, username:str|None,
image:InMemoryUploadedFile|None) -> Profile:
    """
    change my profile details.

    Args:
        user (User): user who want ot change profile.
        bio (str | None): new bio. this is can be None.
        username (str | None): new username. this is can be None
        image (InMemoryUploadedFile | None): profile image. this is can be None

    Returns:
        Profile: return updated Profile object.
    """
    
    profile = user.profile

    if not profile:
        profile = create_profile(user=user)

    profile.bio = bio or profile.bio
    profile.username = username or profile.username
    profile.image = image or profile.image

    profile.save()

    return profile
