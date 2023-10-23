# 소셜 로그인 API 연동 (Python)

## 1. Set up environment
-  requirements.txt
```
pip install -r requirements.txt
```

### 1.1 카카오 로그인
- **.env** 환경변수 설정 (잘못 설정할 경우 error 발생)
```
REST_API_KEY={'Your REST API key'} #Client ID
REDIRECT_URI={'Redirect URI'}
```
### 1.2 네이버 로그인
- **.env** 환경변수 설정 (잘못 설정할 경우 error 발생)
```
REST_API_KEY={'Your REST API key'}
CALLBACK_URL={'Your CALLBACK URL'}
CLIENT_SECRET={'Your Client Secret Key'}
```

## 2. Framework
### 2.1 FastAPI
- **Run** @(root folder)
```
# Kakao 카카오 로그인
uvicorn kakao_login.fastapi.app:app --reload

# Naver 네이버 로그인
uvicorn naver_login.fastapi.app:app --reload
```

### 2.2 Django
- **Run** @(where manage.py is located)
```
python manage.py runserver
```