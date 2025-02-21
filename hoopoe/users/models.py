from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin

from hoopoe.common.models import BaseModel


class BaseUserManager(BUM):
    def create_user(self, email, is_active=True, is_admin=False, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()), is_active=is_active, is_admin=is_admin)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name = "email address",
                              unique=True)

    is_active = models.BooleanField(default=True)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


    def get_token(self) -> dict:
        """
        get refresh token and access token

        Returns:
            dict: return dict type of access and refresh token
        """
        data = dict()
        token_class = RefreshToken

        refresh = token_class.for_user(self)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data

    @property
    def profile(self):
        """
        function to get profile of user

        
        Returns:
            (Profile|None): return Profile of this user.
            this is can be None if Profile of this user not founded.
        """
        return Profile.objects.filter(user=self).first()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="user_profile")
    
    username = models.CharField(max_length=255, default="")

    bio = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, upload_to="media", default=None)

    def __str__(self):
        return f"{self.user}"
