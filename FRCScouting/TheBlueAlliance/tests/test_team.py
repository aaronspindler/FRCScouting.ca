from django.test import TestCase
from datetime import date

from TheBlueAlliance.team import *

class TeamTestCase(TestCase):
    def test_get_team(self):
        #Should be successful
        team3710 = get_team(3710)
        self.assertEqual(team3710.team_number, 3710, "Should be 3710")
        self.assertEqual(team3710.nickname, 'FSS Cyber Falcons', "Should be FSS Cyber Falcons")
        self.assertEqual(team3710.website, 'http://www.cyberfalcons.com', "Should be http://www.cyberfalcons.com")
        self.assertEqual(team3710.rookie_year, 2011, "Should be 2011")

        #Should 404
        team2 = get_team(2)
        self.assertEqual(team2, None, "Should be None")

    def test_get_team_events(self):
        team3710_events = get_team_events(3710)
        self.assertEqual(len(team3710_events), 10)
