from django_undeletable.models import BaseModel
from django.db import models

class Notification(BaseModel):
	title = models.CharField(max_length=255)
	type = models.CharField(max_length=255)
	message = models.TextField()
	sender = models.ForeignKey('account.User', on_delete=models.CASCADE)
	receiver = models.CharField(max_length=255)
	time = models.TimeField(auto_now=True)
	read = models.BooleanField(default=False)
	url = models.URLField(max_length=200)

	def __str__(self):
		return self.title