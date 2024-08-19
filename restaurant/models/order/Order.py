from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from account.models.CustomUser import CustomUser
from restaurant.models.restaurant import MenuItem, Restaurant
from common.models.TimeStampedModel import TimeStampedModel


class Order(TimeStampedModel):
    """
    Entité représentant une commande.

    Cette entité contient les informations relatives à une commande passée
    dans un restaurant, y compris le type de commande (sur place ou à emporter),
    le client, le staff responsable, et le statut de la commande.
    """

    ORDER_TYPE_CHOICES = [
        ("dine_in", _("Sur place")),
        ("takeaway", _("À emporter")),
    ]
    ORDER_STATUS_CHOICES = [
        ("pending", _("En attente")),
        ("accepted", _("Acceptée")),
        ("preparing", _("En préparation")),
        ("ready", _("Prête")),
        ("delivered", _("Livré")),
        ("canceled", _("Annulée")),
    ]

    order_type = models.CharField(
        max_length=10,
        choices=ORDER_TYPE_CHOICES,
        verbose_name=_("Type de commande"),
        help_text=_("Indique si la commande est sur place ou à emporter."),
    )
    client = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
        verbose_name=_("Client"),
        help_text=_(
            "Le client qui a passé la commande. Peut être vide si la commande est sur place sans compte."
        ),
    )
    order_number = models.IntegerField(
        unique=True,
        verbose_name=_("Numéro de commande"),
        help_text=_("Le numéro unique de la commande."),
    )
    client_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Nom du client (si sans compte)"),
        help_text=_("Nom du client pour une commande sur place sans compte."),
    )
    table_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name=_("Numéro de table"),
        help_text=_("Numéro de table pour une commande sur place."),
    )
    staff = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="staff_orders",
        verbose_name=_("Staff"),
        help_text=_("Le membre du personnel responsable de la commande."),
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name=_("Restaurant"),
        help_text=_("Le restaurant où la commande a été passée."),
    )
    items = models.ManyToManyField(
        MenuItem, through="OrderItem", related_name="orders", verbose_name=_("Articles")
    )
    status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        verbose_name=_("Statut de la commande"),
        help_text=_("Le statut actuel de la commande."),
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Montant total"),
        help_text=_("Le montant total de la commande."),
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Note"),
        help_text=_("Une note optionnelle concernant la commande."),
    )

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.all().order_by("order_number").last()
            if last_order:
                self.order_number = last_order.order_number + 1
            else:
                self.order_number = 1
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return (
            f"Order {self.id} | Commande #{self.order_number} - {self.staff.username}"
        )

    def clean(self):
        if self.order_type == "takeaway" and not self.client:
            raise ValidationError(
                _("Une commande à emporter doit avoir un client enregistré.")
            )
        if self.order_type == "dine_in" and not (self.client_name or self.table_number):
            raise ValidationError(
                _(
                    "Une commande sur place doit avoir un nom de client ou un numéro de table."
                )
            )

    class Meta:
        verbose_name = _("Commande")
        verbose_name_plural = _("Commandes")
        ordering = ["-created_at"]
