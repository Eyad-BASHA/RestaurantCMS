from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from account.models import CustomUser
from restaurant.models.reservation import Availability
from restaurant.models.restaurant import Restaurant
from common.models.TimeStampedModel import TimeStampedModel


class Reservation(TimeStampedModel):
    """
    Réservation de table.

    Cette entité représente une réservation de table effectuée par un utilisateur dans un restaurant,
    incluant le nombre de personnes, la date de la réservation, et toute demande spéciale.
    """

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_("Utilisateur"),
        help_text=_("L'utilisateur qui a effectué la réservation."),
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name=_("Restaurant"),
        help_text=_("Le restaurant où la réservation est effectuée."),
    )
    reservation_date = models.DateField(
        verbose_name=_("Date de réservation"), 
        help_text=_("La date de la réservation.")
    )
    start_time = models.TimeField(
        verbose_name=_("Heure de début"),
        help_text=_("L'heure de début de la réservation."),
    )
    end_time = models.TimeField(
        verbose_name=_("Heure de fin"),
        help_text=_("L'heure de fin de la réservation."),
    )
    number_of_people = models.PositiveIntegerField(
        verbose_name=_("Nombre de personnes"),
        help_text=_("Le nombre de personnes pour cette réservation."),
    )
    special_request = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Demande spéciale"),
        help_text=_("Toute demande spéciale pour cette réservation."),
    )
    is_confirmed = models.BooleanField(
        default=False,
        verbose_name=_("Est confirmé"),
        help_text=_("Indique si la réservation est confirm")
    )
    tables = models.ManyToManyField(
        "restaurant.Availability",
        verbose_name=_("Tables réservées"),
        help_text=_("Les tables réservées pour cette réservation."),
    )

    def __str__(self):
        return f"Réservation pour {self.number_of_people} personnes au {self.restaurant.name}"

    class Meta:
        verbose_name = _("Réservation")
        verbose_name_plural = _("Réservations")
        ordering = ["-reservation_date"]

    def clean(self):
        """
        Valide les données avant la sauvegarde.
        """
        if not self.reservation_date:
            raise ValidationError(_("La date de réservation est obligatoire."))

        if self.reservation_date < timezone.now().date():
            raise ValidationError(
                _("La date de la réservation ne peut pas être dans le passé.")
            )

        if not self.start_time:
            raise ValidationError(_("L'heure de début est obligatoire."))

        if not self.end_time:
            raise ValidationError(_("L'heure de fin est obligatoire."))

        if self.start_time > self.end_time:
            raise ValidationError(_("L'heure de début doit être avant l'heure de fin."))

        # for table in self.tables.all():
        #     # Vérification des disponibilités
        #     if table.available_slots < self.number_of_people:
        #         raise ValidationError(
        #             _("Pas assez de places disponibles pour la table {}.").format(
        #                 table.table_number
        #             )
        #         )

    def save(self, *args, **kwargs):
        """
        Sauvegarde la réservation et met à jour les tables associées.
        """
        if self.pk is None:
            # Première sauvegarde pour obtenir un ID
            super().save(*args, **kwargs)

        # Effectuer les validations personnalisées
        self.clean() 
        super().save(*args, **kwargs)

        # Effectuer les validations personnalisées après la première sauvegarde
        for table in self.tables.all():
            # Vérification des disponibilités
            if table.available_slots < self.number_of_people:
                raise ValidationError(
                    _("Pas assez de places disponibles pour la table {}.").format(
                        table.table_number
                    )
                )

        # Après la validation, sauvegarder les tables associées
        super().save(*args, **kwargs)

        # Mise à jour des disponibilités
        for table in self.tables.all():
            table.available_slots -= self.number_of_people
            table.save()

    def cancel_reservation(self):
        for table in self.tables.all():
            table.available_slots += self.number_of_people
            table.save()
        self.delete()
