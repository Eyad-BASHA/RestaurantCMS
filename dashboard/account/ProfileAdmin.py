from tkinter import Image
from django.contrib import admin
from account.models.AddressClient import AddressClient
from account.models.Profile import Profile
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


class CityFilter(admin.SimpleListFilter):
    title = _("City")
    parameter_name = "city"

    def lookups(self, request, model_admin):
        cities = AddressClient.objects.values_list("city", flat=True).distinct()
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(addresses__city=self.value())
        return queryset


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("user", "loyalty_number", "gender")}),
        (
            "Personal Info",
            {"fields": ("phone_number", "bio", "profile_image", "date_of_birth")},
        ),
        ("Addresses", {"fields": ("addresses",)}),
        ("Permissions", {"fields": ("is_comment",)}),
    )
    filter_horizontal = ["addresses"]
    list_display = [
        "user",
        "loyalty_number",
        "phone_number",
        "gender",
        "display_image",
        "is_comment",
    ]
    search_fields = ["user__username", "user__email", "phone_number", "loyalty_number"]
    list_filter = ["gender", "is_comment", CityFilter]  # Added the custom filter here
    readonly_fields = ["loyalty_number", "display_image"]
    ordering = ["user__username"]

    def display_image(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" style="width: 50px; height:50px;" />',
                obj.profile_image.url,
            )
        return "No Image"

    display_image.short_description = "Profile Image"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.profile_image:
            img = Image.open(obj.profile_image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(obj.profile_image.path)


# Register the admin class
admin.site.register(Profile, ProfileAdmin)
