import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_dam_data():
    url = "https://dams.kseb.in/?p=4703"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data from the soup object
    data = []  # Collect data here

    return data

def populate_database():
    from dams.models import Dam, DamStatistics
    data = scrape_dam_data()
    for entry in data:
        dam, created = Dam.objects.get_or_create(name=entry['name'], district=entry['district'])
        DamStatistics.objects.create(
            dam=dam,
            date=datetime.strptime(entry['date'], '%Y-%m-%d').date(),
            rainfall=entry['rainfall'],
            inflow=entry['inflow'],
            power_house_discharge=entry['power_house_discharge'],
            spillway_release=entry['spillway_release'],
        )
