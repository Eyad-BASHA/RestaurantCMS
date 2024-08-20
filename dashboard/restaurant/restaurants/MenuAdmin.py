from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.Menu import Menu
from django.utils.html import format_html


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "restaurant", "slug", "description", "menu_photo"]
    list_filter = ["restaurant", "name", "slug"]
    search_fields = ["name", "restaurant__name", "slug", "description"]
    fieldsets = (
        (
            _("General Information"),
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
        (
            _("Timestamps"),
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("name",)}

    def menu_photo_thumbnail(self, obj):
        if obj.menu_photo:
            return format_html(
                '<img src="{}" style="width: 50px; height:50px;" />', obj.menu_photo.url
            )
        return "-"

    menu_photo_thumbnail.short_description = _("Menu Photo")
    list_display = ["name", "restaurant", "slug", "description", "menu_photo_thumbnail"]
