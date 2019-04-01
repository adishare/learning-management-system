from django_undeletable.models import BaseModel
from django.db import models

class ContentCreator(BaseModel):
	event = models.CharField(max_length=150)
	academy = models.ForeignKey('academy.Academy', on_delete=models.CASCADE)
	start = models.DateField()
	end = models.DateField()
	type = models.CharField(max_length=150)
	learning_activity = models.CharField(max_length=225)
	resource = models.CharField(max_length=150)
	status = models.CharField(max_length=150)
	class_type = models.CharField(max_length=150)
	
	def __str__(self):
		return self.event
