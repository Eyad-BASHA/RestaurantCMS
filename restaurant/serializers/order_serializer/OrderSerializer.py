from rest_framework import serializers
from restaurant.models.order import Order, OrderItem
from account.serializers import (
    UserSerializer,
)  


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "menu_item", "quantity", "item_total", "note"]


class OrderSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)
    staff = serializers.StringRelatedField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "order_type",
            "client",
            "client_name",
            "table_number",
            "staff",
            "restaurant",
            "items",
            "status",
            "total_amount",
            "note",
            "created_at",
            "updated_at",
        ]

    def validate_status(self, value):
        if self.instance and self.instance.status not in ["pending", "accepted"]:
            raise serializers.ValidationError(
                "Vous ne pouvez pas modifier cette commande."
            )
        return value
