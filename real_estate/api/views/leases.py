from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from real_estate.api.serializers.lease import LeaseSerializer
from real_estate.models import Lease
from rest_framework.pagination import PageNumberPagination
from real_estate.models import RealEstateObject
from real_estate.tasks import generate_rental_agr


class LeaseAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer

    def create(self, request, *args, **kwargs):
        r = RealEstateObject.objects.filter(pk=kwargs['pk']).first()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lease = serializer.save(real_estate_object=r, tenant=request.user)

        generate_rental_agr(lease)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
