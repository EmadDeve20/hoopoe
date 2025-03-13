from uuid import UUID

from hoopoe.chat_messages.models import MongoMessageModel


def save_message(sender_id: UUID, reciver_id: UUID, message: str):
    """
    save messages to mongo db

    Args:
        sender_id (UUID): get sender id. sender id is User id
        reciver_id (UUID): get reciver id. reciver id is Reciver id
        message (str): message text
    """

    model = MongoMessageModel()

    model.reciver_id = reciver_id
    model.sender_id = sender_id
    model.message = message

    model.save()
