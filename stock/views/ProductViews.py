from rest_framework import generics, permissions
from stock.custom_permissions.IsAdminOrStockManager import IsAdminOrStockManager
from stock.models import Product
from stock.serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrStockManager]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrStockManager]
