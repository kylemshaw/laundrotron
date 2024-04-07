from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    help = "Load default data into the database for development purposes."

    def handle(self, *args, **options):
        self.create_superuser()

    def create_superuser(self):
        from django.contrib.auth.models import User
        User.objects.create_superuser(
            first_name="Admin",
            username="Admin",
            email="admin@laundrotron.com",
            password="admin",
        )