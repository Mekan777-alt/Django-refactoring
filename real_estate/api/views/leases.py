from time import sleep
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from real_estate.api.serializers.lease import LeaseSerializer
from real_estate.models import Lease, RealEstateObject
from rest_framework_simplejwt.authentication import JWTAuthentication


def generate_rental_agr(lease):
    # Какая-то очень долгая логика по генерации документа
    sleep(20)


class LeaseAPIView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer

    def create(self, request, *args, **kwargs):
        r = get_object_or_404(RealEstateObject, pk=kwargs['pk'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        lease = serializer.save(real_estate_object=r, tenant=request.user)
        generate_rental_agr(lease)

        response_serializer = LeaseSerializer(lease)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
