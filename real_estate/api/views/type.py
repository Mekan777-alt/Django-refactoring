from rest_framework import generics

from real_estate.api.serializers.real_estate_object_type import RealEstateObjectTypeSerializer
from real_estate.models import RealEstateObjectType


class RealEstateObjectTypeAPIView(generics.ListAPIView):
    queryset = RealEstateObjectType.objects.all()
    serializer_class = RealEstateObjectTypeSerializer
