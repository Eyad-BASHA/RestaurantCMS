from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.TimeStampedModel import TimeStampedModel


class AddressRestaurant(TimeStampedModel):
    """
    Adresse de restaurant.

    Cette entité représente une adresse associée à un restaurant.
    Elle permet de stocker différentes adresses pour des usages spécifiques
    comme la facturation, le siège social ou l'adresse principale.
    """

    ADDRESS_TYPE_CHOICES = [
        ("facturation", _("Facturation")),
        ("siege", _("Siège Social")),
        ("principale", _("Principale")),
    ]

    address_type = models.CharField(
        max_length=255,
        choices=ADDRESS_TYPE_CHOICES,
        verbose_name=_("Type d'adresse"),
        help_text=_(
            "Le type d'adresse, par exemple, Facturation, Siège Social, ou Principale."
        ),
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
        verbose_name=_("Code Postal"),
        help_text=_("Le code postal de l'adresse."),
    )
    country = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Pays"),
        help_text=_("Le pays de l'adresse."),
    )

    def __str__(self):
        return f"{self.address_type} : {self.street}, {self.zip_code}, {self.city}, {self.country}"

    class Meta:
        verbose_name = _("Adresse de restaurant")
        verbose_name_plural = _("Adresses de restaurants")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("street", "city", "zip_code", "country")
        indexes = [models.Index(fields=["address_type"])]
