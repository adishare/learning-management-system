from django_undeletable.models import BaseModel
from django.db import models

class Company(BaseModel):
    COMPANY_TYPE = (
        ('P', "Partner"),
        ('N', "Non Parner"),
    )

    code = models.CharField(max_length=20, unique=True, db_index=True)
    company_name = models.CharField(max_length=255)
    type = models.CharField(max_length = 225, choices=COMPANY_TYPE)
    
    def __str__(self):
        return self.company_name
