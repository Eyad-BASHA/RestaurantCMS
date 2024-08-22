from rest_framework import generics, status, views, serializers
from rest_framework.response import Response
from restaurant.models.payment import Payment, PaymentMethod
from restaurant.serializers.payment_serializer import (
    PaymentMethodSerializer,
    PaymentSerializer,
)
import stripe
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

stripe.api_key = settings.STRIPE_SECRET_KEY


# Liste et création des méthodes de paiement
class PaymentMethodListCreateView(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]


# Détails et mise à jour d'une méthode de paiement
class PaymentMethodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated]


# Liste des paiements
class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


# Création d'un paiement
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Vérifiez que le montant est valide avant de sauvegarder
        order = serializer.validated_data.get("order")
        if serializer.validated_data["amount"] > order.total_amount:
            raise serializers.ValidationError(
                "Le montant du paiement dépasse le montant de la commande."
            )
        serializer.save()


# Détails et mise à jour d'un paiement
class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


# Vue pour gérer les paiements Stripe
class StripePaymentView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            order_id = request.data.get("order_id")
            order = Payment.objects.get(id=order_id)
            if order.status != "pending":
                return Response(
                    {"error": "Commande déjà payée ou annulée."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            intent = stripe.PaymentIntent.create(
                amount=int(order.amount * 100),  # Convertir en centimes
                currency="eur",
                metadata={"order_id": order.id},
            )
            return Response(
                {"client_secret": intent["client_secret"]}, status=status.HTTP_200_OK
            )

        except Payment.DoesNotExist:
            return Response(
                {"error": "Commande introuvable."}, status=status.HTTP_404_NOT_FOUND
            )

        except stripe.error.StripeError as e:
            return Response(
                {"error": f"Erreur Stripe: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": f"Une erreur est survenue: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
