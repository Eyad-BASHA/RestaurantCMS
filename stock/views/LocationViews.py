from rest_framework import generics, permissions
from stock.custom_permissions import IsAdminOrStockManager
from stock.models import StockLocation
from stock.serializers import StockLocationSerializer



class StockLocationListCreateView(generics.ListCreateAPIView):
    queryset = StockLocation.objects.all()
    serializer_class = StockLocationSerializer
    permission_classes = [IsAdminOrStockManager]


class StockLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockLocation.objects.all()
    serializer_class = StockLocationSerializer
    permission_classes = [IsAdminOrStockManager]
