from django.contrib import admin


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
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "order_number",
                    "order_type",
                    "client",
                    "client_name",
                    "table_number",
                    "staff",
                    "restaurant",
                    "status",
                    "total_amount",
                    "note",
                ),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )


