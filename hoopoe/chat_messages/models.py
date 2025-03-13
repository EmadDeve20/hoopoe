from uuid import UUID, uuid4

from django.utils import timezone

from config.django.base import mongo_db


class MongoMessageModel:
    """
    model to save messages between sender and reciver of a chat.\

    fields:
        sender_id and reciver_id: must be id of User object.
        message: message must to be a string message.
        datetime and message_id will be generate automaticly.
    """

    sender_id: UUID | str | None = None
    reciver_id: UUID | str | None = None
    message: str = ""
    datetime: timezone = timezone.now()
    message_id: UUID = uuid4()

    @property
    def reciver(self):
        """
        get User model reciver or just reciver_id field.

        Returns:
            User | UUID
        """
        from hoopoe.users.models import User

        try:
            return User.objects.get(id=self.reciver_id)
        except User.DoesNotExist:
            return self.reciver_id

    @property
    def sender(self):
        """
        get User model of sender or just sender_id field.

        Returns:
            User | UUID
        """
        from hoopoe.users.models import User

        try:
            return User.objects.get(id=self.sender_id)
        except User.DoesNotExist:
            return self.sender_id

    def save(self):
        """
        save fields to db
        """

        json_data = self.fields_to_dict

        # This is for save my saved messages. like telegram or saved posts in instagram
        if self.sender == self.reciver:
            saved_message_collection = mongo_db.get_collection(
                f"{self.sender_id}-saved_messages"
            )
            saved_message_collection.insert_one(json_data)

        else:
            sender_collection = mongo_db.get_collection(f"{self.sender_id}-messages")
            reciver_collection = mongo_db.get_collection(f"{self.reciver_id}-messages")

            sender_collection.insert_one(json_data)

            reciver_collection.insert_one(json_data)

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

    @property
    def fields_to_dict(self) -> dict:
        """
        make fields input to dict type.

        Returns:
            dict: dict with key of fields and value is value of each fields.
        """
        self.check_validate()

        dict_data = {
            "sender_id": str(self.sender_id),
            "reciver_id": str(self.reciver_id),
            "message": self.message,
            "datetime": str(self.datetime),
            "message_id": str(self.message_id),
        }

        return dict_data
