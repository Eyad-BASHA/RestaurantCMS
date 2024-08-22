from datetime import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from restaurant.models.reservation import Reservation, Availability
from restaurant.serializers.reservation_serializer import (
    ReservationSerializer,
    AvailabilitySerializer,
)


class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        reservation = self.get_object()
        if reservation.is_confirmed:
            return Response(
                {"detail": "Vous ne pouvez pas modifier une réservation confirmée."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if reservation.reservation_date < timezone.now().date():
            return Response(
                {"detail": "Vous ne pouvez pas modifier une réservation passée."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().update(request, *args, **kwargs)


class AvailabilityListCreateView(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]


class AvailabilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        availability = self.get_object()
        if availability.date < timezone.now().date():
            return Response(
                {"detail": "Vous ne pouvez pas modifier une disponibilité passée."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().update(request, *args, **kwargs)
