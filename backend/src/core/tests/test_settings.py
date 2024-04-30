from __future__ import annotations

from django.conf import settings
from django.test import SimpleTestCase


class TestCaseSettings(SimpleTestCase):
    def test_append_slash_var_exists(self):
        self.assertIsNotNone(settings.APPEND_SLASH)
