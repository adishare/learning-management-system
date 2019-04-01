import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from academy.models.academy import Academy
from hcis_utils import login
from location.models.company import Company

class Command(BaseCommand):
    
   
    def handle(self, *args, **options):
        token = login()
        
        academy_url = settings.HCIS_API_URL + "/api/users/otype/EDUBR/object"
        headers = {'Authorization': token}
        academy_resp = requests.get(academy_url, headers=headers)
        for academy in academy_resp.json()['data']:
            Academy.objects.get_or_create(company = Company.objects.get(code = '1000'), 
                                       code=academy['object_code'], 
                                       name=academy['object_name'])
