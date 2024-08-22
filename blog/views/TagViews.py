from rest_framework import generics 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.models import Tag
from blog.serializers import TagSerializer
from blog.views.CustomPermissions import IsAdminOrModerator


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrModerator]


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrModerator]
