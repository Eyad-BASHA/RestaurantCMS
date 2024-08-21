from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TimeStampedModel


class LoyaltyProgram(TimeStampedModel):
    """
    Entité représentant un programme de fidélité.

    Les clients accumulent des points à chaque achat, qui peuvent être échangés contre des récompenses.
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("Nom du programme"),
        help_text=_("Le nom du programme de fidélité."),
    )
    points_per_euro = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Points par euro dépensé"),
        help_text=_("Nombre de points attribués pour chaque euro dépensé."),
    )
    start_date = models.DateTimeField(
        verbose_name=_("Date de début"),
        help_text=_("La date et l'heure à partir desquelles le programme est actif."),
    )
    end_date = models.DateTimeField(
        verbose_name=_("Date de fin"),
        help_text=_(
            "La date et l'heure après lesquelles le programme n'est plus actif."
        ),
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indique si le programme est actuellement actif."),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Programme de fidélité")
        verbose_name_plural = _("Programmes de fidélité")
        ordering = ["-start_date"]
