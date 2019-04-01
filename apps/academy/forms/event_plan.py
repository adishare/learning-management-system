from django.forms import ModelForm
from django import  forms
from academy.models.event_plan import EventPlan
from academy.models.academy import Academy
from django.forms.widgets import Select
from django.forms.widgets import CheckboxInput


class EventPlanForm(ModelForm):
    class Meta:
        model = EventPlan
        exclude = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

