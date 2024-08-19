from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.Menu import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "restaurant", "slug", "description", "menu_photo"]
    list_filter = ["name", "restaurant", "slug", "description", "menu_photo"]
    search_fields = ["name", "restaurant", "slug", "description", "menu_photo"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "restaurant",
                    "slug",
                    "description",
                    "menu_photo",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("name",)}

# admin.site.register(Menu, MenuAdmin)
