from django_undeletable.models import BaseModel
from django.db import models

class Proficiency(BaseModel):
    LEVEL = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
    )
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=LEVEL, blank=True, null=True)
    
    def __str__(self):
        return self.level
