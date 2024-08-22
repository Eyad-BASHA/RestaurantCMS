from rest_framework import serializers 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from restaurant.models.restaurant import AddressRestaurant
from django.core.exceptions import ValidationError

from restaurant.custom_permissions import IsAdminOrReadOnly



class AddressRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressRestaurant
        fields = [
            "id",
            "address_type",
            "street",
            "city",
            "zip_code",
            "country",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    def validate_zip_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Le code postal doit contenir uniquement des chiffres."
            )
        return value

    def validate(self, data):
        if data["country"] == "France" and len(data["zip_code"]) != 5:
            raise serializers.ValidationError(
                "Le code postal français doit contenir 5 chiffres."
            )
        return data
