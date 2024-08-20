from django.contrib import admin
from blog.models.ArticlePhoto import ArticlePhoto

class ArticlePhotoAdmin(admin.ModelAdmin):
    list_display = ("article", "image", "alt_text")
    search_fields = ("article__title", "alt_text")
    list_filter = ("article", "alt_text")
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
