from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.order import CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1 
    fields = ("menu_item", "quantity", "item_total")
    readonly_fields = (
        "item_total",
    ) 
    def item_total(self, obj):
        return obj.item_total

    item_total.short_description = _("Total de l'article")


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "total_price", "created_at")
    search_fields = ("user__username",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = ("created_at", "updated_at", "total_price")

    fieldsets = (
        (
            None,
            {
                "fields": ("user",),
            },
        ),
        # ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    inlines = [CartItemInline]
