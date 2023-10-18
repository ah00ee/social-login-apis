from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from dotenv import load_dotenv

import os

app = FastAPI()

load_dotenv()

CLIENT_ID = os.environ.get('REST_API_KEY')
REDIRECT_URI = os.environ.get('REDIRECT_URI')

@app.get('/')
async def main():   
    url = f'https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
    return RedirectResponse(url=url)

@app.get('/oauth/kakao/login')
async def get_token_info(code: str=""):

    return {"message": "Success"}