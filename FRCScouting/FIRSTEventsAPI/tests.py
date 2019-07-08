from django.test import TestCase
from .utils import *

class UtilsTestCase(TestCase):
    def test_get_API_key(self):
        api_key = get_API_key()
        self.assertEqual(api_key, b'c2FtcGxldXNlcjo3ZWFhNjMzOC1hMDk3LTQyMjEtYWMwNC1iNjEyMGZjYzRkNDk=')
