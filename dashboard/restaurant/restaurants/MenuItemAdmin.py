from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.MenuItem import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "menu", "slug", "description", "price", "category", "type"]
    list_filter = ["menu", "category", "type"]
    search_fields = ["name", "menu", "slug", "description", "price", "category", "type"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "menu",
                    "slug",
                    "description",
                    "price",
                    "category",
                    "type",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(MenuItem, MenuItemAdmin)
