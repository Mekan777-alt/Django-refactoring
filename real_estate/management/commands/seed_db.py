from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand



class Command(BaseCommand):
    def handle(self, *args, **options):
        Group.objects.create(name='TENANT')
        Group.objects.create(name='LANDLORD')
