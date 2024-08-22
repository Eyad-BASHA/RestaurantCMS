from rest_framework import generics, permissions
from blog.models import Reply
from blog.serializers import ReplySerializer
from blog.views.CustomPermissions import IsAdminOrModerator



class ReplyListCreateView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrModerator]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReplyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrModerator]
