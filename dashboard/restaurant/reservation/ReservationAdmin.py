from django.contrib import admin

from restaurant.models.reservation import Reservation


class ReservationAdmin(admin.ModelAdmin):
    """Admin interface for managing Reservations"""

    list_display = [
        "user",
        "restaurant",
        "number_of_people",
        "reservation_date",
        "special_request_preview",
    ]
    search_fields = [
        "user__email",
        "user__username",
        "restaurant__name",
        "special_request",
    ]
    list_filter = ["restaurant", "reservation_date"]
    date_hierarchy = "reservation_date"
    ordering = ["-reservation_date"]
    list_per_page = 20
    list_select_related = ["user", "restaurant"]

    fieldsets = (
        (
            "Reservation Details",
            {
                "fields": [
                    "user",
                    "restaurant",
                    "number_of_people",
                    "reservation_date",
                ],
            },
        ),
        (
            "Additional Information",
            {
                "fields": ["special_request"],
            },
        ),
    )

    readonly_fields = ["created_at", "updated_at"]

    def special_request_preview(self, obj):
        """Displays a truncated version of special requests in the list view"""
        return (
            (obj.special_request[:50] + "...")
            if obj.special_request and len(obj.special_request) > 50
            else obj.special_request
        )

    special_request_preview.short_description = "Special Request"

    def get_queryset(self, request):
        """Optimizes queryset by selecting related user and restaurant"""
        return super().get_queryset(request).select_related("user", "restaurant")
