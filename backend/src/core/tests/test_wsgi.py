from __future__ import annotations

import os

from django.core.wsgi import get_wsgi_application
from django.test import SimpleTestCase


class WSGITestCase(SimpleTestCase):
    def test_get_wsgi_application_not_none(self):
        application = get_wsgi_application()
        self.assertIsNotNone(application)

    def test_settings_module_correct_value(self):
        settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
        self.assertEqual(settings_module, "core.settings.test")
