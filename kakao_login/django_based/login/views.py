# Create your views here.
from django.http import JsonResponse, HttpResponseRedirect

from dotenv import load_dotenv

import os
import json
import requests

load_dotenv()

CLIENT_ID = os.environ.get('REST_API_KEY')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

def main(request):
    if request.method == "GET":
        url = f'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
        return HttpResponseRedirect(redirect_to=url)

def get_token_info(request):
    code = request.GET.get('code')
    res = requests.post('https://kauth.kakao.com/oauth/token',
                        headers={"Content-type": "application/x-www-form-urlencoded;charset=utf-8"},
                        data=
                        {
                            "grant_type":"authorization_code",
                            "client_id":CLIENT_ID,
                            "redirect_uri":REDIRECT_URI,
                            "code":code
                        }).content.decode()

    res = json.loads(res)

    os.environ["ACCESS_TOKEN"] = res["access_token"]
    os.environ["EXPIRES_IN"] = str(res["expires_in"])
    os.environ["REFRESH_TOKEN"] = res["refresh_token"]
    os.environ["REFRESH_TOKEN_EXPIRES_IN"] = str(res["refresh_token_expires_in"])

    return JsonResponse({"message": "Success"})