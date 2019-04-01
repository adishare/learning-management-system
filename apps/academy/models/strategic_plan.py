from django_undeletable.models import BaseModel
from django.db import models

class StrategicPlanField(models.Model):
    name = models.CharField(max_length=255, unique=True)
    required = models.BooleanField(default=True)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class StrategicPlanIssue(models.Model):
    strategic_plan = models.ForeignKey("academy.StrategicPlan", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.name

class StrategicPlan(BaseModel):
    strategic_initiative = models.CharField(max_length=255)
    
    def __str__(self):
        return self.strategic_initiative

    @property
    def strategicplanissue(self):
        data = []
        for issue in StrategicPlanField.objects.exclude(name="Strategic Initiative"):
            try:
                iss = StrategicPlanIssue.objects.get(strategic_plan=self,name=issue.name.lower().replace(" ", "_") )
                data.append(iss)
            except:
                data.append(False)
        print(data)
        return data



