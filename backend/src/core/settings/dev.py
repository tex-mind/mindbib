from __future__ import annotations

import os
import socket
import sys

from .base import *  # noqa


def zxc():
    pass


# ========================
# DEVELOPMENT
# ========================
DEBUG = bool(os.getenv("DEBUG", "True"))
TESTING = sys.argv[1:2] == ["test"]

# ========================
# SITES
# ========================
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]
try:
    # # the below two lines make it possible to use django-debug-toolbar inside of docker locally
    # # https://knasmueller.net/fix-djangos-debug-toolbar-not-showing-inside-docker
    # # https://stackoverflow.com/questions/10517765/django-debug-toolbar-not-showing-up
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
except OSError:
    # usually raised if this is being run outside of a docker container context
    INTERNAL_IPS = []


# ========================
# CSRF
# ========================
# CSRF_TRUSTED_ORIGINS = []
CSRF_COOKIE_SECURE = False
