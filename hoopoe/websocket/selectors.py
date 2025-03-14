from uuid import UUID

from asgiref.sync import sync_to_async

from hoopoe.users.models import Profile, User
from hoopoe.users.selectors import get_my_profile


async def get_my_username(user: User) -> str | None:
    """
    get my username

    Args:
        user (User): user requester for this

    Returns:
        str|None: return username if founded.
    """
    try:
        profile = await sync_to_async(get_my_profile)(user=user)
        username = profile.username
        return username
    except Exception:
        return None


async def get_user_id_from_username(username: str) -> UUID:
    """
    get id of User model for username of Profile object

    Args:
        username (str): username field of in Profile object

    Returns:
        UUID: retrurn id of User model
    """

    profile = await sync_to_async(Profile.objects.get)(username=username)

    user = await sync_to_async(getattr)(profile, "user")

    return user.pk
