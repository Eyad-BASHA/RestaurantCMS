from rest_framework import serializers
from blog.models import LikeComment


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = ["id", "author", "comment", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
