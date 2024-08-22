from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import ValidationError
from remise.models import Discount, LoyaltyPoint, LoyaltyProgram, UsedDiscount
from remise.serializers import (
    DiscountSerializer,
    LoyaltyPointSerializer,
    LoyaltyProgramSerializer,
    UsedDiscountSerializer,
)


# Custom Permissions
class IsAdminOrModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.has_perm("remise.manage_discount")


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.roles.filter(name="client").exists()
        )


class DiscountViewSet(viewsets.ModelViewSet):
    """
    Vue pour gérer les remises.
    """

    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated, IsAdminOrModerator]

    def get_queryset(self):
        # Filtrer les remises actives
        return self.queryset.filter(is_active=True)

    def perform_create(self, serializer):
        # Vérifier si une remise avec le même code existe déjà
        if Discount.objects.filter(code=serializer.validated_data["code"]).exists():
            raise ValidationError("Une remise avec ce code existe déjà.")
        serializer.save()


class LoyaltyPointViewSet(viewsets.ModelViewSet):
    """
    Vue pour gérer les points de fidélité.
    """

    queryset = LoyaltyPoint.objects.all()
    serializer_class = LoyaltyPointSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_queryset(self):
        # Filtrer pour retourner seulement les points de fidélité de l'utilisateur connecté
        return self.queryset.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        # Empêcher la création de points de fidélité en dehors du programme établi
        if not serializer.validated_data["program"].is_active:
            raise ValidationError(
                "Le programme de fidélité sélectionné n'est pas actif."
            )
        serializer.save()


class LoyaltyProgramViewSet(viewsets.ModelViewSet):
    """
    Vue pour gérer les programmes de fidélité.
    """

    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    permission_classes = [IsAuthenticated, IsAdminOrModerator]

    def get_queryset(self):
        # Filtrer les programmes actifs
        return self.queryset.filter(is_active=True)


class UsedDiscountViewSet(viewsets.ModelViewSet):
    """
    Vue pour gérer l'historique des remises utilisées.
    """

    queryset = UsedDiscount.objects.all()
    serializer_class = UsedDiscountSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_queryset(self):
        # Filtrer pour retourner seulement les remises utilisées par l'utilisateur connecté
        return self.queryset.filter(client__user=self.request.user)

    def perform_create(self, serializer):
        # Validation supplémentaire lors de l'utilisation d'une remise
        discount = serializer.validated_data["discount"]
        if not discount.is_active:
            raise ValidationError("Cette remise n'est plus active.")
        serializer.save()
