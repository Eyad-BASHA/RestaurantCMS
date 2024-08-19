from django.contrib import admin
from stock.models import StockLocation


class StockLocationAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
    list_per_page = 10
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "address",
                )
            },
        ),
    )

