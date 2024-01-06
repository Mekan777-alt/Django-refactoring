from django.db import models


#Аренда
class Lease(models.Model):
    address = models.CharField("Адрес", max_length=255)

    description = models.TextField("Описание", null=True)

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

    price = models.DecimalField(max_digits=19, decimal_places=2)
