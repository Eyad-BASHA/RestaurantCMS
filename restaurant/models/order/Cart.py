from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from account.models.CustomUser import CustomUser
from restaurant.models.restaurant import MenuItem
from common.models.TimeStampedModel import TimeStampedModel


class Cart(TimeStampedModel):
    """
    Panier.

    Cette entité représente le panier d'un utilisateur, contenant les éléments
    de menu ajoutés pour un éventuel achat.
    """

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_("Utilisateur"),
        help_text=_("L'utilisateur propriétaire de ce panier."),
    )
    items = models.ManyToManyField(
        MenuItem,
        through="CartItem",
        verbose_name=_("Articles"),
        help_text=_("Les articles ajoutés au panier par l'utilisateur."),
    )

    @property
    def total_price(self):
        return sum(
            item.menu_item.price * item.quantity for item in self.cart_items.all()
        )

    # def update_total_price(self):
    #     """Met à jour le prix total du panier."""
    #     self.total_price = self.calculate_total_price()
    #     self.save(update_fields=["total_price"])

    # def calculate_total_price(self):
    #     return sum(
    #         item.menu_item.price * item.quantity for item in self.cart_items.all()
    #     )

    def clear_cart(self):
        """Vide le panier."""
        self.cart_items.all().delete()

    def __str__(self):
        return f"Panier pour {self.user.username}"

    def clean(self):
        if not self.user:
            raise ValidationError(_("Un panier doit être associé à un utilisateur."))

    class Meta:
        verbose_name = _("Panier")
        verbose_name_plural = _("Paniers")
        ordering = ["-created_at"]
