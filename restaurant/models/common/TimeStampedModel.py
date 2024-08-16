from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    Modèle abstrait avec gestion automatique des champs created_at et updated_at.

    Ce modèle peut être hérité par d'autres modèles pour ajouter automatiquement
    des champs de suivi de la création et de la mise à jour.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date de création"),
        help_text=_("Date et heure de la création de l'enregistrement."),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Date de mise à jour"),
        help_text=_("Date et heure de la dernière mise à jour de l'enregistrement."),
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]
