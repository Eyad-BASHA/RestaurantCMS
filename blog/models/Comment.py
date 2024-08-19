from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from common.models import TimeStampedModel
from blog.models import Article


class Comment(TimeStampedModel):
    """
    Entité représentant un commentaire sur un article de blog.
    """

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Article"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Auteur"),
    )
    content = models.TextField(verbose_name=_("Comment"))

    def __str__(self):
        return f"Commentaire par {self.author.username} sur {self.article.title}"

    class Meta:
        verbose_name = _("Commentaire")
        verbose_name_plural = _("Commentaires")
        ordering = ["created_at"]
        get_latest_by = "created_at"
