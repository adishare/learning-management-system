from django_undeletable.models import BaseModel
from django.utils import timezone
from django.db import models

class Forum(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField('account.User', blank=True)
    competency = models.ManyToManyField('competency.Competency', blank=True)
    proficiency = models.ManyToManyField('competency.Proficiency', blank=True)

    def __str__(self):
        return self.name
