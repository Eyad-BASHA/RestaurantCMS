from django.contrib import admin


class LoyaltyProgramAdmin(admin.ModelAdmin):
    list_display = ("name", "points_per_euro", "start_date", "end_date", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active", "start_date", "end_date")
    ordering = ("-start_date",)
    list_per_page = 20
    # readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "points_per_euro",
                    "start_date",
                    "end_date",
                    "is_active",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


