from rest_framework import serializers, permissions
from restaurant.models.restaurant import Menu
from restaurant.custom_permissions import IsAdminOrReadOnly
from django.utils.text import slugify


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "id",
            "restaurant",
            "name",
            "slug",
            "description",
            "menu_photo",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    def validate_slug(self, value):
        if Menu.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Un slug avec ce nom existe déjà.")
        return value

    def validate_menu_photo(self, value):
        if value and value.size > 1024 * 1024:
            raise serializers.ValidationError(
                "La taille de l'image ne doit pas dépasser 1 Mo."
            )
        return value

    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)
