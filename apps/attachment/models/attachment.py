from django_undeletable.models import BaseModel
from django.db import models

class Attachment(models.Model):
	CYCLE_CHOICE = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
		(6, 6),
	)

	begin_date = models.DateField()
	end_date = models.DateField()
	name = models.CharField(max_length=255)
	cycle = models.IntegerField(choices=CYCLE_CHOICE)
	format = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	file = models.FileField()
	content_type = models.IntegerField()
	objid = models.CharField(max_length=255)

	def __str__(self):
		return self.name