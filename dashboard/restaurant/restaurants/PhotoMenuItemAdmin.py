from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.PhotoMenuItem import PhotoMenuItem


class PhotoMenuItemAdmin(admin.ModelAdmin):
    list_display = ["menu_item", "photo", "alt_text"]
    list_filter = ["menu_item", "photo", "alt_text"]
    search_fields = ["menu_item", "photo", "alt_text"]
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


# admin.site.register(PhotoMenuItem, PhotoMenuItemAdmin)
