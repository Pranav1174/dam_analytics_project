import requests
from django.core.management.base import BaseCommand
from dams.models import Dam, DamStatistics

class Command(BaseCommand):
    help = 'Import dam statistics data'

    def handle(self, *args, **kwargs):
        url = 'https://dams.kseb.in/api/your_endpoint'  # Replace with the actual API endpoint
        response = requests.get(url)
        
        # Print response status code and content for debugging
        self.stdout.write(self.style.SUCCESS(f'Status Code: {response.status_code}'))
        self.stdout.write(self.style.SUCCESS(f'Response Content: {response.text}'))
        
        if response.status_code == 200:
            try:
                data = response.json()
                for item in data:
                    dam, created = Dam.objects.get_or_create(name=item['Dam Name'], district=item['District'])
                    DamStatistics.objects.create(
                        dam=dam,
                        date=item['Date'],
                        rainfall=item['Rainfall'],
                        inflow=item['Inflow'],
                        power_house_discharge=item['Power House Discharge'],
                        spillway_release=item['Spillway Release']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully imported dam statistics data.'))
            except ValueError as e:
                self.stderr.write(f"JSON Decode Error: {e}")
        else:
            self.stderr.write(f"Failed to retrieve data. Status code: {response.status_code}")

