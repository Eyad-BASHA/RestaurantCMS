from django.contrib import admin
from .models import CustomUser  # Make sure to import your CustomUser model
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone_number")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "last_login",
    ]

    list_display_links = ["email", "username"]
    search_fields = ["email", "username", "first_name", "last_name", "phone_number"]

    readonly_fields = ("last_login", "date_joined")

    # ordering = ["email", "username", "first_name", "last_name", "phone_number"]
    ordering = ["-date_joined"]

    # Remove or correct these fields if they do not exist in CustomUser
    filter_horizontal = []
    list_filter = ["is_staff", "is_active"]


admin.site.register(
    CustomUser, CustomUserAdmin
)  # Register the model with the admin class
