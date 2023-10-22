# Create your views here.
from django.http import JsonResponse, HttpResponseRedirect

from dotenv import load_dotenv

import os
import json
import requests

load_dotenv()

CLIENT_ID = os.environ.get('REST_API_KEY')
REDIRECT_URI = os.environ.get('CALLBACK_URL')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
STATE_STRING = 'TEST'

def main(request):
    if request.method == "GET":
        url = f'https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={CLIENT_ID}&state={STATE_STRING}&redirect_uri={REDIRECT_URI}'
        return HttpResponseRedirect(redirect_to=url)

def get_token_info(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    res = requests.post('https://nid.naver.com/oauth2.0/token',
                        data=
                        {
                            "grant_type":"authorization_code",
                            "client_id":CLIENT_ID,
                            "client_secret":CLIENT_SECRET,
                            "code":code,
                            "state":state
                        }).content.decode()

    res = json.loads(res)

    os.environ["ACCESS_TOKEN"] = res["access_token"]
    os.environ["REFRESH_TOKEN"] = res["refresh_token"]
    os.environ["TOKEN_TYPE"] = res["token_type"]
    os.environ["EXPIRES_IN"] = str(res["expires_in"])

    return JsonResponse({"message": "Success"})