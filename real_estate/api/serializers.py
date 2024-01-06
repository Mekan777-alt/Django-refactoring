from rest_framework import serializers

from real_estate.models import RealEstateObject, Lease


class RealEstateObjectTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class RealEstateObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateObject
        fields = '__all__'


class LeaseSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    price = serializers.FloatField()

    def create(self, validated_data):
        return Lease.objects.create(**validated_data)
