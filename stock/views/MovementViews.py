from rest_framework import generics, permissions
from stock.custom_permissions import IsAdminOrStockManager
from stock.models import StockMovement
from stock.serializers import StockMovementSerializer



class StockMovementListCreateView(generics.ListCreateAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsAdminOrStockManager]


class StockMovementDetailView(generics.RetrieveAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsAdminOrStockManager]
