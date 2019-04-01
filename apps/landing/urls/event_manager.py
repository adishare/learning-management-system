from django.urls import path
from landing.views import event_manager

urlpatterns = [
    path('', event_manager.index, name="landing-event-manager-index"),
]