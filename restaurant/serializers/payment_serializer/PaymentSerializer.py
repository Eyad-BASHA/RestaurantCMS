from rest_framework import serializers
from restaurant.models.payment import Payment, PaymentMethod
from remise.serializers import DiscountSerializer
from restaurant.serializers import OrderSerializer


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    payment_method = serializers.SlugRelatedField(
        slug_field="name", queryset=PaymentMethod.objects.all()
    )
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    status = serializers.ChoiceField(choices=Payment.STATUS_CHOICES)

    class Meta:
        model = Payment
        fields = [
            "id",
            "order",
            "amount",
            "discount",
            "payment_method",
            "status",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        # Vérifier que l'ordre est dans un état qui permet de payer
        if validated_data["order"].status not in ["pending", "accepted"]:
            raise serializers.ValidationError(
                "L'ordre ne peut pas être payé dans son état actuel."
            )

        payment = Payment(**validated_data)
        payment.amount = payment.calculate_amount()
        payment.save()
        return payment
