from django.test import TestCase
from datetime import date

from TheBlueAlliance.validators import *

class ValidatorsTestCase(TestCase):
    def test_validate_teamkey(self):
        print("Testing TBA validators")
        self.assertEqual(validate_teamkey(123), True, "Should be True")
        self.assertEqual(validate_teamkey(1), True, "Should be True")
        self.assertEqual(validate_teamkey(12), True, "Should be True")
        self.assertEqual(validate_teamkey(1234), True, "Should be True")
        self.assertEqual(validate_teamkey(12345), False, "Should be False")
        self.assertEqual(validate_teamkey(51234), False, "Should be False")
        self.assertEqual(validate_teamkey('a1234'), False, "Should be False")
        self.assertEqual(validate_teamkey('1234'), True, "Should be True")
        self.assertEqual(validate_teamkey('12345'), False, "Should be False")
        self.assertEqual(validate_teamkey('test123'), False, "Should be False")
        self.assertEqual(validate_teamkey('te'), False, "Should be False")
        self.assertEqual(validate_teamkey(''), False, "Should be False")
        self.assertEqual(validate_teamkey(0), False, "Should be False")
        self.assertEqual(validate_teamkey('3710'), True, "Should be True")
        self.assertEqual(validate_teamkey(3710), True, "Should be True")
