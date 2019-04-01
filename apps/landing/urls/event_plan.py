from django.urls import path
from landing.views import event_plan

urlpatterns = [
    path('', event_plan.index, name="landing-event-plan-index"),
]