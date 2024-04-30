from __future__ import annotations

from pathlib import Path

from environs import Env

env = Env()
env.read_env()

# ------------------------
# BASE
# ------------------------
BASE_DIR = Path(__file__).resolve(strict=True).parent
DEBUG = env.bool("DEBUG", default="False")
SECRET_KEY = env.str("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("Secret Key is Required")

# ------------------------
# SITES
# ------------------------
DEFAULT_SCHEME: str = "https"
MAIN_DOMAIN: list = env.list("MAIN_DOMAIN", default=["mindbin.local"])
ALLOWED_HOSTS: list = env.list("ALLOWED_HOSTS", default=["mindbin.local"])
BASE_URL: str = f"{DEFAULT_SCHEME}://{MAIN_DOMAIN}"

# ------------------------
# CSRF
# ------------------------
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["https://minbin.local"])
# CSRF_COOKIE_DOMAIN =
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default="True")
CSRF_COOKIE_AGE = 28800

# ------------------------
# APPS
# ------------------------
BASE_APPS = [
    # Project apps
    "core",
]
INSTALLED_APPS = BASE_APPS


# ------------------------
# MIDDLEWARE
# ------------------------
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

# ------------------------
# URLS
# ------------------------
ROOT_URLCONF = "core.urls"
APPEND_SLASH = True

# ------------------------
# DB
# ------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.str("POSTGRES_PORT"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "NAME": env.str("POSTGRES_DB"),
        "TEST": {
            "NAME": env.str("POSTGRES_TEST_DB", default="minbin_test"),
        },
    }
}

# ------------------------
# Internationalization
# ------------------------
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
