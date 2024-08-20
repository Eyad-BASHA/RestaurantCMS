from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import IntegrityError, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from account.models.CustomUser import CustomUser
from account.models.Role import Role
from account.models.AddressClient import AddressClient
from account.models.Profile import Profile
from restaurant.models.restaurant import Restaurant



class RestaurantFilter(admin.SimpleListFilter):
    title = _('Restaurant')
    parameter_name = 'restaurant'

    def lookups(self, request, model_admin):
        restaurants = Restaurant.objects.all()
        return [(restaurant.id, restaurant.name) for restaurant in restaurants]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(restaurants__id=self.value())
        return queryset


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
    list_filter = ["is_staff", "is_active", "is_superuser", RestaurantFilter]

    inlines = [ProfileInline]


