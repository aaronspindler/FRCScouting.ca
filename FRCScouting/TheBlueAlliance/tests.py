from django.test import TestCase
from . import validators, getters

class UtilsTestCase(TestCase):
    def test_validate_teamkey(self):
        self.assertEqual(validators.validate_teamkey(123), True, "Should be True")
        self.assertEqual(validators.validate_teamkey(1), True, "Should be True")
        self.assertEqual(validators.validate_teamkey(12), True, "Should be True")
        self.assertEqual(validators.validate_teamkey(1234), True, "Should be True")
        self.assertEqual(validators.validate_teamkey(12345), False, "Should be False")
        self.assertEqual(validators.validate_teamkey(51234), False, "Should be False")
        self.assertEqual(validators.validate_teamkey('a1234'), False, "Should be False")
        self.assertEqual(validators.validate_teamkey('1234'), True, "Should be True")
        self.assertEqual(validators.validate_teamkey('12345'), False, "Should be False")
        self.assertEqual(validators.validate_teamkey('test123'), False, "Should be False")
        self.assertEqual(validators.validate_teamkey('te'), False, "Should be False")
        self.assertEqual(validators.validate_teamkey(''), False, "Should be False")
        self.assertEqual(validators.validate_teamkey(0), False, "Should be False")
        self.assertEqual(validators.validate_teamkey('3710'), True, "Should be True")
        self.assertEqual(validators.validate_teamkey(3710), True, "Should be True")

    def test_get_team_info(self):
        #Should be successful
        team3710 = getters.get_team_info(3710)
        self.assertEqual(team3710.number, 3710, "Should be 3710")
        self.assertEqual(team3710.nickname, 'FSS Cyber Falcons', "Should be FSS Cyber Falcons")
        self.assertEqual(team3710.website, 'http://www.cyberfalcons.com', "Should be http://www.cyberfalcons.com")
        self.assertEqual(team3710.rookieyear, 2011, "Should be 2011")

        #Should 404
        team2 = getters.get_team_info(2)
        self.assertEqual(team2, None, "Should be None")

        def test_get_event_info(self):
            self.assertEqual(True, True)
