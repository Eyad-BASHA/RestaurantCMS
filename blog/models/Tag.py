from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampedModel


class Tag(TimeStampedModel):
    """
    Entité représentant un tag pour les articles de blog.
    """

    name = models.CharField(max_length=50, unique=True, verbose_name=_("Nom du tag"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ["name"]
        get_latest_by = "name"
