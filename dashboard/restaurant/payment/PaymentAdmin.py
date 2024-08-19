from django.contrib import admin

from restaurant.models.payment import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "payment_method", "status", "created_at")
    search_fields = ("order__id", "payment_method__name", "status")
    list_filter = ("payment_method", "status", "created_at")
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "order",
                    "amount",
                    "payment_method",
                    "status",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )



