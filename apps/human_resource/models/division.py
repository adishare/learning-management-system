from django_undeletable.models import BaseModel
from django.db import models

class Division(BaseModel):
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return "%s of %s" % (self.name, self.company)
