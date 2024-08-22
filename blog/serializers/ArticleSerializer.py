from rest_framework import serializers
from datetime import timezone
from account.serializers import UserSerializer
from blog.models import Article, Category, Tag
from blog.serializers.ArticlePhotoSerializer import ArticlePhotoSerializer


class ArticleSerializer(serializers.ModelSerializer):
    photos = ArticlePhotoSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Tag.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Article
        fields = [
            "id",
            "category",
            "title",
            "slug",
            "content",
            "author",
            "tags",
            "status",
            "published_at",
            "created_at",
            "updated_at",
            "photos",
        ]
        read_only_fields = ["created_at", "updated_at", "slug", "author"]

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Le titre doit contenir au moins 5 caractères."
            )
        return value

    def validate_content(self, value):
        if len(value) < 20:
            raise serializers.ValidationError(
                "Le contenu doit contenir au moins 20 caractères."
            )
        return value

    def validate_slug(self, value):
        if Article.objects.filter(slug=value).exists():
            raise serializers.ValidationError("Un article avec ce slug existe déjà.")
        return value

    def validate_status(self, value):
        if value == "published" and not self.instance.published_at:
            self.instance.published_at = timezone.now()
        return value
