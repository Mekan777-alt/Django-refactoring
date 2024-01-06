from rest_framework import serializers
from authentication.api.serializers.group import GroupSerializers


class UserDetailSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    group = serializers.SerializerMethodField()

    def get_group(self, user):
        group = user.groups.first()

        return GroupSerializers(group).data
