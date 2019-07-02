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
