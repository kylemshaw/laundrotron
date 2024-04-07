from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = "Load default data into the database for development purposes."

    def handle(self, *args, **options):
        self.create_superuser()

    def create_locations(self):
        pass