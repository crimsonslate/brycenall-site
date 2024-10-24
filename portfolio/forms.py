from django import forms
from django.forms.models import ModelForm
from django.forms.renderers import TemplatesSetting
from django.template.base import Template

from portfolio.models import Media


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/form.html"
    field_template_name = "portfolio/forms/field.html"

    def get_template(self, template_name: str) -> Template | None:
        match template_name:
            case "django/forms/widgets/input.html":
                return self.get_template("portfolio/forms/input.html")
            case "django/forms/widgets/text.html":
                return self.get_template("portfolio/forms/input.html")
            case "django/forms/widgets/clearable_file_input.html":
                return self.get_template("portfolio/forms/file.html")
            case "django/forms/widgets/file.html":
                return self.get_template("portfolio/forms/file.html")
            case "django/forms/widgets/textarea.html":
                return self.get_template("portfolio/forms/textarea.html")
            case _:
                print(f"Getting '{template_name}'...")
                return super().get_template(template_name)


class MediaEditForm(ModelForm):
    class Meta:
        model = Media
        fields = [
            "title",
            "source",
            "thumb",
            "subtitle",
            "desc",
            "hidden",
            "is_image",
            "date_created",
        ]


class MediaUploadForm(ModelForm):
    class Meta:
        model = Media
        fields = ["source", "title", "subtitle", "desc"]
        help_texts = {
            "source": "Upload a video or an image.",
            "title": "Create a unique title.",
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
