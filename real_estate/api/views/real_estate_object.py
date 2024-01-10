from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from real_estate.api.serializers.real_estate_object import RealEstateObjectSerializer
from real_estate.models import RealEstateObject
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class RealEstateObjectAPIView(generics.ListCreateAPIView):
    queryset = RealEstateObject.objects.all()
    serializer_class = RealEstateObjectSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
