from django.contrib import admin


class ReplyAdmin(admin.ModelAdmin):
    list_display = ("author", "comment", "content", "created_at")
    search_fields = ("author__username", "comment__content", "content")
    list_filter = ("author", "comment", "created_at")
    ordering = ["-created_at"]
    date_hierarchy = "created_at"
