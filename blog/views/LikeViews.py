from rest_framework import generics, permissions
from blog.models import LikeArticle, LikeComment
from blog.serializers import LikeArticleSerializer, LikeCommentSerializer
from blog.views.CustomPermissions import IsAuthenticatedClient


class LikeArticleCreateView(generics.CreateAPIView):
    queryset = LikeArticle.objects.all()
    serializer_class = LikeArticleSerializer
    permission_classes = [IsAuthenticatedClient]


class LikeCommentCreateView(generics.CreateAPIView):
    queryset = LikeComment.objects.all()
    serializer_class = LikeCommentSerializer
    permission_classes = [IsAuthenticatedClient]
