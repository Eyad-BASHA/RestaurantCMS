from datetime import timezone
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from restaurant.models.restaurant.MenuItem import MenuItem
from restaurant.models.restaurant.PhotoMenuItem import PhotoMenuItem
from django.utils.html import format_html
from django import forms
from dashboard.forms.MultiImageInputForm import MultiImageInputForm


class PhotoMenuItemForm(forms.ModelForm):
    class Meta:
        model = PhotoMenuItem
        fields = ["photo"]
        widgets = {
            # "photo": MultiImageInputForm(),
            "photo": forms.ClearableFileInput(),
        }

class PhotoMenuItemInline(admin.TabularInline):
    model = PhotoMenuItem
    form = PhotoMenuItemForm
    extra = 1
    fields = ("photo", "alt_text", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="100" height="100" />'.format(obj.photo.url)
            )
        return ""

    preview.short_description = _("Aperçu")


class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "menu",
        "get_restaurant",
        "slug",
        "description",
        "price",
        "category",
        "type",
        "is_from_kitchen",
        "status",  
        "show_photos", 
    ]
    list_filter = [
        "menu",
        "menu__restaurant",
        "category",
        "type",
        "status",
        "is_from_kitchen",
    ]
    search_fields = [
        "name",
        "menu__name",
        "menu__restaurant__name",
        "slug",
        "description",
        "price",
        "category__name",
        "type__name",
    ]
    fieldsets = (
        (
            _("Informations générales"),
            {
                "fields": (
                    "name",
                    "menu",
                    "slug",
                    "description",
                    "price",
                    "category",
                    "type",
                    "is_from_kitchen",
                    "status",  
                )
            },
        ),
    )
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PhotoMenuItemInline]

    def get_restaurant(self, obj):
        return obj.menu.restaurant.name

    get_restaurant.short_description = _("Restaurant")
    get_restaurant.admin_order_field = "menu__restaurant__name"

    def show_photos(self, obj):
        photos = obj.photos.all()[:3] 
        return format_html(
            "".join(
                [
                    f'<img src="{photo.photo.url}" width="50" height="50" style="margin-right: 5px;" />'
                    for photo in photos
                ]
            )
        )

    show_photos.short_description = _("Photos")
