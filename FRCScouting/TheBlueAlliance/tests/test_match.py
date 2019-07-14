from django.test import TestCase
from TheBlueAlliance.match import *

class EventTestCase(TestCase):
    def test_get_event(self):
        #Should be successful
        print("Testing TBA get_match")
        match_2017cc_f1m1 = get_match('2017cc_f1m1')
        self.assertEqual(match_2017cc_f1m1.key, '2017cc_f1m1')
        
        match_2019iri_f1m1 = get_match('2019iri_f1m1')
        print(match_2019iri_f1m1)
