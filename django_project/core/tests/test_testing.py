from django.test import TestCase


class TestingTestCase(TestCase):
    def test_trivial(self):
        self.assertEqual(1, 1)
