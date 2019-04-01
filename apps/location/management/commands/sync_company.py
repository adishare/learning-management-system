import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from location.models.company import Company
from hcis_utils import login

class Command(BaseCommand):
    
    
    def handle(self, *args, **options):
        token = login()
        
        company_url = settings.HCIS_API_URL + "/api/company"
        headers = {'Authorization': token}
        company_resp = requests.get(company_url, headers=headers)
        for company in company_resp.json()['data']:
            Company.objects.get_or_create(code=company['business_code'], 
                                       company_name=company['company_name'])
