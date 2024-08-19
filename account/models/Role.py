from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models.TimeStampedModel import *


class Role(TimeStampedModel):
    """
    Modèle représentant un rôle utilisateur.

    Ce modèle définit différents rôles qui peuvent être attribués aux utilisateurs du système,
    tels que client, modérateur, et administrateur.
    """

    ROLE_NAME_CHOICES = [
        ("client", _("Client")),
        ("moderateur", _("Modérateur")),
        ("admin", _("Admin")),
    ]

    name = models.CharField(
        max_length=10,
        choices=ROLE_NAME_CHOICES,
        unique=True,
        verbose_name=_("Nom du rôle"),
        help_text=_("Le nom du rôle, par exemple, client, modérateur, ou admin."),
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Une description optionnelle du rôle."),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Rôle")
        verbose_name_plural = _("Rôles")
        ordering = ["name"]
