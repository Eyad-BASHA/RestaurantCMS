from django.contrib import admin
from stock.models import Product


# @admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "unit")
    search_fields = ("name",)
