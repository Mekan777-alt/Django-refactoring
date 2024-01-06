from django.db import models


#тип объекта недвижимости
class RealEstateObjectType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
