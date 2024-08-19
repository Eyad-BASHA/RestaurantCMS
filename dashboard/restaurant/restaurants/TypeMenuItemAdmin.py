from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.TypeMenuItem import TypeMenuItem


class TypeMenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "description"]
    list_filter = ["name", "slug", "description"]
    search_fields = ["name", "slug", "description"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("name",)}


# admin.site.register(TypeMenuItem, TypeMenuItemAdmin)
