from django.conf import settings
import base64

def get_API_key():
    rawkey = '{}:{}'.format(settings.FMS_API_USER, settings.FMS_API_KEY)
    return base64.b64encode(rawkey.encode())
