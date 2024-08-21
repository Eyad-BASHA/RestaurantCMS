from django.contrib import admin


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "menu_item", "quantity", "created_at")
    search_fields = ("cart__user__username", "menu_item__name")
    list_filter = ("menu_item", "created_at")
    ordering = ("menu_item",)
    list_per_page = 20
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "cart",
                    "menu_item",
                    "quantity",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
