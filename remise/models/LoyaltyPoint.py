from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser, Profile
from remise.models import LoyaltyProgram


class LoyaltyPoint(models.Model):
    """
    Entité représentant les points de fidélité d'un utilisateur.

    Les points sont attribués en fonction des achats effectués par l'utilisateur.
    """

    client = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="loyalty_points",
        verbose_name=_("Profil"),
        help_text=_("Le profil utilisateur associé à ces points de fidélité."),
    )
    program = models.ForeignKey(
        LoyaltyProgram,
        on_delete=models.CASCADE,
        related_name="loyalty_points",
        verbose_name=_("Programme de fidélité"),
        help_text=_("Le programme de fidélité dans lequel les points sont accumulés."),
    )
    points = models.IntegerField(
        verbose_name=_("Points"), help_text=_("Le nombre de points accumulés.")
    )
    earned_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date d'acquisition"),
        help_text=_("La date à laquelle les points ont été acquis."),
    )
    expiry_date = models.DateTimeField(
        verbose_name=_("Date d'expiration"),
        help_text=_("La date à laquelle les points expirent."),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.client.user.username} - {self.points} points"

    class Meta:
        verbose_name = _("Point de fidélité")
        verbose_name_plural = _("Points de fidélité")
        ordering = ["-earned_date"]
