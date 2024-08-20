from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampedModel
from blog.models import Article
from PIL import Image

class ArticlePhoto(TimeStampedModel):
    """
    Entité représentant une photo pour un article de blog.
    """

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="photos", verbose_name=_("Article"))
    image = models.ImageField(upload_to="articles/photos", verbose_name=_("Image"))
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Texte alternatif"),
        help_text=_("Texte alternatif pour l'image, utilisé pour l'accessibilité."),
    )

    def __str__(self):
        return f"Image pour {self.article.title}"

        # REDIMENSIONNER LA PHOTO

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = _("Photo d'article")
        verbose_name_plural = _("Photos d'articles")
        ordering = ["-created_at"]
        get_latest_by = "created_at"
