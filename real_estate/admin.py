from django.contrib import admin
from real_estate.models import RealEstateObject

# Register your models here.


@admin.register(RealEstateObject)
class RealEstateObjectAdmin(admin.ModelAdmin):
    pass
