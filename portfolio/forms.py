from django.forms import ModelForm

from portfolio.models import Media, Comment


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


class MediaEditForm(ModelForm):
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


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
