from django.test import TestCase
from . import validators, getters
from datetime import date

class ValidatorsTestCase(TestCase):
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

class GettersTestCase(TestCase):
    def test_get_team(self):
        #Should be successful
        team3710 = getters.get_team(3710)
        self.assertEqual(team3710.team_number, 3710, "Should be 3710")
        self.assertEqual(team3710.nickname, 'FSS Cyber Falcons', "Should be FSS Cyber Falcons")
        self.assertEqual(team3710.website, 'http://www.cyberfalcons.com', "Should be http://www.cyberfalcons.com")
        self.assertEqual(team3710.rookie_year, 2011, "Should be 2011")

        #Should 404
        team2 = getters.get_team(2)
        self.assertEqual(team2, None, "Should be None")

    def test_get_event(self):
        #Should be successful
        event2019abca = getters.get_event('2019abca')
        self.assertEqual(event2019abca.address, "7555 Falconridge Blvd NE #10, Calgary, AB T3J 0C9, Canada")
        self.assertEqual(event2019abca.city, "Calgary")
        self.assertEqual(event2019abca.country, "Canada")
        self.assertEqual(event2019abca.district, None)
        self.assertEqual(event2019abca.division_keys, [])
        self.assertEqual(event2019abca.end_date, date(2019,4,6))
        self.assertEqual(event2019abca.event_code, "abca")
        self.assertEqual(event2019abca.event_type, 0)
        self.assertEqual(event2019abca.event_type_string, "Regional")
        self.assertEqual(event2019abca.first_event_code, "ABCA")
        self.assertEqual(event2019abca.first_event_id, None)
        self.assertEqual(event2019abca.gmaps_place_id, "ChIJWxy6PJljcVMRpVrD88vyEdY")
        self.assertEqual(event2019abca.gmaps_url, "https://maps.google.com/?cid=15425377156502608549")
        self.assertEqual(event2019abca.key, "2019abca")
        self.assertEqual(event2019abca.lat, 51.1202633)
        self.assertEqual(event2019abca.lng, -113.9486288)
        self.assertEqual(event2019abca.location_name, "The Genesis Centre")
        self.assertEqual(event2019abca.name, "Canadian Rockies Regional")
        self.assertEqual(event2019abca.parent_event_key, None)
        self.assertEqual(event2019abca.playoff_type, None)
        self.assertEqual(event2019abca.playoff_type_string, None)
        self.assertEqual(event2019abca.postal_code, "T3J 0C9")
        self.assertEqual(event2019abca.short_name, "Canadian Rockies")
        self.assertEqual(event2019abca.start_date, date(2019,4,3))
        self.assertEqual(event2019abca.state_prov, "AB")
        self.assertEqual(event2019abca.timezone, "America/Edmonton")

        #TODO webcasts

        self.assertEqual(event2019abca.website, "http://frcwest.com/")
        self.assertEqual(event2019abca.week, 5)
        self.assertEqual(event2019abca.year, 2019)

        #Should 404
        event2000abcd = getters.get_event('2000abcd')
        self.assertEqual(event2000abcd, None, 'Should be None')

    def test_get_events_by_year(self):
        #Currently does not work because of a bug in API
        #See: https://github.com/TBA-API/tba-api-client-python/pull/3

        # events2019 = getters.get_events_by_year(2019)
        # self.assertEqual(len(events2019),242, 'Should be 242')

        events1950 = getters.get_events_by_year(1950)
        self.assertEqual(events1950, None, 'Should be None')
