from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from authentication.api.serializers.registration import RegistrationSerializer
from authentication.api.serializers.user_detail import UserDetailSerializers


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        user_serializer = UserDetailSerializers(instance=user)

        return Response(data=user_serializer.data, status=status.HTTP_201_CREATED)
