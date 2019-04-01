import datetime
from django_undeletable.models import BaseModel
from django.db import models

YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class LearningFocus(BaseModel):
    unit_business = models.CharField(max_length=225)
    academy = models.ForeignKey('academy.Academy', on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    org_competence = models.CharField(max_length=225)
    objective = models.CharField(max_length=225)
    staff = models.CharField(max_length=225)
    supervisor = models.CharField(max_length=225)
    manager = models.CharField(max_length=225)
    senior_manager = models.CharField(max_length=225)
    top_management = models.CharField(max_length=225)

    def __str__(self):
        return self.unit_business
