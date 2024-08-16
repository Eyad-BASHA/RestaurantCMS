from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class CategoryRestaurant(MPTTModel):
    """
    Catégorie pour les restaurants.

    Cette entité représente une catégorie pour organiser les restaurants,
    permettant de les classer en catégories et sous-catégories.
    """

    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom"),
        help_text=_("Le nom de la catégorie de restaurant."),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_("Slug"),
        help_text=_(
            "Un identifiant unique dérivé du nom de la catégorie, utilisé dans les URL."
        ),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description de la catégorie de restaurant."),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("Catégorie parente"),
        help_text=_("La catégorie parente si cette catégorie est une sous-catégorie."),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
        help_text=_("Indique si la catégorie est active ou non."),
    )
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Catégorie de restaurant")
        verbose_name_plural = _("Catégories de restaurants")
        ordering = ["name"]
        unique_together = ("name", "slug")
        # index_together = ("name", "slug")
