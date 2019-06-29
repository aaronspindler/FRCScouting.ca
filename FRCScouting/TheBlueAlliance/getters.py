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

#TODO :
def get_event_info(eventkey):
    url = 'https://www.thebluealliance.com/api/v3/event/{}'.format(year)
    headers = {'X-TBA-Auth-Key': settings.THE_BLUE_ALLIANCE_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        eventinfo = Event()
    return None

#TODO :
def get_events_for_year(year):
    return None
