from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import Profile
from common.models import TimeStampedModel
from remise.models import Discount
from restaurant.models.order import Order


class UsedDiscount(TimeStampedModel):
    """
    Entité représentant l'utilisation d'une remise par un utilisateur.

    Cette entité permet de suivre quelles remises ont été utilisées et dans quelles commandes.
    """

    client = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="used_discounts",
        verbose_name=_("Profil"),
        help_text=_("Le profil utilisateur ayant utilisé la remise."),
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        related_name="used_discounts",
        verbose_name=_("Remise"),
        help_text=_("La remise utilisée."),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="used_discounts",
        verbose_name=_("Commande"),
        help_text=_("La commande dans laquelle la remise a été appliquée."),
    )
    used_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date d'utilisation"),
        help_text=_("La date et l'heure auxquelles la remise a été utilisée."),
    )

    def __str__(self):
        return f"Remise {self.discount.code} utilisée par {self.client.user.username} sur la commande {self.order.id}"

    class Meta:
        verbose_name = _("Remise utilisée")
        verbose_name_plural = _("Remises utilisées")
        ordering = ["-used_at"]
