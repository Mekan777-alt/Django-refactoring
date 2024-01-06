from time import sleep

from rest_framework import generics, status
from rest_framework.response import Response

from real_estate.api.serializers.lease import LeaseSerializer
from real_estate.models import Lease, RealEstateObject


def generate_rental_agr(lease):
    # Какая-то очень долгая логика по генерации документа
    sleep(20)


class LeaseAPIView(generics.ListCreateAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer

    def create(self, request, *args, **kwargs):
        r = RealEstateObject.objects.filter(pk=kwargs['pk']).first()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lease = serializer.save(real_estate_object=r, tenant=request.user)

        generate_rental_agr(lease)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
