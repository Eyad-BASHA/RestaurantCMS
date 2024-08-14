from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("cat_name",)}
    list_display = ["cat_name", "slug"]


admin.site.register(Category, CategoryAdmin)
