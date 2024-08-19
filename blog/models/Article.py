from datetime import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import CustomUser
from blog.models import Category
from common.models import TimeStampedModel


class Article(TimeStampedModel):
    """
    Entité représentant un article de blog.
    """

    STATUS_CHOICES = [
        ("draft", "Brouillon"),
        ("published", "Publié"),
        ("archived", "Archivé"),
    ]

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles",
        verbose_name=_("Catégorie"),
    )
    title = models.CharField(max_length=255, verbose_name=_("Titre"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    content = models.TextField(verbose_name=_("Contenu"))
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="articles",
        limit_choices_to={"roles__name__in": ["admin", "moderateur"]},
        verbose_name=_("Auteur"),
    )
    tags = models.ManyToManyField(
        "Tag", related_name="articles", verbose_name=_("Tags")
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
        verbose_name=_("Statut"),
    )
    published_at = models.DateTimeField(
        blank=True, null=True, verbose_name=_("Date de publication")
    )

    def save(self, *args, **kwargs):
        # Si l'article est publié et que published_at est vide, le remplir avec la date actuelle
        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-published_at"]
        get_latest_by = "published_at"
