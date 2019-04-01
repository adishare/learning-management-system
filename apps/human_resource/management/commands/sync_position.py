import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from human_resource.models.position import Position
from location.models.company import Company
from hcis_utils import login

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        token = login()
        
        city_url = settings.HCIS_API_URL + "/api/users/otype/JOBRL/object"
        headers = {'Authorization': token}
        city_resp = requests.get(city_url, headers=headers)
        company = Company.objects.get(code='1000')
        for position in city_resp.json()['data']:
            Position.objects.get_or_create(company = company, 
                                       code=position['object_code'], 
                                       title=position['object_name'])
