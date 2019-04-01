from django_undeletable.models import BaseModel
from django.db import models

class Location(BaseModel):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=225)
    city = models.ForeignKey('location.City', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey('location.Company', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
