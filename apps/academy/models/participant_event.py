from django_undeletable.models import BaseModel
from django.db import models

class ParticipantEvent(BaseModel):
    participant_name = models.ForeignKey('human_resource.Participant', 
                                        on_delete=models.CASCADE)
    event_name = models.ForeignKey('academy.Event', 
                                   on_delete=models.CASCADE)
    state =  models.BooleanField(default=False)
	
    def __str__(self):
        return str(self.id)
