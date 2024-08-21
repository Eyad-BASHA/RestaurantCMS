from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from restaurant.models.payment import Payment
from remise.models import Discount, LoyaltyPoint, LoyaltyProgram, UsedDiscount
from restaurant.models.order import Order
from restaurant.models.payment.PaymentMethod import PaymentMethod
from common.models.TimeStampedModel import TimeStampedModel


class Payment(TimeStampedModel):
    """
    Paiement.

    Cette entité représente un paiement effectué pour une commande spécifique,
    incluant le montant payé, la méthode de paiement utilisée, et le statut du paiement.
    """

    STATUS_CHOICES = [
        ("pending", _("En attente")),
        ("paid", _("Payé")),
        ("failed", _("Échoué")),
        ("refunded", _("Remboursé")),
        ("canceled", _("Annulé")),
    ]

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_("Commande"),
        help_text=_("La commande associée à ce paiement."),
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Montant"),
        help_text=_("Le montant total payé pour la commande."),
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Remise"),
        help_text=_("La remise appliquée à la commande."),
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        verbose_name=_("Méthode de paiement"),
        help_text=_("La méthode utilisée pour effectuer le paiement."),
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name=_("Statut"),
        help_text=_(
            "Le statut actuel du paiement, par exemple 'Payé', 'En attente', etc."
        ),
    )

    def save(self, *args, **kwargs):
        self.amount = round(self.amount, 2)
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.status}"

    class Meta:
        verbose_name = _("Paiement")
        verbose_name_plural = _("Paiements")
        ordering = ["-created_at"]
        get_latest_by = "created_at"

    def calculate_amount(self):
        """
        Calcule le montant total après application de la remise, le cas échéant.
        """
        total = self.order.total_amount
        if self.discount:
            if self.discount.discount_type == "percentage":
                total -= total * (self.discount.value / 100)
            elif self.discount.discount_type == "fixed":
                total -= self.discount.value
        return max(total, 0)

    @receiver(post_save, sender=Payment)
    def add_loyalty_points(sender, instance, created, **kwargs):
        if created and instance.status == "paid":
            try:
                program = LoyaltyProgram.objects.get(is_active=True)
            except LoyaltyProgram.DoesNotExist:
                program = None

            if program:
                points = int(instance.order.total_amount * program.points_per_euro)
                LoyaltyPoint.objects.create(
                    client=instance.order.client.profile,
                    program=program,
                    points=points,
                    expiry_date=program.end_date
                )


    @receiver(post_save, sender=Payment)
    def record_used_discount(sender, instance, created, **kwargs):
        if created and instance.status == "paid" and instance.discount:
            UsedDiscount.objects.create(
                client=instance.order.client.profile,
                discount=instance.discount,
                order=instance.order,
            )
