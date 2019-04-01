from django_undeletable.models import BaseModel
from django.db import models

class EmployeeGrade(BaseModel):
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


