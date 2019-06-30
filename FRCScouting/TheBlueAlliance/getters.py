from django.conf import settings
from .models import Team, Event
import requests

def get_team_info(teamkey):
    url = 'https://www.thebluealliance.com/api/v3/team/frc{}'.format(teamkey)
    headers = {'X-TBA-Auth-Key': settings.THE_BLUE_ALLIANCE_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        teaminfo = Team()

        teaminfo.number = result['team_number']
        teaminfo.key = result['key']
        teaminfo.nickname = result['nickname']
        teaminfo.name = result['name']
        teaminfo.city = result['city']
        teaminfo.state_prov = result['state_prov']
        teaminfo.country = result['country']
        teaminfo.address = result['address']
        teaminfo.postalcode = result['postal_code']
        teaminfo.website = result['website']
        teaminfo.rookieyear = result['rookie_year']
        teaminfo.motto = result['motto']
        teaminfo.save()
        return teaminfo
    elif response.status_code == 404:
        return None

#TODO
def get_event_info(eventkey):
    url = 'https://www.thebluealliance.com/api/v3/event/{}'.format(eventkey)
    headers = {'X-TBA-Auth-Key': settings.THE_BLUE_ALLIANCE_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        eventinfo = Event()
        eventinfo.address = result['address']
        eventinfo.city = result['city']
        eventinfo.country = result['country']
        eventinfo.district = result['district']
        eventinfo.division_keys = result['division_keys']
        eventinfo.end_date = result['end_date']
        eventinfo.event_code = result['event_code']
        eventinfo.event_type = result['event_type']
        eventinfo.event_type_string = result['event_type_string']
        eventinfo.first_event_code = result['first_event_code']
        eventinfo.first_event_id = result['first_event_id']
        eventinfo.gmaps_place_id = result['gmaps_place_id']
        eventinfo.gmaps_url = result['gmaps_url']
        eventinfo.key = result['key']
        eventinfo.lat = result['lat']
        eventinfo.lng = result['lng']
        eventinfo.location_name = result['location_name']
        eventinfo.name = result['name']
        eventinfo.parent_event_key = result['parent_event_key']
        eventinfo.playoff_type = result['playoff_type']
        eventinfo.playoff_type_string = result['playoff_type_string']
        eventinfo.postal_code = result['postal_code']
        eventinfo.short_name = result['short_name']
        eventinfo.start_date = result['start_date']
        eventinfo.state_prov = result['state_prov']
        eventinfo.timezone = result['timezone']
        eventinfo.webcasts = result['webcasts']
        eventinfo.website = result['website']
        eventinfo.week = result['week']
        eventinfo.year = result['year']
        eventinfo.save()

        return eventinfo
    elif response.status_code == 404:
        return None

#TODO
def get_events_for_year(year):
    url = 'https://www.thebluealliance.com/api/v3/events/{}'.format(year)
    headers = {'X-TBA-Auth-Key': settings.THE_BLUE_ALLIANCE_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        events = {}
        for event in result:
            eventinfo = Event()
            eventinfo.address = event['address']
            eventinfo.city = event['city']
            eventinfo.country = event['country']
            eventinfo.district = event['district']
            eventinfo.division_keys = event['division_keys']
            eventinfo.end_date = event['end_date']
            eventinfo.event_code = event['event_code']
            eventinfo.event_type = event['event_type']
            eventinfo.event_type_string = event['event_type_string']
            eventinfo.first_event_code = event['first_event_code']
            eventinfo.first_event_id = event['first_event_id']
            eventinfo.gmaps_place_id = event['gmaps_place_id']
            eventinfo.gmaps_url = event['gmaps_url']
            eventinfo.key = event['key']
            eventinfo.lat = event['lat']
            eventinfo.lng = event['lng']
            eventinfo.location_name = event['location_name']
            eventinfo.name = event['name']
            eventinfo.parent_event_key = event['parent_event_key']
            eventinfo.playoff_type = event['playoff_type']
            eventinfo.playoff_type_string = event['playoff_type_string']
            eventinfo.postal_code = event['postal_code']
            eventinfo.short_name = event['short_name']
            eventinfo.start_date = event['start_date']
            eventinfo.state_prov = event['state_prov']
            eventinfo.timezone = event['timezone']

            #TODO: Webcasts

            eventinfo.website = event['website']
            eventinfo.week = event['week']
            eventinfo.year = event['year']

            events[eventinfo.key] = eventinfo

            eventinfo.save()

        return events

    elif response.status_code == 404:
        return None
