from django.core.management.base import BaseCommand
from dams.models import Dam, DamStatistics
from scripts.scrape_data import populate_database

class Command(BaseCommand):
    help = 'Populate the database with dam data'

    def handle(self, *args, **kwargs):
        populate_database()
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
