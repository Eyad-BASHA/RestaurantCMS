from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from blog.models import Tag
from common.models import TimeStampedModel



class Category(TimeStampedModel):
    """
    Entité représentant une catégorie pour les articles de blog.
    """

    name = models.CharField(max_length=50, unique=True, verbose_name=_("Nom de la catégorie"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Catégorie")
        verbose_name_plural = _("Catégories")
        ordering = ["name"]
        get_latest_by = "name"