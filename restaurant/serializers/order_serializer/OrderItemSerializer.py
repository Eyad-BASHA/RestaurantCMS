from rest_framework import serializers
from restaurant.models.order import OrderItem
from restaurant.models.restaurant import MenuItem
from restaurant.serializers.restaurant_serializer import MenuItemSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    item_total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["id", "order", "menu_item", "quantity", "item_total", "note"]

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "La quantité doit être supérieure à zéro."
            )
        return value
