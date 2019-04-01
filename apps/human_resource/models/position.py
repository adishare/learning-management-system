from django_undeletable.models import BaseModel
from django.db import models

class Position(BaseModel):
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


