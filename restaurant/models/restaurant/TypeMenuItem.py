from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models.TimeStampedModel import TimeStampedModel


class TypeMenuItem(TimeStampedModel):
    """
    Type d'élément de menu.

    Cette entité représente les différents types d'éléments qui peuvent figurer
    dans un menu, comme les plats, les boissons, les desserts, etc.
    """

    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom"),
        help_text=_(
            "Le nom du type d'élément de menu. Possibilités : Plat, Boisson, Dessert, Entrée, Accompagnement, etc."
        ),
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=_("Slug"),
        help_text=_("L'identifiant unique du type d'élément de menu."),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description du type d'élément de menu."),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Type d'élément de menu")
        verbose_name_plural = _("Types d'éléments de menu")
        ordering = ["name"]
        unique_together = ("name",)
        indexes = [models.Index(fields=["name"])]
