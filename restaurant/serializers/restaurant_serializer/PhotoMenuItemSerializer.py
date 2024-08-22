from rest_framework import serializers
from restaurant.models.restaurant import PhotoMenuItem


class PhotoMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoMenuItem
        fields = ["id", "menu_item", "photo", "alt_text", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_photo(self, value):
        if value.size > 1024 * 1024:
            raise serializers.ValidationError(
                "La taille de l'image ne doit pas dépasser 1 Mo."
            )
        return value
