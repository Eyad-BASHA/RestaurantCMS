from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.Restaurant import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "description",
        "addresses",
        "logo",
    ]
    list_filter = ["name", "slug", "category", "description", "logo"]
    search_fields = ["name", "slug", "category", "description"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "slug",
                    "category",
                    "description",
                    "logo",
                    "addresses",
                    "staff",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("name",)}

    filter_horizontal = (
        "staff",
    )  


# admin.site.register(Restaurant, RestaurantAdmin)
