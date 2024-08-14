"""Entity Role for users"""

from django.db import models


class Role(models.Model):
    """Role model."""

    ROLE_NAME_CHOICES = [
        ("client", "Client"),
        ("moderateur", "Moderateur"),
        ("admin", "Admin"),
    ]
    # user = models.ForeignKey("account.CustomUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=10, choices=ROLE_NAME_CHOICES, unique=True)
    description = models.TextField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
