from django.contrib import admin


class LoyaltyPointAdmin(admin.ModelAdmin):
    list_display = ("client", "program", "points", "earned_date", "expiry_date")
    search_fields = ("client__user__username", "program__name")
    list_filter = ("program", "earned_date", "expiry_date")
    ordering = ("-earned_date",)
    list_per_page = 20
    # readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "client",
                    "program",
                    "points",
                    "earned_date",
                    "expiry_date",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


