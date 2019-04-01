from django.db import models
from django.forms.models import ModelForm
from academy.models.academy import Academy
from academy.models.participant_event import ParticipantEvent
from django.forms.widgets import CheckboxSelectMultiple

class ParticipantEventForm(ModelForm):
    
    class Meta:
        model = ParticipantEvent
        exclude = []
             
    def __init__(self, *args, **kwargs):
        
        super(ParticipantEventForm, self).__init__(*args, **kwargs)
        
