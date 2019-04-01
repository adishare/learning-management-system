from django_undeletable.models import BaseModel
from django.db import models

class EmployeeCompetency(BaseModel):
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    employee = models.ForeignKey('human_resource.Employee', on_delete=models.CASCADE)
    competency = models.ForeignKey('competency.Competency', on_delete=models.CASCADE)
    proficiency = models.ForeignKey('competency.Proficiency', on_delete=models.CASCADE)
   
    def __str__(self):
        return self.competency.title
