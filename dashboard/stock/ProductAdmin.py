from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from stock.models import Product, StockMovement


class StockMovementInline(admin.TabularInline):
    model = StockMovement
    extra = 0
    fields = ["from_location", "to_location", "quantity", "movement_date"]
    readonly_fields = ["movement_date"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity", "unit", "location", "description"]
    list_filter = ["location", "unit"]
    search_fields = ["name", "description"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "description",
                    "quantity",
                    "unit",
                    "location",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["name"]
    inlines = [StockMovementInline]

    def save_model(self, request, obj, form, change):
        if not change:
            # New product, initial stock setting
            StockMovement.objects.create(
                product=obj,
                from_location=None,
                to_location=obj.location,
                quantity=obj.quantity,
                movement_date=obj.created_at,
            )
        super().save_model(request, obj, form, change)
