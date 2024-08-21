# CategoryRestaurantAdmin
# CategoryRestaurantAdmin is a class that is used to customize the admin page for the CategoryRestaurant model.

from django.contrib import admin
from django.utils.html import format_html
from restaurant.models.restaurant.CategoryRestaurant import CategoryRestaurant
from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryRestaurantAdmin(DjangoMpttAdmin):
    """Admin interface for Category Restaurant"""

    list_display = (
        "name",
        "slug",
        "description",
        "parent",
        "is_active",
    )
    list_filter = ("is_active", "parent")
    search_fields = ("name", "description", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at", )
    ordering = ["name"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
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
