# tests/test_jwt.py
from accounts.views import SignupView, LoginView
from accounts.models import User
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
def test_signup_and_token_issue():
    client = APIClient()
    response = client.post('/api/accounts/signup/', {
        "username": "JIN HO2",
        "password": "12341234",
        "nickname": "Mentos4"
    })
    assert response.status_code == 201

@pytest.mark.django_db
def test_login_and_token_issue():
    client = APIClient()
    client.post('/api/accounts/signup/', {
        "username": "JIN HO2",
        "password": "12341234",
        "nickname": "Mentos4"
    })
    response = client.post('/api/accounts/login/', {
        "username": "JIN HO2",
        "password": "12341234"
    })
    assert response.status_code == 200
