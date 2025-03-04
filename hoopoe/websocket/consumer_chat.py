import ast

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from hoopoe.users.models import User
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


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        try:
            self.user = self.scope["user"]

            if self.user is None:
                if "message" in self.scope:
                    await self.accept()
                    await self.send(self.scope["message"])
                await self.close(code=4003)

        except KeyError:
            await self.accept()
            if "message" in self.scope:
                await self.send(self.scope["message"])
            await self.close(code=4003)
        except Exception:
            await self.close(code=4102)

        # TODO: username in profile must to be unique for each user.
        self.my_username = await get_my_username(user=self.user)
        if self.my_username is None:
            await self.close(401)

        else:
            await self.channel_layer.group_add(self.my_username, self.channel_name)

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        data = await sync_to_async(ast.literal_eval)(text_data)

        # TODO: handle data recive with class or function to automaticly
        if "action" in data:
            if data["action"] == "check_connection":
                event = {
                    "message": {
                        "action": "check_connection",
                        "is_connecting": True,
                    }
                }
                await self.send_message(event)

            if data["action"] == "send_message":
                # data in action will be like this:
                # {"message": "hello", "receiver": "emaddeve20"}
                message = data["data"]["message"]
                receiver = data["data"]["receiver"]

                await self.send_message_to_receiver(message, receiver)

    async def send_message_to_receiver(self, message, receiver):
        receiver_channel_name = receiver
        await self.channel_layer.group_send(
            receiver_channel_name,
            {
                "type": "send_message",
                "message": message,
                "sender": self.my_username,
            },
        )

    async def send_message(self, event: dict):
        """
        send message

        Args:
            event (dict): event must be have message key with message data.
        """
        message = event["message"]
        sender = event.get("sender")
        data = {"message": message, "sender": sender if sender else None}
        await self.send_json(data)

    async def disconnect(self, code):
        if self.user.is_authenticated:
            await self.channel_layer.group_discard(self.my_username, self.channel_name)
