from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from common.models import TimeStampedModel
from blog.models import Comment


class LikeComment(TimeStampedModel):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="liked_comments",
        verbose_name=_("Auteur"),
        help_text=_("L'utilisateur qui a aimé le commentaire."),
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="likes",
        verbose_name=_("Commentaire"),
        help_text=_("Le commentaire qui a été aimé."),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} likes comment {self.comment.id}"
