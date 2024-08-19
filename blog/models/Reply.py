from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from common.models import TimeStampedModel
from blog.models import Article, Comment


class Reply(TimeStampedModel):
    """
    Entité représentant une réponse à un commentaire.
    """

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name=_("Commentaire"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="replies",
        limit_choices_to={
            "roles__name__in": ["admin", "moderateur"]
        }, 
        verbose_name=_("Auteur"),
    )
    content = models.TextField(verbose_name=_("Repondre"))

    def __str__(self):
        return f"Réponse par {self.author.username} sur commentaire {self.comment.id}"

    class Meta:
        verbose_name = _("Réponse")
        verbose_name_plural = _("Réponses")
        ordering = ["created_at"]
