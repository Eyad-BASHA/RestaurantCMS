from django.db import models
from django.utils.translation import gettext_lazy as _

from restaurant.models.restaurant.Menu import Menu
from restaurant.models.restaurant.TypeMenuItem import TypeMenuItem
from restaurant.models.restaurant.CategoryMenuItem import CategoryMenuItem
from ..common import TimeStampedModel


class MenuItem(TimeStampedModel):
    """
    Élément de menu pour un restaurant.

    Cette entité représente un article ou un plat dans un menu spécifique
    d'un restaurant, avec des détails tels que le prix, la catégorie, et le type.
    """

    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name=_("Menu"),
        help_text=_("Le menu auquel cet élément est associé."),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom"),
        help_text=_("Le nom de l'élément de menu."),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_("Slug"),
        help_text=_(
            "Un identifiant unique dérivé du nom de l'élément, utilisé dans les URL."
        ),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description de l'élément de menu."),
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name=_("Prix"),
        help_text=_("Le prix de l'élément de menu."),
    )
    category = models.ForeignKey(
        CategoryMenuItem,
        on_delete=models.CASCADE,
        verbose_name=_("Catégorie"),
        help_text=_("La catégorie à laquelle appartient cet élément de menu."),
    )
    type = models.ForeignKey(
        TypeMenuItem,
        on_delete=models.CASCADE,
        verbose_name=_("Type"),
        help_text=_(
            "Le type de cet élément de menu (par exemple, plat, boisson, etc.)."
        ),
    )
    is_from_kitchen = models.BooleanField(
        default=True,
        verbose_name=_("Provenant de la cuisine"),
        help_text=_("Indique si cet élément est préparé en cuisine ou au bar."),
    )

    def __str__(self):
        return f"{self.name} | {self.category.name}"

    class Meta:
        verbose_name = _("Élément de menu")
        verbose_name_plural = _("Éléments de menu")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("name", "menu")
        indexes = [models.Index(fields=["name", "menu"])]
