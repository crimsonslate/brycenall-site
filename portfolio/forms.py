from django import forms
from django.forms.models import ModelForm
from django.forms.renderers import TemplatesSetting
from django.template import Template

from portfolio.models import Media


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/form.html"
    formset_template_name = "portfolio/forms/formset.html"
    field_template_name = "portfolio/forms/field.html"

    def get_template(self, template_name: str) -> Template | None:
        if template_name.startswith("django/forms/widgets/"):
            template_name = template_name.replace(
                "django/forms/widgets/", "portfolio/forms/partials/_"
            )
        return super().get_template(template_name)


class MediaUploadForm(ModelForm):
    class Meta:
        model = Media
        fields = ["source", "title", "desc"]
        help_texts = {
            "source": "Upload a file.",
            "title": "Create a unique title for the media.",
            "desc": "Write a description for the new media.",
        }


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
