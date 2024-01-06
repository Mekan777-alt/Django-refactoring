from django.contrib import admin

# Register your models here.
from django.contrib import admin

from real_estate.models import RealEstateObject


@admin.register(RealEstateObject)
class RealEstateObjectAdmin(admin.ModelAdmin):
    pass
