from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from authentication.enums import Groups


class Command(BaseCommand):
    def handle(self, *args, **options):
        Group.objects.get_or_create(name=Groups.TENANT.name)
        Group.objects.get_or_create(name=Groups.LANDLORD.name)

        self.stdout.write('Groups added to database')
