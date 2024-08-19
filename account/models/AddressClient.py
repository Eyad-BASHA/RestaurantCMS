from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.TimeStampedModel import *


class AddressClient(TimeStampedModel):
    """
    Entité représentant une adresse pour un utilisateur.

    Cette entité permet de stocker plusieurs adresses pour un utilisateur,
    avec différents types comme livraison, facturation, etc.
    """

    ADDRESS_TYPE_CHOICES = [
        ("livraison", _("LIVRAISON")),
        ("facturation", _("FACTURATION")),
        ("siege", _("SIÈGE SOCIAL")),
        ("principale", _("PRINCIPALE")),
    ]

    address_type = models.CharField(
        max_length=255,
        choices=ADDRESS_TYPE_CHOICES,
        verbose_name=_("Type d'adresse"),
        help_text=_("Le type d'adresse, par exemple, livraison ou facturation."),
    )
    street = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Rue"),
        help_text=_("La rue associée à l'adresse."),
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Ville"),
        help_text=_("La ville où se situe l'adresse."),
    )
    zip_code = models.CharField(
        max_length=10,
        blank=True,
        verbose_name=_("Code postal"),
        help_text=_("Le code postal de l'adresse."),
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Pays"),
        help_text=_("Le pays de l'adresse."),
    )

    def __str__(self):
        return f"{self.street}, {self.zip_code}, {self.city}, {self.country}"

    class Meta:
        verbose_name = _("Adresse client")
        verbose_name_plural = _("Adresses clients")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("street", "city", "zip_code", "country")
        indexes = [models.Index(fields=["address_type"])]
