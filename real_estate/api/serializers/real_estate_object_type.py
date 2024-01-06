from rest_framework import serializers


class RealEstateObjectTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
