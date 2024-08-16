from django.db import models
from django.utils.translation import gettext_lazy as _


class Discount(models.Model):
    """
    Entité représentant une remise.

    Les remises peuvent être appliquées sous forme de pourcentage ou de montant fixe.
    """

    DISCOUNT_TYPE_CHOICES = [
        ("percentage", _("Pourcentage")),
        ("fixed", _("Montant fixe")),
    ]

    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("Code de remise"),
        help_text=_("Le code que l'utilisateur doit saisir pour obtenir la remise."),
    )
    discount_type = models.CharField(
        max_length=20,
        choices=DISCOUNT_TYPE_CHOICES,
        verbose_name=_("Type de remise"),
        help_text=_("Le type de remise, soit en pourcentage, soit en montant fixe."),
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Valeur de la remise"),
        help_text=_(
            "La valeur de la remise. Si c'est un pourcentage, entrez un nombre entre 0 et 100."
        ),
    )
    min_order_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Montant minimum de commande"),
        help_text=_(
            "Le montant minimum de la commande pour que la remise soit applicable."
        ),
        null=True,
        blank=True,
    )
    start_date = models.DateTimeField(
        verbose_name=_("Date de début"),
        help_text=_("La date et l'heure à partir desquelles la remise est active."),
    )
    end_date = models.DateTimeField(
        verbose_name=_("Date de fin"),
        help_text=_(
            "La date et l'heure après lesquelles la remise n'est plus applicable."
        ),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indique si la remise est actuellement active."),
    )

    def __str__(self):
        return f"{self.code} - {self.get_discount_type_display()}"

    class Meta:
        verbose_name = _("Remise")
        verbose_name_plural = _("Remises")
        ordering = ["-start_date"]
