from django.contrib import admin

class UsedDiscountAdmin(admin.ModelAdmin):
    list_display = ("client", "discount", "order", "used_at")
    search_fields = ("client__user__username", "discount__code", "order__id")
    list_filter = ("used_at",)
    ordering = ("-used_at",)
    list_per_page = 20
    # readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "client",
                    "discount",
                    "order",
                    "used_at",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


