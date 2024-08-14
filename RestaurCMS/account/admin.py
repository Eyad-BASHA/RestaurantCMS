from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import IntegrityError, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.custom_user_entity import CustomUser
from .models.role_entity import Role
from .models.address_entity import Address
from .models.profile_entity import Profile


# class AddressInline(admin.TabularInline):
#     model = Profile.addresses.through
#     extra = 1
#     verbose_name = "Adresse"
#     verbose_name_plural = "Adresses"


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("user", "gender")}),
        (
            "Personal info",
            {"fields": ("phone_number", "bio", "profile_image", "date_of_birth")},
        ),
        ("Addresses", {"fields": ("addresses",)}),
    )
    # inlines = [AddressInline]
    filter_horizontal = ["addresses"]
    list_display = ["user", "phone_number", "gender"]


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1
    fields = (
        "gender",
        "phone_number",
        "bio",
        "date_of_birth",
        "profile_image",
        "addresses",
    )
    filter_horizontal = ["addresses"]


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Roles", {"fields": ("roles",)}),
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
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "roles",
                ),
            },
        ),
    )

    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "date_joined",
        "last_login",
    ]

    list_display_links = ["email", "username"]
    search_fields = ["email", "username", "first_name", "last_name"]
    readonly_fields = ("last_login", "date_joined")
    ordering = ["-date_joined"]
    filter_horizontal = ["roles"]
    list_filter = ["is_staff", "is_active", "is_superuser"]

    inlines = [ProfileInline]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(Role)
