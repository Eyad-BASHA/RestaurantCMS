from django.contrib import admin


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "menu_item", "quantity", "item_total", "created_at")
    search_fields = ("order__order_number", "menu_item__name")
    list_filter = ("menu_item", "created_at")
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "order",
                    "menu_item",
                    "quantity",
                    "note",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
