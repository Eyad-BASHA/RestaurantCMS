from django.contrib import admin

from stock.models import StockMovement


# @admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "from_location",
        "to_location",
        "movement_date",
    )
    list_filter = ("product", "from_location", "to_location")
    search_fields = ("product__name",)
    date_hierarchy = "movement_date"
    ordering = ("-movement_date",)
