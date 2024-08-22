from rest_framework import serializers
from stock.models import StockMovement


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = [
            "id",
            "product",
            "from_location",
            "to_location",
            "quantity",
            "movement_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "movement_date"]

    def validate(self, data):
        if data["quantity"] <= 0:
            raise serializers.ValidationError(
                "La quantité doit être supérieure à zéro."
            )
        if data["from_location"] == data["to_location"]:
            raise serializers.ValidationError(
                "Les emplacements source et destination ne peuvent pas être identiques."
            )
        return data
