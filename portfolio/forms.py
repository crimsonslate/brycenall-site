from django import forms
from django.forms import ModelForm

from portfolio.models import Media


class CommentForm(forms.Form): ...


class MediaUploadForm(ModelForm):
    class Meta:
        model = Media
        fields = [
            "source",
            "thumb",
            "title",
            "desc",
            "is_image",
            "hidden",
            "date_created",
        ]
