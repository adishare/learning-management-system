from django_undeletable.models import BaseModel
from django.db import models

class Curriculum(BaseModel):
	CLAIM_TYPE = (
		('N', "Not Claimmed"),
		('C', "Claimmed"),
	)

	title = models.CharField(max_length=255)
	company = models.ForeignKey('location.Company', on_delete=models.CASCADE, blank=True, null=True)
	competency_goal = models.ForeignKey('competency.Competency', on_delete=models.CASCADE)
	issue = models.ForeignKey('academy.StrategicPlan', on_delete=models.CASCADE)
	learning_activity = models.ManyToManyField('academy.LearningActivity', blank=True, related_name='learning_activity')
	capacity = models.PositiveIntegerField()
	claim = models.CharField(max_length=2, choices=CLAIM_TYPE)	

	def __str__(self):
		return self.title