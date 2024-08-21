from django.db import models
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant import Restaurant
from common.models import TimeStampedModel


class Availability(TimeStampedModel):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, verbose_name=_("Restaurant")
    )
    date = models.DateField(verbose_name=_("Date"))
    start_time = models.TimeField(verbose_name=_("Heure de début"))
    end_time = models.TimeField(verbose_name=_("Heure de fin"))
    table_number = models.CharField(max_length=10, verbose_name=_("Numéro de table"))
    available_slots = models.PositiveIntegerField(
        verbose_name=_("Nombre de places disponibles")
    )

    class Meta:
        verbose_name = _("Disponibilité")
        verbose_name_plural = _("Disponibilités")
        unique_together = ("restaurant", "date", "start_time")

    def __str__(self):
        return f"{self.restaurant.name} - Table {self.table_number} - {self.date} {self.start_time}-{self.end_time} ({self.available_slots} places)"
