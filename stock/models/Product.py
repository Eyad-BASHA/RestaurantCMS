from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.TimeStampedModel import TimeStampedModel


class Product(TimeStampedModel):
    """
    Modèle représentant un produit dans le stock.

    Ce modèle contient les informations essentielles sur un produit,
    y compris son nom, sa description, la quantité disponible en stock,
    et l'unité de mesure utilisée.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Nom du produit"),
        help_text=_("Le nom du produit."),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description du produit."),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantité en stock"),
        help_text=_("La quantité disponible en stock."),
    )
    unit = models.CharField(
        max_length=50,
        verbose_name=_("Unité de mesure"),
        help_text=_("L'unité de mesure pour ce produit (par ex: kg, litre, etc.)."),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Produit")
        verbose_name_plural = _("Produits")
        ordering = ["name"]
