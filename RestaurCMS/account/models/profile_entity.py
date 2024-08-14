"""Profile Enity pour Customuser"""

from django.db import models

from RestaurCMS.account.models.address_entity import Address
from RestaurCMS.account.models.custom_user_entity import CustomUser
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Profile(models.Model):
    """Profile model."""

    GENDER_CHOICES = (
        ("homme", "HOMME"),
        ("femme", "FEMME"),
        ("autre", "AUTRE"),
    )
    user = models.OneToOneField(
        CustomUser, related_name="profile", on_delete=models.CASCADE
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=50, blank=False, null=False, unique=True)
    bio = models.TextField(max_length=255, blank=True)
    profile_image = models.ImageField(
        upload_to="photos/profile",
        blank=True,
        null=True,
        default="photos/profile/user_picture/user_img.png",
        verbose_name=_("Photo d'Utilisateur"),
    )
    date_of_birth = models.DateField(blank=True, null=True)

    addresses = models.ManyToManyField(Address, related_name="profiles")

    is_comment = models.BooleanField(default=True, verbose_name=_("Pouvez Commenter"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    # RESIZING THE PICTURE
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        img = Image.open(self.profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)
