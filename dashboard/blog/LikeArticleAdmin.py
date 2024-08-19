from django.contrib import admin


class LikeArticleAdmin(admin.ModelAdmin):
    list_display = ("author", "article", "created_at")
    search_fields = ("author__username", "article__title")
    list_filter = ("author", "article", "created_at")
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
