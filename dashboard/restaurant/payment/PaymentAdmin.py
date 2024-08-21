from django.contrib import admin

from remise.models import Discount
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
                    "discount",
                    "amount",
                    "payment_method",
                    "status",
                ),
            },
        ),
        # ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    class Media:
        js = ("js/admin_payment.js",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["discount"].queryset = Discount.objects.filter(is_active=True)
        return form
