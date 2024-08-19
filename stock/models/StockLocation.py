from django.db import models
from common.models.TimeStampedModel import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class StockLocation(TimeStampedModel):
    """
    Modèle représentant un emplacement de stockage.

    Ce modèle contient les informations relatives à un emplacement spécifique
    où les produits sont stockés, comme le nom de l'emplacement et son adresse.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Nom de l'emplacement"),
        help_text=_("Le nom de l'emplacement de stockage."),
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Adresse"),
        help_text=_("L'adresse de l'emplacement de stockage."),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Emplacement de stock")
        verbose_name_plural = _("Emplacements de stock")
        ordering = ["name"]
