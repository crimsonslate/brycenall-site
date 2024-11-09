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
    source = forms.FileField(
        label=_("Source"),
        help_text=_("Upload a video or an image."),
        widget=widgets.FileInput(attrs={"class": "w-full block bg-white"}),
        allow_empty_file=False,
        validators=[validate_media_file_extension],
    )
    thumb = forms.FileField(
        label=_("Thumbnail"),
        help_text=_("Upload an optional thumbnail."),
        widget=widgets.ClearableFileInput(attrs={"class": "w-full block bg-white"}),
        allow_empty_file=False,
        validators=[validate_image_file_extension],
    )
    title = forms.CharField(
        label=_("Title"),
        help_text=_(""),
        widget=widgets.TextInput(attrs={"class": "w-full block bg-white"}),
    )
    subtitle = forms.CharField(
        label=_("Subtitle"),
        help_text=_(""),
        widget=widgets.TextInput(attrs={"class": "p-4 w-full block bg-white"}),
    )
    desc = forms.CharField(
        label=_("Description"), help_text=_(""), widget=widgets.TextInput()
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"), help_text=_(""), widget=widgets.TextInput()
    )


class MediaUploadForm(forms.Form):
    source = forms.FileField(
        label=_("Source"),
        help_text=_("Upload a video or an image."),
        widget=widgets.FileInput(
            attrs={
                "class": "w-full bg-white rounded-md",
            }
        ),
        allow_empty_file=False,
        validators=[validate_media_file_extension],
    )
    thumb = forms.FileField(
        label=_("Thumbnail"),
        help_text=_("Upload an optional thumbnail."),
        widget=widgets.FileInput(attrs={"class": "w-full bg-white rounded-md"}),
        allow_empty_file=False,
        validators=[validate_image_file_extension],
        required=False,
    )
    title = forms.CharField(
        label=_("Title"),
        widget=widgets.TextInput(attrs={"class": "w-full bg-white rounded-md"}),
        max_length=128,
    )
    subtitle = forms.CharField(
        label=_("Subtitle"),
        widget=widgets.TextInput(attrs={"class": "w-full bg-white rounded-md"}),
        required=False,
    )
    desc = forms.CharField(
        label=_("Description"),
        widget=widgets.Textarea(attrs={"class": "w-full bg-white rounded-md"}),
        required=False,
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"),
        widget=widgets.CheckboxInput(attrs={"class": "bg-white rounded-md"}),
        required=False,
    )


class MediaSearchForm(forms.Form):
    search = forms.CharField(
        max_length=128,
        widget=widgets.TextInput(
            attrs={
                "class": "w-full bg-white rounded-md text-center",
                "hx-post": reverse_lazy("portfolio search"),
                "hx-trigger": "keyup queue:last",
                "hx-target": "#search-results",
                "placeholder": "Search...",
                "autofocus": True,
            },
        ),
    )
