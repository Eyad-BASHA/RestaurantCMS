from rest_framework import serializers
from blog.models import LikeArticle


class LikeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeArticle
        fields = ["id", "author", "article", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
