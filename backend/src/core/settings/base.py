from __future__ import annotations

import os
from pathlib import Path

# ------------------------
# BASE
# ------------------------
BASE_DIR = Path(__file__).resolve().parents[2]
DEBUG = bool(os.getenv("DEBUG", "False"))
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("Secret Key is Required")

# ========================
# SITES
# ========================
DEFAULT_SCHEME = "https"
MAIN_DOMAIN = os.getenv("MAIN_DOMAIN", "mindbin.local")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "mindbin.local").split(",")
BASE_URL = f"{DEFAULT_SCHEME}://{MAIN_DOMAIN}"

# ========================
# CSRF
# ========================
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "https://gck.local").split(",")
# CSRF_COOKIE_DOMAIN =
CSRF_COOKIE_SECURE = bool(os.getenv("CSRF_COOKIE_SECURE", "True"))
CSRF_COOKIE_AGE = 28800

# ========================
# APPS
# ========================
INSTALLED_APPS = [
    # Custom
    "core",
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

# ========================
# URLS
# ========================
# ROOT_URLCONF = "core.urls"
APPEND_SLASH = True

# ========================
# DB
# ========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "host.docker.internal",
        "PORT": os.getenv("POSTGRES_PORT"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "NAME": os.getenv("POSTGRES_DB"),
    }
}

# ========================
# Internationalization
# ========================
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
