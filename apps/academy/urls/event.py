from django.urls import path
from academy.views import event

urlpatterns = [
    path('add/', event.add, name="academy-event-add"),
    path('<id>/edit/', event.edit, name="academy-event-edit"),
    path('<id>/delete/', event.delete, name="academy-event-delete"),
    path('<id>/set-on-going/', event.set_on_going, name="academy-event-set-on-going"),
    path('<id>/set-finish/', event.set_finish, name="academy-event-set-finish"),
]