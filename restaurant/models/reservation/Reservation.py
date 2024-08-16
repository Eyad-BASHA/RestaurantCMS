from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser
from restaurant.models.restaurant import Restaurant
from ..common import TimeStampedModel


class Reservation(TimeStampedModel):
    """
    Réservation de table.

    Cette entité représente une réservation de table effectuée par un utilisateur dans un restaurant,
    incluant le nombre de personnes, la date de la réservation, et toute demande spéciale.
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_("Utilisateur"),
        help_text=_("L'utilisateur qui a effectué la réservation."),
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name=_("Restaurant"),
        help_text=_("Le restaurant où la réservation est effectuée."),
    )
    number_of_people = models.PositiveIntegerField(
        verbose_name=_("Nombre de personnes"),
        help_text=_("Le nombre de personnes pour cette réservation."),
    )
    reservation_date = models.DateTimeField(
        verbose_name=_("Date de la réservation"),
        help_text=_("La date et l'heure de la réservation."),
    )
    special_request = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Demande spéciale"),
        help_text=_("Toute demande spéciale pour cette réservation."),
    )

    def __str__(self):
        return f"Réservation pour {self.number_of_people} personnes au {self.restaurant.name}"

    class Meta:
        verbose_name = _("Réservation")
        verbose_name_plural = _("Réservations")
        ordering = ["-reservation_date"]
