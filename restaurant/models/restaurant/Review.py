from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser
from restaurant.models.restaurant import MenuItem
from common.models.TimeStampedModel import TimeStampedModel


class Review(TimeStampedModel):
    """
    Entité combinant la note et l'avis pour un élément de menu après un achat.

    Cette entité permet aux utilisateurs de laisser une note (rating) et un commentaire (review)
    sur un élément de menu après l'avoir acheté.
    """

    RATING_CHOICES = [
        (1, _("1 - Très mauvais")),
        (2, _("2 - Mauvais")),
        (3, _("3 - Correct")),
        (4, _("4 - Bon")),
        (5, _("5 - Excellent")),
    ]

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Élément de menu"),
        help_text=_("L'élément de menu sur lequel l'utilisateur laisse un avis."),
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Utilisateur"),
        help_text=_("L'utilisateur qui laisse la note et l'avis."),
    )
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Note"),
        help_text=_("La note donnée à l'élément de menu, sur une échelle de 1 à 5."),
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Commentaire"),
        help_text=_("Un commentaire optionnel sur l'élément de menu."),
    )

    def __str__(self):
        return f"Review by {self.user.username} for {self.menu_item.name} - {self.rating}/5"

    class Meta:
        verbose_name = _("Avis")
        verbose_name_plural = _("Avis")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("menu_item", "user")
        indexes = [models.Index(fields=["menu_item", "user"])]
