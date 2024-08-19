from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from common.models import TimeStampedModel
from blog.models import Article


class LikeArticle(TimeStampedModel):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="liked_articles",
        verbose_name=_("Auteur"),
        help_text=_("L'utilisateur qui a aimé l'article."),
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name=_("Article"),
        help_text=_("L'article qui a été aimé."),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} likes {self.article.title}"
