from django_undeletable.models import BaseModel
from django.db import models

class Building(BaseModel):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    city = models.ForeignKey('location.City', on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)
    address = models.CharField(max_length=225)
    company = models.ForeignKey('location.Company', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
