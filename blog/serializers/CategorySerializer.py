from rest_framework import serializers
from blog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le nom de la catégorie doit contenir au moins 3 caractères."
            )
        return value
