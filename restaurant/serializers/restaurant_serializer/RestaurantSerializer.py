from rest_framework import serializers, permissions
from restaurant.models.restaurant import Restaurant
from restaurant.custom_permissions import IsAdminOrReadOnly
from django.utils.text import slugify


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "slug",
            "category",
            "description",
            "addresses",
            "logo",
            "staff",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    def validate_slug(self, value):
        if Restaurant.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Un slug avec ce nom existe déjà.")
        return value

    def validate_logo(self, value):
        if value and value.size > 1024 * 1024:
            raise serializers.ValidationError(
                "La taille du logo ne doit pas dépasser 1 Mo."
            )
        return value

    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)
