from django import forms
from blog.models.ArticlePhoto import ArticlePhoto
from dashboard.forms import MultiImageInputForm


class MultiImageInputForm(forms.ClearableFileInput):
    template_name = "admin/multi_image_input.html"
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs is None:
            attrs = {}
        attrs["multiple"] = True
        self.attrs = attrs
