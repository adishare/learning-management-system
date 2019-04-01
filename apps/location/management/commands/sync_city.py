import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from location.models.city import City
from hcis_utils import login
from location.models.company import Company

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        token = login()
        
        city_url = settings.HCIS_API_URL + "/api/city/getall"
        headers = {'Authorization': token}
        city_resp = requests.get(city_url, headers=headers)
        for city in city_resp.json()['data']:
            City.objects.get_or_create(company = Company.objects.get(code = '1000'), 
                                       code=city['id'], 
                                       name=city['name'])
