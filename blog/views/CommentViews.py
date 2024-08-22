from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Comment
from blog.serializers import CommentSerializer
from blog.views.CustomPermissions import IsAdminOrModeratorOrAuthor


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAdminOrModeratorOrAuthor,
    ]
