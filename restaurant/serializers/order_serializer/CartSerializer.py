from rest_framework import serializers
from restaurant.models.order import Cart, CartItem
from account.serializers import (
    UserSerializer,
)  


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["id", "menu_item", "quantity", "item_total"]


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Assuming you want to show user details
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Cart
        fields = ["id", "user", "cart_items", "total_price"]
