from django.urls import path
from academy.views import participant_event

urlpatterns = [
    path('', participant_event.index, name="academy-participant-event-index"),
    path('add/', participant_event.add, name="academy-participant-event-add"),
    path('<id>/edit/', participant_event.edit, name="academy-participant-event-edit"),
    path('<id>/delete/', participant_event.delete, name="academy-participant-event-delete"),
]
