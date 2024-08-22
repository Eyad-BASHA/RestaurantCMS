from rest_framework import serializers
from remise.models import LoyaltyProgram


class LoyaltyProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyProgram
        fields = [
            "id",
            "name",
            "points_per_euro",
            "start_date",
            "end_date",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate_points_per_euro(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Le nombre de points par euro ne peut pas être négatif."
            )
        return value

    def validate(self, data):
        if data["end_date"] and data["end_date"] <= data["start_date"]:
            raise serializers.ValidationError(
                "La date de fin doit être postérieure à la date de début."
            )
        return data
