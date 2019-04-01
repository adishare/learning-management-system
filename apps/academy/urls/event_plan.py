from django.urls import path
from academy.views import event_plan

urlpatterns = [
    path('add/', event_plan.add, name="academy-event-plan-add"),
    path('<id>/edit/', event_plan.edit, name="academy-event-plan-edit"),
    path('<id>/delete/', event_plan.delete, name="academy-event-plan-delete"),
]