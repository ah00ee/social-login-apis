from django.urls import path

from . import views

urlpatterns = [
    path('', views.main),  #127.0.0.1:8000/
    path('oauth/kakao/login/', views.get_token_info)
]
