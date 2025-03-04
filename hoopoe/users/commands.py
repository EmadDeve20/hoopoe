import os

from config.django.base import BASE_DIR


class UserCommands:
    default_profile_img_path = "images/default/accounts/"

    def create_default_profile_image(self) -> bool:
        target_path = f"{BASE_DIR}/hoopoe/media/{self.default_profile_img_path}"

        if not os.path.exists(target_path):
            os.system(f"mkdir -p {target_path}")

        if not os.path.isfile(target_path + "/default.jpg"):
            image_in_assets = (
                f"{BASE_DIR}/hoopoe/assets/{self.default_profile_img_path}/default.jpg"
            )
            image_to_media = (
                f"{BASE_DIR}/hoopoe/media/{self.default_profile_img_path}/default.jpg"
            )
            os.system(f"cp {image_in_assets} {image_to_media} ")

        return True
