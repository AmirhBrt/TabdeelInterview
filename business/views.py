from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.db import transaction

from .serializers import CreateSellerSerializer, ChargeRecordSerializer


class CreateSellerView(APIView):

    @staticmethod
    def post(request):
        seller_serializer = CreateSellerSerializer(data=request.data)
        if seller_serializer.is_valid():
            with transaction.atomic():
                seller_serializer.save()
                return Response({'message': 'Seller created successfully', 'data': seller_serializer.data},
                                status=status.HTTP_201_CREATED)
        return Response({'message': 'Error creating seller', 'errors': seller_serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class CreateChargeRecordView(APIView):
    @transaction.atomic
    def post(self, request):
        charge_record_serializer = ChargeRecordSerializer(data=request.data)
        if charge_record_serializer.is_valid():
            charge_record_serializer.save()
            return Response({'message': 'Charge recorde has been done', 'data': charge_record_serializer.
                            data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'An error has been occurred during creation',
                         'errors': charge_record_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
