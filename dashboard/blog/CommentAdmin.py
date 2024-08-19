from django.contrib import admin


class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "author", "content", "created_at")
    search_fields = ("author__username", "article__title", "content")
    list_filter = ("author", "article", "created_at")
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
