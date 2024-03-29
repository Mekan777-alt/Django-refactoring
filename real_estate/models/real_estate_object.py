from django.db import models


# объект недвижимости
class RealEstateObject(models.Model):
    cadastral_number = models.CharField(max_length=255)

    address = models.CharField(max_length=255)

    description = models.TextField()

    price = models.DecimalField(max_digits=19, decimal_places=2)

    owner = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE
    )

    type = models.ForeignKey(
        'real_estate.RealEstateObjectType',
        on_delete=models.CASCADE,
        related_name='real_estate_objects'
    )
