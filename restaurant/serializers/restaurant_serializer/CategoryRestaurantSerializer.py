from rest_framework import serializers
from restaurant.models.restaurant import CategoryRestaurant
from restaurant.custom_permissions import IsAdminOrReadOnly
from django.utils.text import slugify

class CategoryRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRestaurant
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "parent",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    permission_classes = [IsAdminOrReadOnly]

    def validate_name(self, value):
        if CategoryRestaurant.objects.filter(name=value).exists():
            raise serializers.ValidationError("Une catégorie avec ce nom existe déjà.")
        return value

    def validate_slug(self, value):
        if CategoryRestaurant.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Un slug avec ce nom existe déjà.")
        return value

    def create(self, validated_data):
        if not validated_data.get("slug"):
            validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)
