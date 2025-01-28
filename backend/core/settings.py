"""
Django settings for core project.
"""

import os
import environ

from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

PROJECT_NAME = env("PROJECT_NAME")

DEBUG: bool = env.bool("DEBUG")

SECRET_KEY: str = env("SECRET_KEY")


BASE_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS: list[str] = [
    "apps.casts",
    "apps.categories",
    "apps.movies",
    "apps.utils",
]

THIRD_APPS: list[str] = [
    "rest_framework",
    "graphene_django",
    "corsheaders",
    "drf_spectacular",
    "drf_spectacular_sidecar",
]

INSTALLED_APPS: list[str] = BASE_APPS + PROJECT_APPS + THIRD_APPS

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES: list[dict] = [
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

WSGI_APPLICATION = "core.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
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


PASSWORD_HASHERS: list[str] = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

GRAPHENE: dict[str, str] = {
    "SCHEMA": "core.schema.schema",
}

ALLOWED_HOSTS: list = env.list("ALLOWED_HOSTS")

INTERNAL_IPS: list = env.list("INTERNAL_IPS")

CORS_ALLOWED_ORIGINS: list = env.list("CORS_ALLOWED_ORIGINS")

CORS_ALLOW_HEADERS: list[str] = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:3000",
]

CORS_ALLOW_METHODS: list[str] = [
    "GET",
    "POST",
]

CORS_ALLOW_ALL_ORIGINS = True


STATIC_URL = "static/"
STATIC_ROOT: str = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT: str = os.path.join(BASE_DIR, "media")
