from django.contrib import admin


class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "total_price", "created_at")
    search_fields = ("user__username",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 20
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": ("user",),
            },
        ),
        ("Dates", {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )

