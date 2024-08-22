"""
Serializers for the user API View.
"""

from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from django.utils.translation import gettext as _
import logging

from account.models.AddressClient import AddressClient
from account.models.Profile import Profile

logger = logging.getLogger(__name__)


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

        # logger.debug(f"Authenticating user with email_or_username: {email_or_username}")

        user = authenticate(
            request=self.context.get("request"),
            username=email_or_username,
            password=password,
        )

        if not user:
            # logger.debug(f"First authentication attempt failed for {email_or_username}")
            User = get_user_model()
            try:
                user_obj = User.objects.get(email=email_or_username)
                user = authenticate(
                    request=self.context.get("request"),
                    username=user_obj.username,
                    password=password,
                )
            except User.DoesNotExist:
                # logger.debug(f"User with email {email_or_username} does not exist")
                pass

        if not user:
            msg = _("Unable to authenticate with provided credentials")
            # logger.debug(f"Authentication failed: {msg}")
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


class PasswordResetConfirmSerializer(serializers.Serializer):
    password = serializers.CharField()
    token = serializers.CharField()

    def validate(self, attrs):
        """Validate the password reset token"""
        # This is a placeholder for actual implementation
        return attrs


class AddressClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressClient
        fields = ["address_type", "street", "city", "zip_code", "country"]


class ProfileSerializer(serializers.ModelSerializer):
    addresses = AddressClientSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = [
            "loyalty_number",
            "gender",
            "phone_number",
            "bio",
            "profile_image",
            "date_of_birth",
            "addresses",
        ]

    def create(self, validated_data):
        addresses_data = validated_data.pop("addresses", [])
        profile = Profile.objects.create(**validated_data)

        for address_data in addresses_data:
            address, created = AddressClient.objects.get_or_create(**address_data)
            profile.addresses.add(address)

        return profile

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop("addresses", [])
        instance.loyalty_number = validated_data.get(
            "loyalty_number", instance.loyalty_number
        )
        instance.gender = validated_data.get("gender", instance.gender)
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.bio = validated_data.get("bio", instance.bio)
        instance.profile_image = validated_data.get(
            "profile_image", instance.profile_image
        )
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.save()

        instance.addresses.clear()
        for address_data in addresses_data:
            address, created = AddressClient.objects.get_or_create(**address_data)
            instance.addresses.add(address)

        return instance


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    profile = ProfileSerializer(required=False)

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "username", "profile")
        extra_kwargs = {"password": {"write_only": True, "min_length": 8}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        profile_data = validated_data.pop("profile", None)
        user = get_user_model().objects.create_user(**validated_data)

        if profile_data:
            Profile.objects.create(user=user, **profile_data)

        # return get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""

        profile_data = validated_data.pop("profile", None)
        user = super().update(instance, validated_data)

        if profile_data:
            profile = user.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if "password" in validated_data:
            user.set_password(validated_data["password"])
            user.save()

        return user
