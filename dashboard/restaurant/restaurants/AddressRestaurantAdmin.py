from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.AddressRestaurant import AddressRestaurant


class AddressRestaurantAdmin(admin.ModelAdmin):
    list_display = ["address_type", "street", "zip_code", "city", "country"]
    list_filter = ["address_type", "city", "country"]
    search_fields = ["address_type", "street", "zip_code", "city", "country"]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "address_type",
                    "street",
                    "zip_code",
                    "city",
                    "country",
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

