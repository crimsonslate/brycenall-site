from django import forms
from django.forms import ModelForm
from django.forms.renderers import TemplatesSetting

from portfolio.models import Media, Comment


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/_form.html"
    formset_template_name = "portfolio/forms/_formset.html"
    field_template_name = "portfolio/forms/_field.html"


class NewsletterSignupForm(forms.Form):
    email = forms.EmailField(
        label="Email Address",
        error_messages={"required": "Please enter your email address."},
    )
    opted_in = forms.BooleanField(
        label="I agree",
        help_text="By checking this box, you agree to recieve marketing emails from us in the future.",
        initial=False,
        error_messages={
            "required": "You must agree to recieve marketing emails from us to sign up for our newsletter."
        },
    )


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
