from django.urls import path, include
from .views import login_page, logout_page

urlpatterns = [
    path('login/', login_page, name="account-login"),
    path('logout/', logout_page, name="account-logout"),
]