from django.contrib import admin
from blog.models.ArticlePhoto import ArticlePhoto

class ArticlePhotoAdmin(admin.ModelAdmin):
    list_display = ("article", "image")
    search_fields = ("article__title",)
    list_filter = ("article",)
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
