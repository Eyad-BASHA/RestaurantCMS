"""Address Entity for users"""

from django.db import models


class Address(models.Model):
    """Address entity, many addresses for one user."""

    ADDRESS_TYPE_CHOICES = [
        ("livraison", "LIVRAISON"),
        ("facturation", "FACTURATION"),
    ]

    address_type = models.CharField(max_length=255, choices=ADDRESS_TYPE_CHOICES)

    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.zip_code}, {self.city}, {self.country}"
