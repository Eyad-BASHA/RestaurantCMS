from django.db import models
from common.models.TimeStampedModel import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class StockMovement(TimeStampedModel):
    """
    Modèle représentant un mouvement de stock.

    Ce modèle enregistre les mouvements de produits d'un emplacement de stockage
    à un autre, avec des informations telles que le produit déplacé, la quantité déplacée,
    l'emplacement source et l'emplacement destination.
    """

    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        verbose_name=_("Produit"),
        help_text=_("Le produit déplacé."),
    )
    from_location = models.ForeignKey(
        "StockLocation",
        on_delete=models.CASCADE,
        related_name="outgoing_movements",
        verbose_name=_("De l'emplacement"),
        help_text=_("L'emplacement source d'où le produit est déplacé."),
    )
    to_location = models.ForeignKey(
        "StockLocation",
        on_delete=models.CASCADE,
        related_name="incoming_movements",
        verbose_name=_("À l'emplacement"),
        help_text=_("L'emplacement destination où le produit est déplacé."),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantité déplacée"),
        help_text=_("La quantité du produit déplacé."),
    )
    movement_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date du mouvement"),
        help_text=_("La date et l'heure du mouvement de stock."),
    )

    def __str__(self):
        return f"Déplacement de {self.product.name} - {self.quantity} {self.product.unit} de {self.from_location.name} à {self.to_location.name}"

    class Meta:
        verbose_name = _("Mouvement de stock")
        verbose_name_plural = _("Mouvements de stock")
        ordering = ["-movement_date"]
