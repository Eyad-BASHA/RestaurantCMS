from rest_framework import serializers
from remise.models import UsedDiscount


class UsedDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedDiscount
        fields = [
            "id",
            "client",
            "discount",
            "order",
            "used_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "used_at"]

    def validate(self, data):
        if data["discount"].is_active is False:
            raise serializers.ValidationError("Cette remise n'est plus active.")
        if data["order"].status not in ["pending", "accepted"]:
            raise serializers.ValidationError(
                "Les remises ne peuvent être appliquées qu'aux commandes en attente ou acceptées."
            )
        return data
