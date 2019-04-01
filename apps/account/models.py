from django.contrib.auth.models import AbstractUser,Group
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey('location.Company',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    role = models.ManyToManyField('account.Role')
    active_role = models.ForeignKey('account.Role',
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name='active_user')

    def __unicode__(self):
        return self.full_name
        
    def __str__(self):
        return self.__unicode__()
    
    def set_active_role(self, role_code):
        role = Role.objects.get(code=role_code)
        self.active_role = role
        self.save()
    
class Role(models.Model):
    company = models.ForeignKey('location.Company',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    code = models.CharField(max_length=255, blank=True)
    landing_url_name = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.name