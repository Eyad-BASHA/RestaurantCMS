from rest_framework import serializers
from restaurant.models.restaurant import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "menu_item",
            "user",
            "rating",
            "comment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "La note doit être comprise entre 1 et 5."
            )
        return value
