from django_undeletable.models import BaseModel
from django.db import models

class Vendor(BaseModel):
	company = models.ForeignKey("location.Company", on_delete=models.CASCADE)
	code = models.CharField(max_length=225)	
	name = models.CharField(max_length=225)	
	
	def __str__(self):
		return self.name