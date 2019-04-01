from django_undeletable.models import BaseModel
from django.db import models

class Trainer(BaseModel):
	TRAINER_TYPE = (
		('N', "Normal Trainer"),
	)
	
	company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
	vendor = models.ForeignKey('academy.Vendor', on_delete=models.CASCADE)	
	ic_number = models.CharField(max_length=50)	
	type = models.CharField(max_length=2, choices=TRAINER_TYPE)	
	name = models.CharField(max_length=50)	
	
	def __str__(self):
		return self.name