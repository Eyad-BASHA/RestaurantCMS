from django.contrib import admin
from django.utils.html import format_html

# from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

from restaurant.models.restaurant import CategoryMenuItem


class CategoryMenuItemAdmin(DjangoMpttAdmin):
    """Category Menu Item Admin"""

    list_display = (
        "name",
        "slug",
        "description",
        "cat_image",
        "parent",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")

    def cat_image(self, obj):
        """Category image"""
        return format_html(
            '<img src="{}" width="100" height="100" />'.format(obj.cat_image.url)
        )

    cat_image.short_description = "Image"


# admin.site.register(CategoryMenuItem, CategoryMenuItemAdmin)
