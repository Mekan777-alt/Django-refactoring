from rest_framework import serializers

from real_estate.models import Lease


class LeaseSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def create(self, validated_data):
        return Lease.objects.create(**validated_data)
