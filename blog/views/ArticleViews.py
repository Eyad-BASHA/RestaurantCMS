from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Article
from blog.serializers import ArticleSerializer
from blog.views.CustomPermissions import IsAdminOrModerator

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrModerator]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrModerator]
