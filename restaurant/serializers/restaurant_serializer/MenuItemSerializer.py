from rest_framework import serializers, permissions
from restaurant.models.restaurant import MenuItem
from restaurant.custom_permissions import IsAdminOrReadOnly
from django.utils.text import slugify


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "menu",
            "name",
            "slug",
            "description",
            "price",
            "category",
            "type",
            "is_from_kitchen",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Le prix ne peut pas être négatif.")
        return value

    def validate_slug(self, value):
        if MenuItem.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Un slug avec ce nom existe déjà.")
        return value

    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)
