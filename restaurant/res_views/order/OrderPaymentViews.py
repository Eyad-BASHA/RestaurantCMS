import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from restaurant.models.order import Order
from restaurant.models.payment import Payment
from restaurant.serializers.payment_serializer import PaymentSerializer
from rest_framework import generics, permissions
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            order_id = request.data.get("order_id")
            order = Order.objects.get(id=order_id)
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_amount * 100),  # Convertir en centimes
                currency="eur",
                metadata={"order_id": order.id},
            )
            return Response({"client_secret": intent["client_secret"]})

        except Order.DoesNotExist:
            return Response(
                {"error": "Commande introuvable."}, status=status.HTTP_404_NOT_FOUND
            )

        except stripe.error.StripeError as e:
            return Response(
                {"error": "Erreur Stripe: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": "Une erreur est survenue: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RecordPaymentView(generics.CreateAPIView):
    """
    Vue pour enregistrer un paiement effectué en restaurant.
    """

    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        payment.order.status = "paid"
        payment.order.save()


class SplitPaymentView(APIView):
    """
    Vue pour diviser le paiement d'une commande en plusieurs parties.
    """

    def post(self, request, *args, **kwargs):
        order_id = request.data.get("order_id")
        amounts = request.data.get("amounts")
        order = Order.objects.get(id=order_id)

        total_paid = 0
        for amount in amounts:
            Payment.objects.create(order=order, amount=amount, status="paid")
            total_paid += amount

        if total_paid >= order.total_amount:
            order.status = "paid"
            order.save()

        return Response({"status": "Payments recorded successfully."})
