from django_undeletable.models import BaseModel
from django.db import models

class Workplace(BaseModel):
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    division = models.ForeignKey('human_resource.Division', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
