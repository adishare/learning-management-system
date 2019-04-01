from django_undeletable.models import BaseModel
from django.db import models

class Competency(BaseModel):
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
