from rest_framework import generics

from real_estate.api.serializers import RealEstateObjectSerializer
from real_estate.models import RealEstateObject


class RealEstateObjectAPIView(generics.ListCreateAPIView):
    queryset = RealEstateObject.objects.all()
    serializer_class = RealEstateObjectSerializer
