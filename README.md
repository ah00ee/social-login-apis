# 소셜 로그인 API 연동

## Framework
- FastAPI

## 1. 카카오 로그인
### .env 환경변수 설정
* (잘못 설정할 경우 error 발생)
```
REST_API_KEY={'Your REST API key'}
REDIRECT_URI={'Redirect URI'}
```
### Run
```
uvicorn kakao_login.fastapi.app:app --reload
```

## 2. 네이버 로그인
### .env 환경변수 설정
* (잘못 설정할 경우 error 발생)
```
REST_API_KEY={'Your REST API key'}
CALLBACK_URL={'Your CALLBACK URL'}
CLIENT_SECRET={'Your Client Secret Key'}
```
### Run
```
uvicorn naver_login.fastapi.app:app --reload
```