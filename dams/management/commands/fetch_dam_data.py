# dams/management/commands/fetch_dam_data.py
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from dams.models import Dam, DamStatistics
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetches dam data from KSEB website and updates the database.'

    def handle(self, *args, **kwargs):
        url = 'https://dams.kseb.in/?p=4703'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Print out the first 500 characters of the page to see the structure
        print(soup.prettify()[:500])

        # Assuming the data is in a table format; you will need to adjust this based on the actual HTML structure.
        table = soup.find('table')
        if not table:
            self.stdout.write(self.style.ERROR('No table found on the page.'))
            return

        rows = table.find_all('tr')

        for row in rows[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) < 7:
                continue  # Skip rows that do not have enough columns

            dam_name = cols[0].text.strip()
            district = cols[1].text.strip()
            date_raw = cols[2].text.strip()
            print(f"Raw date data: {date_raw}")  # Print raw date data for inspection

            # Adjust date parsing according to the observed format
            try:
                date = datetime.strptime(date_raw, '%d-%m-%Y').date()
            except ValueError as e:
                print(f"Date parsing error: {e}")  # Print error if parsing fails
                continue

            try:
                rainfall = float(cols[3].text.strip())
                inflow = float(cols[4].text.strip())
                power_house_discharge = float(cols[5].text.strip())
                spillway_release = float(cols[6].text.strip())
            except ValueError as e:
                print(f"Value parsing error: {e}")  # Print error if value parsing fails
                continue

            dam, created = Dam.objects.get_or_create(name=dam_name, district=district)
            DamStatistics.objects.update_or_create(
                dam=dam, date=date,
                defaults={
                    'rainfall': rainfall,
                    'inflow': inflow,
                    'power_house_discharge': power_house_discharge,
                    'spillway_release': spillway_release
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and updated dam data.'))
