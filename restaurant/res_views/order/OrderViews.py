from rest_framework import generics, permissions
from restaurant.models.order import Order, OrderItem, Cart
from restaurant.serializers.order_serializer import OrderSerializer, OrderItemSerializer
from account.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
            if cart.cart_items.count() == 0:
                return Response(
                    {"error": "Votre panier est vide."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            order_data = {
                "client": user.id,
                "order_type": "takeaway",
                "status": "pending",
                "restaurant": cart.restaurant.id,
            }

            serializer = self.get_serializer(data=order_data)
            serializer.is_valid(raise_exception=True)
            with transaction.atomic():
                order = serializer.save()

                for cart_item in cart.cart_items.all():
                    OrderItem.objects.create(
                        order=order,
                        menu_item=cart_item.menu_item,
                        quantity=cart_item.quantity,
                        item_total=cart_item.item_total,
                    )
                order.update_total_amount()
                cart.clear_cart()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Cart.DoesNotExist:
            return Response(
                {"error": "Panier introuvable."}, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CreateOrderForClientView(generics.CreateAPIView):
    """
    Vue pour que le staff crée une commande pour un client en restaurant.
    """

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Le staff doit être authentifié

    def create(self, request, *args, **kwargs):
        staff = request.user
        client_name = request.data.get("client_name", None)
        table_number = request.data.get("table_number", None)
        order_type = request.data.get("order_type", "dine_in")

        if not client_name and order_type == "dine_in":
            return Response(
                {"error": "Le nom du client ou le numéro de table est requis."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_data = {
            "staff": staff.id,
            "client_name": client_name,
            "table_number": table_number,
            "order_type": order_type,
            "status": "pending",
            "restaurant": request.data.get("restaurant"),
        }

        serializer = self.get_serializer(data=order_data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListClientOrdersView(generics.ListAPIView):
    """
    Vue pour afficher les commandes d'un client.
    """

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(client=self.request.user).order_by("-created_at")


class ListRestaurantOrdersView(generics.ListAPIView):
    """
    Vue pour afficher les commandes pour le staff.
    """

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            restaurant=self.request.user.restaurants.first()
        ).order_by("-created_at")


class UpdateOrderView(generics.UpdateAPIView):
    """
    Vue pour modifier une commande si elle est en attente ou acceptée.
    """

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(status__in=["pending", "accepted"])

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.update_total_amount()  
