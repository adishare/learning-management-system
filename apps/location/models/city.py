from django_undeletable.models import BaseModel
from django.db import models

class City(BaseModel):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    company = models.ForeignKey('location.Company', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
