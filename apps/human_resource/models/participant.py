from django_undeletable.models import BaseModel
from django.db import models

class Participant(BaseModel):
    nik = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


