from django.conf import settings
import tbaapiv3client
import requests
import json
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

#TODO : Get a request to FRC Events API Working
def testRequest():
    url = 'https://frc-staging-api.firstinspires.org/v2.0/2017/teams'
    key = ''
    headers = {'Authorization' : key}
    response = requests.get(url, headers=headers)
    print(response)
