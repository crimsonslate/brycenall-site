from django import forms
from django.forms.renderers import TemplatesSetting
from django.template import Template
from django.forms.widgets import Textarea


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/form.html"
    formset_template_name = "portfolio/forms/formset.html"
    field_template_name = "portfolio/forms/field.html"

    def get_template(self, template_name: str) -> Template | None:
        if template_name.startswith("django/forms/widgets/"):
            return super().get_template(
                template_name.replace(
                    "django/forms/widgets/", "portfolio/forms/partials/_"
                )
            )
        elif template_name.startswith("django/forms/"):
            return super().get_template(
                template_name.replace("django/forms/", "portfolio/forms/")
            )
        return super().get_template(template_name)


class CommentUploadForm(forms.Form):
    user = forms.UUIDField()
    text = forms.CharField(max_length=2048)


class MediaUploadForm(forms.Form):
    source = forms.FileField()
    title = forms.CharField(label="Title", max_length=256)
    desc = forms.CharField(label="Description", max_length=2048, widget=Textarea())


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
