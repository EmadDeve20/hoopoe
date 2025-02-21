
from django.db import transaction

from rest_framework.request import Request 

from hoopoe.users.models import User


# def create_profile(*, user:BaseUser, bio:str | None) -> Profile:
#     return Profile.objects.create(user=user, bio=bio)

# def create_user(*, email:str, password:str) -> BaseUser:
#     


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

    return user


def delete_my_account(request:Request):
    """
    delete my account

    Args:
        request (Request): request object of user request.
    """

    user = request.user
    user.delete()
