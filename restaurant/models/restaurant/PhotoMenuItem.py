from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from restaurant.models.restaurant import MenuItem
from common.models.TimeStampedModel import TimeStampedModel


class PhotoMenuItem(TimeStampedModel):
    """
    Photo pour un élément de menu.

    Cette entité permet d'associer plusieurs photos à un élément de menu spécifique,
    permettant ainsi de mieux illustrer les produits proposés.
    """

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE,
        related_name="photos",
        verbose_name=_("Élément de menu"),
        help_text=_("L'élément de menu auquel cette photo est associée."),
    )
    photo = models.ImageField(
        upload_to="photos/menu_items",
        verbose_name=_("Photo"),
        help_text=_("La photo de l'élément de menu."),
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Texte alternatif"),
        help_text=_("Texte alternatif pour l'image, utilisé pour l'accessibilité."),
    )

    def __str__(self):
        return f"Photo for {self.menu_item.name}"

    # REDIMENSIONNER LA PHOTO
    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        img = Image.open(self.photo.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    class Meta:
        verbose_name = _("Photo d'élément de menu")
        verbose_name_plural = _("Photos d'éléments de menu")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
        indexes = [models.Index(fields=["menu_item"])]
