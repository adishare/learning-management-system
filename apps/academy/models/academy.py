from django_undeletable.models import BaseModel
from django.db import models

class Academy(BaseModel):
	company = models.ForeignKey("location.Company", on_delete=models.CASCADE)
	code = models.CharField(max_length=225)	
	name = models.CharField(max_length=225)
	division = models.ManyToManyField('human_resource.Division')

	def __str__(self):
		return self.name