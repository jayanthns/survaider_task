from django.core.management.base import BaseCommand, CommandError

from myapp.add_data import add_data


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print("LOADING...")
        add_data()
        print("LOADING DATA DONE.")
