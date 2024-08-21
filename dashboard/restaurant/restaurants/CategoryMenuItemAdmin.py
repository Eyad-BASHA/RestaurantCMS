from django.contrib import admin
from django.utils.html import format_html

# from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

from restaurant.models.restaurant import CategoryMenuItem


class CategoryMenuItemAdmin(DjangoMpttAdmin):
    """Admin interface for Category Menu Item"""

    list_display = (
        "name",
        "slug",
        "description",
        "display_image",
        "parent",
        "is_active",
    )
    list_filter = ("is_active", "parent")
    search_fields = ("name", "description", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("display_image",)
    ordering = ["name"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "cat_image",
                    "display_image",
                    "parent",
                    "is_active",
                ),
            },
        ),
    )

    def display_image(self, obj):
        """Displays the category image in the admin list view"""
        if obj.cat_image:
            return format_html(
                '<img src="{}" width="100" height="100" />', obj.cat_image.url
            )
        return format_html('<span style="color: #999;">No image</span>')

    display_image.short_description = "Category Image"

    def get_queryset(self, request):
        """Optimizes queryset by selecting related parent categories"""
        return super().get_queryset(request).select_related("parent")


# admin.site.register(CategoryMenuItem, CategoryMenuItemAdmin)
