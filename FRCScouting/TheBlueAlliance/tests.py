from django.test import TestCase
from . import utils

class UtilsTestCase(TestCase):
    def test_validate_teamkey(self):
            self.assertEqual(utils.validate_teamkey(123), True, "Should be True")
