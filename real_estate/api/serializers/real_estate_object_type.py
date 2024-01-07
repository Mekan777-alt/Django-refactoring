from rest_framework import serializers


class RealEstateObjectTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    def create(self, validated_data):
        return RealEstateObjectTypeSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
