from datetime import timezone
from django.contrib import admin
from blog.models.Article import Article
from blog.models.ArticlePhoto import ArticlePhoto
from django import forms
from dashboard.forms.MultiImageInputForm import MultiImageInputForm


class ArticlePhotoForm(forms.ModelForm):
    class Meta:
        model = ArticlePhoto
        fields = ["image"]
        widgets = {
            "image": MultiImageInputForm(),  # Correct usage of the widget
        }


class ArticlePhotoInline(admin.TabularInline):
    model = ArticlePhoto
    form = ArticlePhotoForm
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "status", "published_at")
    search_fields = ("title", "content", "author__username", "category__name")
    list_filter = ("category", "author", "status", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ArticlePhotoInline]
    ordering = ["-published_at"]
    date_hierarchy = "published_at"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "category",
                    "title",
                    "slug",
                    "content",
                    "author",
                    "tags",
                    "status",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": ("published_at",),
            },
        ),
    )
    readonly_fields = ("published_at",)

    def save_model(self, request, obj, form, change):
        if obj.status == "published" and not obj.published_at:
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)
