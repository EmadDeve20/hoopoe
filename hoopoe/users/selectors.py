from rest_framework.request import Request
from rest_framework.exceptions import NotFound


from hoopoe.users.models import Profile


def get_my_profile(request:Request) -> Profile:
    """
    function to get user logging profile

    Args:
        request (Request): get request of user requested

    Raises:
        NotFound: Error if Profile Notfound!

    Returns:
        Profile: return profile object of user requestr
    """
    user = request.user
    
    try:
        return Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        raise NotFound("Sorry Your Prifle Notfound!")

