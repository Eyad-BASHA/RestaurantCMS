# CategoryRestaurantAdmin
# CategoryRestaurantAdmin is a class that is used to customize the admin page for the CategoryRestaurant model.

from django.contrib import admin
from django.utils.html import format_html
from restaurant.models.restaurant.CategoryRestaurant import CategoryRestaurant
from django_mptt_admin.admin import DjangoMpttAdmin


class CategoryRestaurantAdmin(DjangoMpttAdmin):
    list_display = (
        "name",
        "slug",
        "description",
        "parent",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")


# admin.site.register(CategoryRestaurant, CategoryRestaurantAdmin)
