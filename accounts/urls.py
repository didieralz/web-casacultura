# accounts/urls.py
from django.urls import path

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),# http://127.0.0.1:8000/accounts/signup/
]