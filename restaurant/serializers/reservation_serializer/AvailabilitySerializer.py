from rest_framework import serializers
from restaurant.models.reservation import Availability
from django.core.exceptions import ValidationError


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = [
            "id",
            "restaurant",
            "date",
            "start_time",
            "end_time",
            "table_number",
            "available_slots",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, data):
        if data["start_time"] >= data["end_time"]:
            raise ValidationError(
                "L'heure de début doit être antérieure à l'heure de fin."
            )
        return data
