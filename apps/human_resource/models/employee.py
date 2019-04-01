from django_undeletable.models import BaseModel
from django.db import models

class Employee(BaseModel):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
    company = models.ForeignKey('location.Company', on_delete=models.CASCADE)
    location = models.ForeignKey("location.Location", on_delete=models.CASCADE)
    division = models.ForeignKey("human_resource.Division", on_delete=models.CASCADE)
    position = models.ForeignKey("human_resource.Position", on_delete=models.CASCADE)
    ic_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=255)
    grade = models.ForeignKey("human_resource.EmployeeGrade", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


