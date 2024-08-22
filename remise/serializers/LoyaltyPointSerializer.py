from datetime import timezone
from rest_framework import serializers
from remise.models import LoyaltyPoint


class LoyaltyPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyPoint
        fields = [
            "id",
            "client",
            "program",
            "points",
            "earned_date",
            "expiry_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "earned_date"]

    def validate_points(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Les points ne peuvent pas être négatifs."
            )
        return value

    def validate_expiry_date(self, value):
        if value and value <= timezone.now():
            raise serializers.ValidationError(
                "La date d'expiration doit être dans le futur."
            )
        return value
