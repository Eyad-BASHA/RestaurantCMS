from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.Restaurant import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "description",
        "addresses",
        "logo",
    ]
    list_filter = ["name", "slug", "description", "logo"]
    search_fields = ["name", "slug", "description", "logo"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "logo",
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
