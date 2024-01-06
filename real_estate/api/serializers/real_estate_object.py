from rest_framework import serializers

from real_estate.models import RealEstateObject


class RealEstateObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateObject
        fields = '__all__'
