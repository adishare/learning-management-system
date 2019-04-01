from django.urls import path
from landing.views import expert

urlpatterns = [
    path('', expert.index, name="landing-expert-index"),
]