from django.db import models
from django.utils.translation import gettext_lazy as _
from restaurant.models.order import Order
from restaurant.models.restaurant import MenuItem
from ..common import TimeStampedModel


class OrderItem(TimeStampedModel):
    """
    Élément de commande.

    Cette entité représente un élément spécifique (un plat ou un produit)
    dans une commande. Elle relie un élément de menu à une commande particulière
    en spécifiant la quantité commandée et toute note supplémentaire.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name=_("Commande"),
        help_text=_("La commande à laquelle cet élément est associé."),
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        verbose_name=_("Élément de menu"),
        help_text=_("L'élément de menu commandé."),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantité"),
        help_text=_("La quantité commandée pour cet élément de menu."),
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Note"),
        help_text=_("Une note optionnelle pour cet élément de commande."),
    )

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

    class Meta:
        verbose_name = _("Élément de commande")
        verbose_name_plural = _("Éléments de commande")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("order", "menu_item")
        indexes = [models.Index(fields=["order", "menu_item"])]
