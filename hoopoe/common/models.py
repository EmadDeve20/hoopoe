from uuid import UUID, uuid4

from django.db import models
from django.utils import timezone

from config.django.base import mongo_db


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MongoMessageModel:
    """
    model to save messages between sender and reciver of a chat.
    """

    sender_id: UUID | None = None
    reciver_id: UUID | None = None
    message: str = ""
    datetime: timezone = timezone.now()
    message_id: UUID = uuid4()

    @property
    def reciver(self):
        return self.reciver_id

    @property
    def sender(self):
        return self.sender_id

    def save(self):
        self.check_validate()

        sender_collection = mongo_db.get_collection(f"{self.sender_id}-messages")
        reciver_collection = mongo_db.get_collection(f"{self.reciver_id}-messages")

        sender_collection.insert_one(
            {
                "sender_id": str(self.sender_id),
                "reciver_id": str(self.reciver_id),
                "message": self.message,
                "datetime": str(self.datetime),
                "message_id": str(self.message_id),
            }
        )

        reciver_collection.insert_one(
            {
                "sender_id": str(self.sender_id),
                "reciver_id": str(self.reciver_id),
                "message": self.message,
                "datetime": str(self.datetime),
                "message_id": str(self.message_id),
            }
        )

    def check_validate(self):
        """
        check data is valid to save or not

        Raises:
            ValueError: if sender_id is None
            ValueError: if reciver_id is None
            ValueError: if length of message is zero
        """

        if self.sender_id is None:
            raise ValueError("sender_id can not be None!")

        if self.reciver_id is None:
            raise ValueError("reciver_id can not be None!")

        if self.message == "":
            raise ValueError(
                "The length of the message has to be greater than or equal to one."
            )
