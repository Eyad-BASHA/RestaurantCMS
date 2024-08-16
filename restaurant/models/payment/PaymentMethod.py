from django.db import models
from django.utils.translation import gettext_lazy as _
from ..common import TimeStampedModel


class PaymentMethod(TimeStampedModel):
    """
    Méthode de paiement.

    Cette entité représente une méthode de paiement disponible pour les clients,
    telle que carte de crédit, PayPal, ou autre.
    """

    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom de la méthode"),
        help_text=_(
            "Le nom de la méthode de paiement, par exemple, 'Carte de Crédit'."
        ),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une description facultative de la méthode de paiement."),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Méthode de paiement")
        verbose_name_plural = _("Méthodes de paiement")
        ordering = ["name"]
