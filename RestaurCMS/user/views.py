"""
Views for the user API
"""

from rest_framework import generics, authentication, permissions
from RestaurCMS.user.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
    # authentication_classes = []
    # permission_classes = []


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
