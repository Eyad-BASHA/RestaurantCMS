from rest_framework import generics, permissions
from restaurant.models.restaurant import (
    Menu,
    MenuItem,
    TypeMenuItem,
    CategoryMenuItem,
    CategoryRestaurant,
)
from restaurant.serializers import (
    MenuSerializer,
    MenuItemSerializer,
    TypeMenuItemSerializer,
    CategoryMenuItemSerializer,
    CategoryRestaurantSerializer,
)
from restaurant.custom_permissions import IsAdminOrReadOnly


# Menu Views
class MenuListCreateView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Menu Item Views
class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Type Menu Item Views
class TypeMenuItemListCreateView(generics.ListCreateAPIView):
    queryset = TypeMenuItem.objects.all()
    serializer_class = TypeMenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]


class TypeMenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeMenuItem.objects.all()
    serializer_class = TypeMenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]


# Category Menu Item Views
class CategoryMenuItemListCreateView(generics.ListCreateAPIView):
    queryset = CategoryMenuItem.objects.all()
    serializer_class = CategoryMenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryMenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryMenuItem.objects.all()
    serializer_class = CategoryMenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]


# Category Restaurant Views
class CategoryRestaurantListCreateView(generics.ListCreateAPIView):
    queryset = CategoryRestaurant.objects.all()
    serializer_class = CategoryRestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryRestaurantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryRestaurant.objects.all()
    serializer_class = CategoryRestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]
