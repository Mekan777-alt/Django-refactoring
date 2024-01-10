from rest_framework import serializers
from real_estate.models import RealEstateObjectType


class RealEstateObjectTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        return RealEstateObjectType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
