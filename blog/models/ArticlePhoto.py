from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import TimeStampedModel
from blog.models import Article

class ArticlePhoto(TimeStampedModel):
    """
    Entité représentant une photo pour un article de blog.
    """

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="photos", verbose_name=_("Article"))
    image = models.ImageField(upload_to="articles/photos", verbose_name=_("Image"))

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = _("Photo d'article")
        verbose_name_plural = _("Photos d'articles")
        ordering = ["-created_at"]
        get_latest_by = "created_at"