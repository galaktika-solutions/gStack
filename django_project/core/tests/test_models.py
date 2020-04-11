from django.test import TestCase

from core.factories import KeyValueStoreFactory


class KeyValueStoreTestCase(TestCase):
    maxDiff = None

    @classmethod
    def setUpTestData(cls):
        cls.obj = KeyValueStoreFactory()

    def test_str(self):
        self.assertEqual(type(self.obj.__str__()), str)
