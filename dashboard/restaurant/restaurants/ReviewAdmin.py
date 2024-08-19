from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.Review import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["menu_item", "user", "rating"]
    list_filter = ["menu_item", "user", "rating"]
    search_fields = ["menu_item", "user", "rating"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "menu_item",
                    "user",
                    "rating",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]


# admin.site.register(Review, ReviewAdmin)
