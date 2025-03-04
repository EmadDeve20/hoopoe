from django.core.management.base import BaseCommand

from hoopoe.users.commands import UserCommands


class Command(BaseCommand):
    help = "This is An Initializer. run it in first time in your first run."

    def handle(self, *args, **options):
        user_commands = UserCommands()

        # ============================== User Commands ============================

        if user_commands.create_default_profile_image():
            self.stdout.write(
                self.style.SUCCESS("added Default Profile Image Successfuly.")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS("failed to add Default Profile Image!")
            )
