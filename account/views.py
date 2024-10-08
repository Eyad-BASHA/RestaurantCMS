"""
Views for the user API
"""
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from rest_framework import generics, authentication, permissions, status

from account.models import Role
from .serializers import PasswordResetSerializer, RoleSerializer, UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from account.models.Profile import Profile


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
    # authentication_classes = []
    # permission_classes = []


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse("Your account has been activated successfully.")
    else:
        return HttpResponse("Activation link is invalid!")


# class CreateTokenView(TokenObtainPairView):
#     """Create a new auth token for user"""

#     serializer_class = AuthTokenSerializer
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CreateTokenView(APIView):
    """Create a new auth token for user"""

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Password reset email has been sent."}, status=status.HTTP_200_OK
        )


def user_profile_view(request, user_id):
    try:
        profile = Profile.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        profile = None

    context = {
        "profile": profile,
    }
    return render(request, "user_profile.html", context)


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
