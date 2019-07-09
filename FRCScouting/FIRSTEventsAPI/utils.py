from django.conf import settings
import base64

def get_API_key():
    rawkey = '{}:{}'.format(settings.FMS_API_USER, settings.FMS_API_KEY)
    return base64.b64encode(rawkey.encode())

#TODO : Get a request to FRC Events API Working
def testRequest():
    url = 'https://frc-staging-api.firstinspires.org/v2.0/2017/teams'
    key = ''
    headers = {'Basic' : key}
    response = requests.get(url, headers=headers)
    print(response)
