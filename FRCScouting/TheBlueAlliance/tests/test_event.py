from django.test import TestCase
from datetime import date

from TheBlueAlliance.event import *

class EventTestCase(TestCase):
    def test_get_event(self):
        #Should be successful
        event2019abca = get_event('2019abca')
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
        event2000abcd = get_event('2000abcd')
        self.assertEqual(event2000abcd, None, 'Should be None')

    def test_get_events_by_year(self):
        #Currently does not work because of a bug in API
        #See: https://github.com/the-blue-alliance/the-blue-alliance/pull/2543

        # events2019 = getters.get_events_by_year(2019)
        # self.assertEqual(len(events2019),242, 'Should be 242')

        events1950 = get_events_by_year(1950)
        self.assertEqual(events1950, None, 'Should be None')

    def test_get_events_by_year_simple(self):
        #Should succeed
        events2018 = get_events_by_year_simple(2018)
        self.assertEqual(len(events2018),278, 'Should be 278')

        #Should 404
        events1950 = get_events_by_year_simple(1950)
        self.assertEqual(events1950, None, 'Should be None')

    def test_get_events_by_year_keys(self):
        #Should succeed
        events2019keys = get_events_by_year_keys(2019)
        self.assertEqual(len(events2019keys), 243, 'Should be 243')

        events2018keys = get_events_by_year_keys(2018)
        self.assertEqual(len(events2018keys), 278, 'Should be 278')

        events2017keys = get_events_by_year_keys(2017)
        self.assertEqual(len(events2017keys), 255, 'Should be 255')

        events2016keys = get_events_by_year_keys(2016)
        self.assertEqual(len(events2016keys), 203, 'Should be 203')

        #Should 404
        events1950keys = get_events_by_year_keys(1950)
        self.assertEqual(events1950keys, None, 'Should be None')

    def test_get_all_event_keys(self):
        allkeys = get_all_event_keys()
        self.assertEqual(len(allkeys), 4)
        self.assertEqual(len(allkeys[2016]), 203)
        self.assertEqual(len(allkeys[2017]), 255)
        self.assertEqual(len(allkeys[2018]), 278)
        self.assertEqual(len(allkeys[2019]), 243)

    def test_get_all_events_simple(self):
        allEvents = get_all_events_simple()
        self.assertEqual(len(allEvents), 4)
        self.assertEqual(len(allEvents[2016]), 203)
        self.assertEqual(len(allEvents[2017]), 255)
        self.assertEqual(len(allEvents[2018]), 278)
        self.assertEqual(len(allEvents[2019]), 243)

    def test_get_event_teams(self):
        iri2016_teams = get_event_teams("2016iri")
        self.assertEqual(len(iri2016_teams),69)

    def test_get_event_matches(self):
        iri2018_matches = get_event_matches('2018iri')
        self.assertEqual(len(iri2018_matches), 122)
