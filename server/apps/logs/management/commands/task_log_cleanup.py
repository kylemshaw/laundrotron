from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Deletes logs that are older than a predefined date to prevent the database from growing too large."

    def handle(self, *args, **options):
        self.delete_old_logs()

    def delete_old_logs(self):
        # TODO
        pass