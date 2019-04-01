import requests
from django.conf import settings

def login():
    login_url = settings.HCIS_API_URL + "/api/auth"
    login_data = {
        "username": settings.HCIS_API_USERNAME,
        "password": settings.HCIS_API_PASSWORD,
    }
    login_resp = requests.post(login_url, json=login_data)
    token = login_resp.json().get('data')
    return token

