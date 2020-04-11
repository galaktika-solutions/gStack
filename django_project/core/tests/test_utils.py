from django.test import TestCase
from django.conf import settings
import django

from core.utils import read_secret


class UtilsTestCase(TestCase):
    maxDiff = None

    def test_read_secret(self):
        django.setup()
        self.assertEqual(
            settings.SECRET_KEY,
            read_secret('DJANGO_SECRET_KEY')
        )
