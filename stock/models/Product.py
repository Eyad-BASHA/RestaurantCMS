from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.TimeStampedModel import TimeStampedModel


class Product(TimeStampedModel):
    """
    Modèle représentant un produit dans le stock.

    Ce modèle contient les informations essentielles sur un produit,
    y compris son nom, sa description, la quantité disponible en stock,
    l'unité de mesure utilisée, et l'emplacement de stockage initial.
    """

    UNIT_CHOICES = (
        ("kg", _("Kilogramme")),
        ("g", _("Gramme")),
        ("mg", _("Milligramme")),
        ("l", _("Litre")),
        ("ml", _("Millilitre")),
        ("cm", _("Centimètre")),
        ("m", _("Mètre")),
        ("piece", _("Pièce")),
        ("box", _("Boîte")),
        ("pack", _("Pack")),
        ("bottle", _("Bouteille")),
        ("dozen", _("Douzaine")),
        ("can", _("Canette")),
        ("jar", _("Pot")),
        ("bag", _("Sac")),
    )

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
        choices=UNIT_CHOICES,
        verbose_name=_("Unité de mesure"),
        help_text=_("L'unité de mesure pour ce produit."),
    )
    location = models.ForeignKey(
        "StockLocation",
        on_delete=models.CASCADE,
        verbose_name=_("Emplacement de stockage"),
        help_text=_("L'emplacement de stockage initial pour ce produit."),
    )

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit}) - {self.location.name}"

    class Meta:
        verbose_name = _("Produit")
        verbose_name_plural = _("Produits")
        ordering = ["name"]
