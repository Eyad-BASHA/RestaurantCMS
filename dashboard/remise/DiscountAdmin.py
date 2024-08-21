from django.contrib import admin


class DiscountAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "discount_type",
        "value",
        "min_order_amount",
        "start_date",
        "end_date",
        "is_active",
    )
    search_fields = ("code",)
    list_filter = ("discount_type", "is_active", "start_date", "end_date")
    ordering = ("-start_date",)
    list_per_page = 20
    # readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "code",
                    "discount_type",
                    "value",
                    "min_order_amount",
                    "start_date",
                    "end_date",
                    "is_active",
                ),
            },
        ),
        # ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


