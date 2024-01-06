from rest_framework import serializers


class GroupSerializers(serializers.Serializer):
    name = serializers.CharField()
