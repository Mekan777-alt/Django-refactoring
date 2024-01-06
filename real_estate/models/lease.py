from django.db import models

from real_estate.models.real_estate_object import RealEstateObject


class Lease(models.Model):
    address = models.CharField(max_length=255)

    description = models.TextField(null=True)

    real_estate_object = models.ForeignKey(
        RealEstateObject,
        on_delete=models.CASCADE
    )

    tenant = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='leases'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    price = models.FloatField()
