from hoopoe.chat_messages.models import Contacts
from hoopoe.users.models import User


def get_contacts_by_user_model(*, user: User) -> Contacts:
    """
    get Contacts by user

    Args:
        user (User): user object model

    Returns:
        Contacts: return Contacts model by User
    """

    contacts, _ = Contacts.objects.get_or_create(user=user)

    return contacts
