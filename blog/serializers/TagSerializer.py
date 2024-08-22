from rest_framework import serializers
from blog.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le nom du tag doit contenir au moins 3 caractères."
            )
        return value
