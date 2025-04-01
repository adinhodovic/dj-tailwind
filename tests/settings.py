import os

from django.utils.translation import gettext_lazy as _

DEBUG = True

SECRET_KEY = "very-secret"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django.contrib.sessions",
]

MIDDLEWARE = [
    "django.middleware.locale.LocaleMiddleware",
]

THIRD_PARTY_APPS = []

LOCAL_APPS = ["dj_tailwind", "tests"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ]
        },
    }
]

LOCALE_PATHS = [
    os.path.join(os.path.dirname(__file__), "locale"),
]
LANGUAGES = (("en-us", _("English")),)

USE_TZ = False
