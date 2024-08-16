import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image
from account.models.AddressClient import AddressClient
from account.models.CustomUser import CustomUser
from restaurant.models.common.TimeStampedModel import *


class Profile(TimeStampedModel):
    """
    Modèle représentant le profil d'un utilisateur.

    Ce modèle contient des informations personnelles supplémentaires pour l'utilisateur,
    telles que le genre, la date de naissance, le numéro de téléphone, et l'image de profil.
    """

    GENDER_CHOICES = (
        ("homme", _("HOMME")),
        ("femme", _("FEMME")),
        ("autre", _("AUTRE")),
    )

    user = models.OneToOneField(
        CustomUser,
        related_name="profile",
        on_delete=models.CASCADE,
        verbose_name=_("Utilisateur"),
        help_text=_("L'utilisateur associé à ce profil."),
    )
    loyalty_number = models.CharField(
        max_length=36,
        unique=True,
        verbose_name=_("Numéro de fidélité"),
        help_text=_("Numéro unique de fidélité pour l'utilisateur."),
        default=uuid.uuid4,
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        verbose_name=_("Genre"),
        help_text=_("Le genre de l'utilisateur."),
    )
    phone_number = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
        verbose_name=_("Numéro de téléphone"),
        help_text=_("Le numéro de téléphone unique de l'utilisateur."),
    )
    bio = models.TextField(
        max_length=255,
        blank=True,
        verbose_name=_("Biographie"),
        help_text=_("Une courte biographie de l'utilisateur."),
    )
    profile_image = models.ImageField(
        upload_to="photos/profile",
        blank=True,
        null=True,
        default="photos/profile/user_picture/user_img.png",
        verbose_name=_("Photo d'utilisateur"),
        help_text=_("Une photo représentant l'utilisateur."),
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Date de naissance"),
        help_text=_("La date de naissance de l'utilisateur."),
    )
    addresses = models.ManyToManyField(
        AddressClient,
        related_name="profiles",
        verbose_name=_("Adresses"),
        help_text=_("Les adresses associées à ce profil."),
    )
    is_comment = models.BooleanField(
        default=True,
        verbose_name=_("Peut commenter"),
        help_text=_("Indique si l'utilisateur est autorisé à commenter."),
    )

    def __str__(self):
        return f"{self.user.username} - {self.loyalty_number}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        """
        Redimensionner l'image de profil
        si elle dépasse les dimensions autorisées.
        """
        super().save(force_insert, force_update, using, update_fields)
        if self.profile_image:
            img = Image.open(self.profile_image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_image.path)

    class Meta:
        verbose_name = _("Profil")
        verbose_name_plural = _("Profils")
        ordering = ["-created_at"]
