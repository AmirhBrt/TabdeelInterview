from rest_framework.views import APIView
from rest_framework.views import Response

from serializers import SellerSerializer


class CreateSellerView(APIView):
    def post(self, request):
        seller_serializer = SellerSerializer(data=request.data)
        if seller_serializer.is_valid():
            return Response({'message': 'Seller created successfully', 'data': seller_serializer.data})
        return Response({'message': 'Error creating seller', 'errors': seller_serializer.errors})
