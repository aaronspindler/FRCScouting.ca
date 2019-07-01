from django.conf import settings
import tbaapiv3client
from tbaapiv3client.rest import ApiException

def get_status():
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.TBAApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_status()
        info = api_response
        return info
    except ApiException as e:
        return None

def get_team(teamkey):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_team("frc" + str(teamkey))
        info = api_response
        return info
    except ApiException as e:
        return None

def get_event(eventkey):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_event(eventkey)
        info = api_response
        return info
    except ApiException as e:
        return None

# Currently is buggy because of backend API bug
# See: https://github.com/the-blue-alliance/the-blue-alliance/pull/2543
def get_events_by_year(year):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_events_by_year(year)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_events_by_year_keys(year):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.EventApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_events_by_year_keys(year)
        info = api_response
        return info
    except ApiException as e:
        return None
