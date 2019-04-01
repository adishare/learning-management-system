from django_undeletable.models import BaseModel
from django.db import models

class Partner(BaseModel):
    PARTNER_TYPE = (
        ('T', "Trainer"),
        ('V', "Vendor"),
    )

    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    code = models.CharField(max_length = 225)
    name = models.CharField(max_length = 225)
    type = models.CharField(max_length = 225, choices=PARTNER_TYPE)

    def __str__(self):
        return self.name