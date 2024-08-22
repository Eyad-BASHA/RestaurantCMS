from rest_framework import serializers, permissions
from restaurant.models.restaurant import TypeMenuItem
from restaurant.custom_permissions import IsAdminOrReadOnly
from django.utils.text import slugify


class TypeMenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMenuItem
        fields = ["id", "name", "slug", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    def validate_name(self, value):
        if TypeMenuItem.objects.filter(name=value).exists():
            raise serializers.ValidationError("Un type avec ce nom existe déjà.")
        return value

    def validate_slug(self, value):
        if TypeMenuItem.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Un slug avec ce nom existe déjà.")
        return value

    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)
