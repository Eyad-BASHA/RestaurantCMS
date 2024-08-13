"""
Serializers for the user API View.
"""

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "username")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    email_or_username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email_or_username = attrs.get("email_or_username")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email_or_username,
            password=password,
        )

        if not user:
            User = get_user_model()
            try:
                user_obj = User.objects.get(email=email_or_username)
                user = authenticate(
                    request=self.context.get("request"),
                    username=user_obj.username,
                    password=password,
                )
            except User.DoesNotExist:
                pass

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authentication")

        attrs["user"] = user
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        """Validate that the email exists in the system"""
        if not get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "No user is associated with this email address."
            )
        return value

    def save(self):
        """Send password reset email"""
        from django.core.mail import send_mail
        from django.conf import settings

        user = get_user_model().objects.get(email=self.validated_data["email"])
        # Generate password reset token and send email
        # This is a placeholder for actual implementation
        send_mail(
            "Password Reset",
            "Here is the link to reset your password: <reset_link>",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )
