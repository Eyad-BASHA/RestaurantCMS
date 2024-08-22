from rest_framework import serializers
from restaurant.models.reservation import Reservation, Availability
from restaurant.serializers.reservation_serializer import AvailabilitySerializer
from django.core.exceptions import ValidationError
from django.utils import timezone


class ReservationSerializer(serializers.ModelSerializer):
    tables = AvailabilitySerializer(many=True)

    class Meta:
        model = Reservation
        fields = [
            "id",
            "user",
            "restaurant",
            "reservation_date",
            "start_time",
            "end_time",
            "number_of_people",
            "special_request",
            "is_confirmed",
            "tables",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate_reservation_date(self, value):
        if value < timezone.now().date():
            raise ValidationError(
                "La date de la réservation ne peut pas être dans le passé."
            )
        return value

    def create(self, validated_data):
        tables_data = validated_data.pop("tables")
        reservation = Reservation.objects.create(**validated_data)
        for table_data in tables_data:
            availability = Availability.objects.get(
                restaurant=table_data["restaurant"],
                date=table_data["date"],
                start_time=table_data["start_time"],
                table_number=table_data["table_number"],
            )
            if availability.available_slots < validated_data["number_of_people"]:
                raise ValidationError(
                    f"La table {availability.table_number} n'a pas assez de places disponibles."
                )
            reservation.tables.add(availability)
        return reservation

    def update(self, instance, validated_data):
        tables_data = validated_data.pop("tables", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tables_data:
            instance.tables.clear()
            for table_data in tables_data:
                availability = Availability.objects.get(
                    restaurant=table_data["restaurant"],
                    date=table_data["date"],
                    start_time=table_data["start_time"],
                    table_number=table_data["table_number"],
                )
                if availability.available_slots < instance.number_of_people:
                    raise ValidationError(
                        f"La table {availability.table_number} n'a pas assez de places disponibles."
                    )
                instance.tables.add(availability)

        return instance
