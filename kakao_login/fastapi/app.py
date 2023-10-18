from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from dotenv import load_dotenv

import os
import json
import requests

app = FastAPI()

load_dotenv()

CLIENT_ID = os.environ.get('REST_API_KEY')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

@app.get('/')
async def main():   
    url = f'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
    return RedirectResponse(url=url)

@app.get('/oauth/kakao/login')
async def get_token_info(code: str):
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

    return {"message": "Success"}