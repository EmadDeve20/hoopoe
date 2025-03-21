import os

from config.env import BASE_DIR, env

env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "=ug_ucl@yi6^mrcjyz%(u0%&g2adt#bz3@yos%#@*t#t!ypx=a"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])


# Application definition
LOCAL_APPS = [
    "hoopoe.core.apps.CoreConfig",
    "hoopoe.common.apps.CommonConfig",
    "hoopoe.users.apps.UsersConfig",
    "hoopoe.authentication.apps.AuthenticationConfig",
    "hoopoe.captcha.apps.CaptchaConfig",
    "hoopoe.commands.apps.CommandsConfig",
    "hoopoe.websocket.apps.WebsocketConfig",
    "hoopoe.chat_messages.apps.ChatMessagesConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_celery_results",
    "django_celery_beat",
    "corsheaders",
    "drf_spectacular",
    "django_extensions",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    "whitenoise.runserver_nostatic",
    "daphne",  # daphne must before 'django.contrib.staticfiles'
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Asgi config for channels
ASGI_APPLICATION = "config.asgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": env.db(
        "DATABASE_URL", default="psql://user:password@127.0.0.1:5432/hoopoe"
    ),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "user",
            "PASSWORD": "password",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "hoopoe/media")

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "hoopoe.api.exception_handlers.drf_default_with_modifications_exception_handler",
    # 'EXCEPTION_HANDLER': 'hoopoe.api.exception_handlers.hacksoft_proposed_exception_handler',
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}


# Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_LOCATION", default="redis://localhost:6379"),
    }
}

USERNAME_REDIS = env("USERNAME_REDIS", default="hoopoe")
PASSWORD_REDIS = env("PASSWORD_REDIS", default="hoopoe")
HOST_REDIS = env("HOST_REDIS", default="127.0.0.1")
PORT_REDIS = env("PORT_REDIS", cast=int, default=6379)

# database channel layer for websocket
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            # "hosts": [(env("HOST_REDIS"), env("PORT_REDIS", cast=int, default=6379))],
            "hosts": [f"redis://:{PASSWORD_REDIS}@{HOST_REDIS}:{PORT_REDIS}/14"],
            "capacity": 1500,  # default 100
            # "expiry": 100,  # default 60
        },
    },
}

# Cache time to live is 15 minutes.
CACHE_TTL = 60 * 15


APP_DOMAIN = env("APP_DOMAIN", default="http://localhost:8000")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from config.settings.celery import *  # noqa
from config.settings.cors import *  # noqa
from config.settings.jwt import *  # noqa
from config.settings.mongodb import *  # noqa
from config.settings.sessions import *  # noqa
from config.settings.swagger import *  # noqa

# from config.settings.sentry import *  # noqa
# from config.settings.email_sending import *  # noqa
