from django.db import transaction
from django.contrib.auth import authenticate


from rest_framework.request import Request 
from rest_framework.exceptions import ValidationError

from hoopoe.users.models import User, Profile


def create_profile(*, user:User):
    """
    function to create a profile for a user

    Args:
        user (User): user object
    """
    username = user.email.split("@")[0]
    Profile.objects.create(user=user, username=username)


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

@transaction.atomic
def delete_my_account(request:Request):
    """
    delete my account

    Args:
        request (Request): request object of user request.
    """

    user = request.user
    user.delete()


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
