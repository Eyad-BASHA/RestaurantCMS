from rest_framework import generics, permissions
from restaurant.models.restaurant import PhotoMenuItem
from restaurant.serializers import PhotoMenuItemSerializer
from restaurant.custom_permissions import IsAdminOrReadOnly


class PhotoMenuItemListCreateView(generics.ListCreateAPIView):
    queryset = PhotoMenuItem.objects.all()
    serializer_class = PhotoMenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]


class PhotoMenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhotoMenuItem.objects.all()
    serializer_class = PhotoMenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]
