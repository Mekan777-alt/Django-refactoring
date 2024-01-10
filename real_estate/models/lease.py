from django.db import models


#Аренда
class Lease(models.Model):
    real_estate_object = models.ForeignKey(
        'real_estate.RealEstateObject',
        on_delete=models.CASCADE,
        related_name='объект_недвижимости'
    )

    tenant = models.ForeignKey(
        'authentication.User',
        on_delete=models.CASCADE,
        related_name='арендатор'
    )

    start_date = models.DateField()
    end_date = models.DateField()
