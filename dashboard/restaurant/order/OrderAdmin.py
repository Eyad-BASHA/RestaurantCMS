from django.contrib import admin

from restaurant.models.order import OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1 
    fields = ("menu_item", "quantity", "item_total")
    readonly_fields = ("item_total",)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "order_type",
        "client",
        "staff",
        "restaurant",
        "status",
        "total_amount",
        "created_at",
    )
    search_fields = (
        "order_number",
        "client__username",
        "staff__username",
        "restaurant__name",
        "status",
    )
    list_filter = ("order_type", "status", "restaurant", "created_at")
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = (
        "order_number",
        "created_at",
        "updated_at",
        "total_amount",
        "status",
    )

    inlines = [OrderItemInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "order_type",
                    "client",
                    "client_name",
                    "table_number",
                    "staff",
                    "restaurant",
                    "note",
                ),
            },
        ),
        # ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

    # def save_model(self, request, obj, form, change):
    #     if not obj.order_number:
    #         obj.order_number = obj.generate_order_number()
    #     super().save_model(request, obj, form, change)
