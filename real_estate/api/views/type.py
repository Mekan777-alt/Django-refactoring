from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from real_estate.api.serializers.real_estate_object_type import RealEstateObjectTypeSerializer
from real_estate.models import RealEstateObjectType
from rest_framework.response import Response
from rest_framework import status


class RealEstateObjectTypeAPIView(generics.ListCreateAPIView):
    queryset = RealEstateObjectType.objects.all().order_by('name')
    serializer_class = RealEstateObjectTypeSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

