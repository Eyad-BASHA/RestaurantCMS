from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from restaurant.models.order import Cart
from restaurant.models.restaurant import MenuItem
from common.models.TimeStampedModel import TimeStampedModel
from decimal import Decimal

class CartItem(TimeStampedModel):
    """
    Élément du panier.

    Cette entité représente un article spécifique dans le panier d'un utilisateur,
    incluant l'élément de menu sélectionné et la quantité souhaitée.
    """

    cart = models.ForeignKey(
        "Cart",
        on_delete=models.CASCADE,
        related_name="cart_items",
        verbose_name=_("Panier"),
        help_text=_("Le panier auquel cet article est associé."),
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        verbose_name=_("Élément de menu"),
        help_text=_("L'élément de menu ajouté au panier."),
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantité"),
        help_text=_("La quantité de l'élément de menu ajoutée au panier."),
    )

    @property
    def item_total(self):
        if (
            self.quantity is None
            or self.menu_item is None
            or self.menu_item.price is None
        ):
            return Decimal("0.00")
        return self.quantity * self.menu_item.price

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

    class Meta:
        verbose_name = _("Article du panier")
        verbose_name_plural = _("Articles du panier")
        ordering = ["menu_item"]
        unique_together = ("cart", "menu_item")
        indexes = [models.Index(fields=["cart", "menu_item"])]
