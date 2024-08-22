from rest_framework import serializers
from account.serializers import UserSerializer
from blog.models import Reply


class ReplySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ["id", "comment", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at", "author"]

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "La réponse doit contenir au moins 10 caractères."
            )
        return value
