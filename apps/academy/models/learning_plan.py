from django_undeletable.models import BaseModel
from django.db import models


class LearningPlan(BaseModel):
    title = models.CharField(max_length=255)
    location = models.ForeignKey("location.Location", on_delete=models.CASCADE)
    date = models.DateField()
    budget = models.IntegerField()
    competency_issue = models.ForeignKey("academy.StrategicPlan", on_delete=models.CASCADE)
    participant = models.IntegerField()
    batch = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title