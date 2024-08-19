from django.db import models
from django.utils.translation import gettext_lazy as _

from restaurant.models.order import Order
from restaurant.models.payment.PaymentMethod import PaymentMethod
from common.models.TimeStampedModel import TimeStampedModel


class Payment(TimeStampedModel):
    """
    Paiement.

    Cette entité représente un paiement effectué pour une commande spécifique,
    incluant le montant payé, la méthode de paiement utilisée, et le statut du paiement.
    """

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_("Commande"),
        help_text=_("La commande associée à ce paiement."),
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Montant"),
        help_text=_("Le montant total payé pour la commande."),
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        verbose_name=_("Méthode de paiement"),
        help_text=_("La méthode utilisée pour effectuer le paiement."),
    )
    status = models.CharField(
        max_length=50,
        verbose_name=_("Statut"),
        help_text=_(
            "Le statut actuel du paiement, par exemple 'Payé', 'En attente', etc."
        ),
    )

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"

    class Meta:
        verbose_name = _("Paiement")
        verbose_name_plural = _("Paiements")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
