from django.db import models
from django.utils.translation import gettext_lazy as _
from restaurant.models.order import Order
from restaurant.models.restaurant import MenuItem
from common.models.TimeStampedModel import TimeStampedModel


class OrderItem(TimeStampedModel):
    """
    Élément de commande.

    Cette entité représente un élément spécifique (un plat ou un produit)
    dans une commande. Elle relie un élément de menu à une commande particulière
    en spécifiant la quantité commandée et toute note supplémentaire.
    """

    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_items"
    )
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name="menu_items"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantité"))
    item_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Total de l'article"),
        editable=False,
    )

    note = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Note"),
        help_text=_("Une note optionnelle pour l'article de commande."),
    )

    def save(self, *args, **kwargs):
        self.item_total = self.menu_item.price * self.quantity
        super(OrderItem, self).save(*args, **kwargs)
        self.order.update_total_amount()

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity})"

    class Meta:
        verbose_name = _("Élément de commande")
        verbose_name_plural = _("Éléments de commande")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        indexes = [models.Index(fields=["order", "menu_item"])]
