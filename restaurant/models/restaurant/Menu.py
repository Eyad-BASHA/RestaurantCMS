from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from restaurant.models.restaurant import Restaurant
from ..common import TimeStampedModel


class Menu(TimeStampedModel):
    """
    Menu pour un restaurant.

    Cette entité représente un menu pour un restaurant spécifique,
    permettant d'organiser les plats et les articles offerts par le restaurant.
    """

    restaurant = models.ForeignKey(
        "restaurant.Restaurant",
        on_delete=models.CASCADE,
        verbose_name=_("Restaurant"),
        help_text=_("Le restaurant auquel ce menu est associé."),
    )
    name = models.CharField(
        max_length=255, verbose_name=_("Nom"), help_text=_("Le nom du menu.")
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_("Slug"),
        help_text=_(
            "Un identifiant unique dérivé du nom du menu, utilisé dans les URL."
        ),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Une brève description du menu."),
    )
    menu_photo = models.ImageField(
        upload_to="photos/menu",
        blank=True,
        null=True,
        default="photos/profile/user_picture/user_img.png",
        verbose_name=_("Photo pour Menu"),
        help_text=_("Une photo représentant le menu."),
    )

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"

    # REDIMENSIONNER LA PHOTO
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        img = Image.open(self.menu_photo.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.menu_photo.path)

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        unique_together = ("name", "restaurant")
        indexes = [models.Index(fields=["name", "restaurant"])]
