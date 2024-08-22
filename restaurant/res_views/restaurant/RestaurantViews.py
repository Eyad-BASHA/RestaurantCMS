from rest_framework import generics, permissions
from restaurant.models.restaurant import Restaurant, AddressRestaurant
from restaurant.serializers import RestaurantSerializer, AddressRestaurantSerializer


# Permissions
class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit it.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.is_superuser


# Restaurant Views
class RestaurantListCreateView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


class RestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


# Address Views
class AddressRestaurantListCreateView(generics.ListCreateAPIView):
    queryset = AddressRestaurant.objects.all()
    serializer_class = AddressRestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


class AddressRestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddressRestaurant.objects.all()
    serializer_class = AddressRestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]
