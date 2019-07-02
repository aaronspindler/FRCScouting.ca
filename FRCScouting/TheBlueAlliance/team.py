from django.conf import settings
import tbaapiv3client
from tbaapiv3client.rest import ApiException

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

def get_teams(page_num):
    configuration = tbaapiv3client.Configuration()
    configuration.api_key['X-TBA-Auth-Key'] = settings.THE_BLUE_ALLIANCE_KEY
    api_instance = tbaapiv3client.TeamApi(tbaapiv3client.ApiClient(configuration))
    try:
        api_response = api_instance.get_teams(page_num)
        info = api_response
        return info
    except ApiException as e:
        return None

def get_all_teams_slow():
    teams = []
    for team_num in range(5000):
        try:
            team = get_team(team_num)
            teams.append(team)
        except Exception as e:
            continue
    return teams

def get_all_teams_by_page():
    teams = []
    for page in range(20):
        page_contents = get_teams(page)
        if page_contents:
            for team in page_contents:
                teams.append(team)
        else:
            break
    return teams
