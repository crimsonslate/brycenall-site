from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import validate_image_file_extension
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.forms import widgets

from portfolio.validators import validate_media_file_extension


class PortfolioAuthenticationForm(AuthenticationForm):
    """A basic authentication form."""


class MediaEditForm(forms.Form):
    default_class = "w-full block bg-white rounded-md p-4 mt-2 mb-4 dark:text-gray-50 dark:bg-gray-800"

    source = forms.FileField(
        label=_("Source"),
        help_text=_("Upload a video or an image."),
        widget=widgets.FileInput(attrs={"class": default_class}),
        allow_empty_file=False,
        validators=[validate_media_file_extension],
    )
    thumb = forms.FileField(
        label=_("Thumbnail"),
        help_text=_("Upload an optional thumbnail."),
        widget=widgets.ClearableFileInput(attrs={"class": default_class}),
        allow_empty_file=False,
        validators=[validate_image_file_extension],
    )
    title = forms.CharField(
        label=_("Title"),
        help_text=_(""),
        widget=widgets.TextInput(attrs={"class": default_class}),
    )
    subtitle = forms.CharField(
        label=_("Subtitle"),
        help_text=_(""),
        widget=widgets.TextInput(attrs={"class": default_class}),
    )
    desc = forms.CharField(
        label=_("Description"), help_text=_(""), widget=widgets.Textarea()
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"),
        help_text=_(""),
        widget=widgets.CheckboxInput(attrs={"class": default_class}),
    )


class MediaUploadForm(forms.Form):
    default_field_class = "w-full block bg-white rounded-md p-4 mt-2 mb-4 dark:text-gray-50 dark:bg-gray-800"

    source = forms.FileField(
        label=_("Source"),
        help_text=_("Upload a video or an image."),
        widget=widgets.FileInput(attrs={"class": default_field_class}),
        allow_empty_file=False,
        validators=[validate_media_file_extension],
    )
    thumb = forms.FileField(
        label=_("Thumbnail"),
        help_text=_("Upload an optional thumbnail."),
        widget=widgets.FileInput(attrs={"class": default_field_class}),
        allow_empty_file=False,
        validators=[validate_image_file_extension],
        required=False,
    )
    title = forms.CharField(
        label=_("Title"),
        widget=widgets.TextInput(attrs={"class": default_field_class}),
        max_length=64,
    )
    subtitle = forms.CharField(
        label=_("Subtitle"),
        widget=widgets.TextInput(attrs={"class": default_field_class}),
        required=False,
    )
    desc = forms.CharField(
        label=_("Description"),
        widget=widgets.Textarea(attrs={"class": default_field_class}),
        required=False,
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"),
        help_text=_(
            """If you're not ready to share this media with the world,
            or if you'd rather just store it here, check this box."""
        ),
        widget=widgets.CheckboxInput(attrs={"class": default_field_class}),
        required=False,
    )


class MediaSearchForm(forms.Form):
    default_field_class = "w-full block bg-white rounded-md p-2 dark:text-gray-50 dark:bg-gray-800 text-center"

    search = forms.CharField(
        max_length=64,
        widget=widgets.TextInput(
            attrs={
                "class": default_field_class,
                "hx-post": reverse_lazy("portfolio search"),
                "hx-trigger": "keyup queue:last",
                "hx-target": "#search-results",
                "hx-swap": "outerHTML",
                "placeholder": "Search...",
                "autofocus": True,
                "required": False,
            },
        ),
    )
