from django.db import models
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class CategoryMenuItem(MPTTModel):
    """
    Catégorie pour les éléments du menu.

    Cette entité représente une catégorie pour les produits ou les éléments de menu.
    Elle peut être utilisée pour organiser les éléments dans une hiérarchie (par exemple,
    les catégories et sous-catégories).
    """

    name = models.CharField(
        max_length=255, verbose_name=_("Nom"), help_text=_("Le nom de la catégorie.")
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
        max_length=255,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description de la catégorie."),
    )
    cat_image = models.ImageField(
        upload_to="photos/category",
        blank=True,
        verbose_name=_("Image de la catégorie"),
        help_text=_("Une image représentative de la catégorie."),
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

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Catégorie d'article de menu")
        verbose_name_plural = _("Catégories d'articles de menu")
        ordering = ["name"]
        unique_together = ("name", "slug")
        # index_together = ("name", "slug")

    def __str__(self):
        return self.name
