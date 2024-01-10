from time import sleep
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from real_estate.api.serializers.lease import LeaseSerializer
from real_estate.models import Lease
from rest_framework.pagination import PageNumberPagination


def generate_rental_agr(lease):
    # Какая-то очень долгая логика по генерации документа
    sleep(20)


class LeaseAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    pagination_class = PageNumberPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(self.get_paginated_response(serializer.data))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
