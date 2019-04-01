from django_undeletable.models import BaseModel
from django.db import models

class EventPlan(BaseModel):

    learning_plan = models.ForeignKey("academy.LearningPlan", on_delete=models.CASCADE)
    curriculum_title = models.ForeignKey("competency.Curriculum", on_delete=models.CASCADE)
    mentor_request = models.CharField(max_length=150)
    vendor_request = models.CharField(max_length=150)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
      return str(self.id)
