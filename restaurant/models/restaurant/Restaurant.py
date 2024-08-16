from django.db import models
from django.utils.translation import gettext_lazy as _
from ..common import TimeStampedModel


class Restaurant(TimeStampedModel):
    """
    Entité représentant un restaurant.

    Cette entité contient les informations principales sur un restaurant,
    y compris son nom, sa description, et son adresse principale.
    """

    name = models.CharField(
        max_length=255,
        verbose_name=_("Nom du restaurant"),
        help_text=_("Le nom du restaurant."),
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_("Slug"),
        help_text=_("Un identifiant unique dérivé du nom, utilisé dans les URLs."),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description du restaurant."),
    )
    addresses = models.ForeignKey(
        "restaurant.AddressRestaurant",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="main_address",
        verbose_name=_("Adresse principale"),
        help_text=_("L'adresse principale du restaurant."),
    )
    logo = models.ImageField(
        upload_to="restaurant/logos/",
        blank=True,
        null=True,
        verbose_name=_("Logo"),
        help_text=_("Le logo du restaurant."),
    )

    def __str__(self):
        return f"{self.name} | {self.addresses if self.addresses else 'Pas d adresse'}"

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("name",)
        indexes = [models.Index(fields=["name"])]
