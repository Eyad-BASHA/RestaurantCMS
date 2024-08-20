from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.PhotoMenuItem import PhotoMenuItem


class PhotoMenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu_item", "photo", "alt_text"]
    list_filter = ["menu_item", "alt_text"]
    search_fields = ["menu_item", "alt_text"]
    ordering = ["-created_at"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "menu_item",
                    "photo",
                    "alt_text",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
