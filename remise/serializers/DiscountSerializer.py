from rest_framework import serializers
from remise.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [
            "id",
            "code",
            "discount_type",
            "value",
            "min_order_amount",
            "start_date",
            "end_date",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate_value(self, value):
        if self.instance and self.instance.discount_type == "percentage":
            if not 0 <= value <= 100:
                raise serializers.ValidationError(
                    "La valeur doit être comprise entre 0 et 100 pour un pourcentage."
                )
        elif value < 0:
            raise serializers.ValidationError("La valeur ne peut pas être négative.")
        return value

    def validate(self, data):
        if data["end_date"] <= data["start_date"]:
            raise serializers.ValidationError(
                "La date de fin doit être postérieure à la date de début."
            )
        return data
