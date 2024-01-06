from rest_framework import generics

from authentication.api.serializers.registration import RegistrationSerializer


class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
