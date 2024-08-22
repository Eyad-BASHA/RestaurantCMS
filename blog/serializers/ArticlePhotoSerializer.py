from rest_framework import serializers
from blog.models import ArticlePhoto


class ArticlePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePhoto
        fields = ["id", "article", "image", "alt_text", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_alt_text(self, value):
        if len(value) > 255:
            raise serializers.ValidationError(
                "Le texte alternatif ne peut pas dépasser 255 caractères."
            )
        return value
