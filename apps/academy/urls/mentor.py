from django.urls import path
from academy.views import mentor

urlpatterns = [
    path('view-detail/', mentor.view, name="view-detail"),
]