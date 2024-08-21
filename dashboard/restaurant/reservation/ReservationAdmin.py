from django.contrib import admin

from restaurant.models.reservation import Reservation


class ReservationAdmin(admin.ModelAdmin):
    """Admin interface for managing Reservations"""

    list_display = [
        "user",
        "restaurant",
        "reservation_date",
        "start_time",
        "end_time",
        "number_of_people",
    ]
    search_fields = ["user__username", "restaurant__name", "reservation_date"]
    list_filter = ["restaurant", "reservation_date"]
    date_hierarchy = "reservation_date"
    ordering = ["-reservation_date"]
    list_per_page = 20
    list_select_related = ["user", "restaurant"]
    filter_horizontal = ("tables",)

    fieldsets = (
        (
            "Reservation Details",
            {
                "fields": [
                    "user",
                    "restaurant",
                    "reservation_date",
                    "start_time",
                    "end_time",
                    "number_of_people",
                    "is_confirmed",
                    "tables",
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
