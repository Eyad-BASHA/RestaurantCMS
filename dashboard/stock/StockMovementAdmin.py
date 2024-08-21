from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from stock.models import StockMovement


class StockMovementAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "from_location",
        "to_location",
        "quantity",
        "movement_date",
    ]
    list_filter = ["product", "from_location", "to_location", "movement_date"]
    search_fields = ["product__name", "from_location__name", "to_location__name"]
    fieldsets = (
        (
            _("Informations sur le mouvement"),
            {
                "fields": (
                    "product",
                    "from_location",
                    "to_location",
                    "quantity",
                    "movement_date",
                )
            },
        ),
    )
    readonly_fields = ["movement_date"]
    ordering = ["-movement_date"]
