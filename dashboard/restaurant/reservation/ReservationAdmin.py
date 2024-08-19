from django.contrib import admin

from restaurant.models.reservation import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "restaurant", "number_of_people", "reservation_date"]
    search_fields = ["user__email", "restaurant__name"]
    list_filter = ["restaurant", "reservation_date"]
    date_hierarchy = "reservation_date"
    ordering = ["-reservation_date"]
    list_per_page = 10
    list_select_related = ["user", "restaurant"]
    raw_id_fields = ["user", "restaurant"]
    # readonly_fields = ["created", "modified"]
    fieldsets = (
        (
            None,
            {"fields": ["user", "restaurant", "number_of_people", "reservation_date"]},
        ),
        ("Informations supplémentaires", {"fields": ["special_request"]}),
        ("Métadonnées", {"fields": ["created", "modified"]}),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ["user", "restaurant", "number_of_people", "reservation_date"]},
        ),
        ("Informations supplémentaires", {"fields": ["special_request"]}),
    )


# admin.site.register(Reservation, ReservationAdmin)
