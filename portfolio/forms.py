from django.forms import ModelForm
from django.forms.renderers import TemplatesSetting

from portfolio.models import Media, Comment


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/_form.html"
    formset_template_name = "portfolio/forms/_formset.html"
    field_template_name = "portfolio/forms/_field.html"


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
