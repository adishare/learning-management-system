import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from competency.models.competency import Competency
from hcis_utils import login
from location.models.company import Company

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        token = login()
        
        competency_url = settings.HCIS_API_URL + "/api/users/otype/CMPTY/object"
        headers = {'Authorization': token}
        competency_resp = requests.get(competency_url, headers=headers)
        for competency in competency_resp.json()['data']:
            Competency.objects.get_or_create(company = Company.objects.get(code = '1000'), 
                                       		title = competency['object_name'])
