from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import validate_image_file_extension
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from portfolio.forms.renderer import PortfolioFormRenderer
from portfolio.forms.widgets import FileInput, TextInput, TextareaInput, CheckboxInput
from portfolio.validators import validate_media_file_extension


class PortfolioAuthenticationForm(AuthenticationForm):
    """A basic authentication form."""


class MediaEditForm(forms.Form):
    default_renderer = PortfolioFormRenderer

    source = forms.FileField(
        label=_("Source"),
        help_text=_("Upload a video or an image."),
        widget=FileInput(),
        allow_empty_file=False,
        validators=[validate_media_file_extension],
    )
    thumb = forms.FileField(
        label=_("Thumbnail"),
        help_text=_("Upload an optional thumbnail."),
        widget=FileInput(),
        allow_empty_file=False,
        validators=[validate_image_file_extension],
    )
    title = forms.CharField(label=_("Title"), help_text=_(""), widget=TextInput())
    subtitle = forms.CharField(label=_("Subtitle"), help_text=_(""), widget=TextInput())
    desc = forms.CharField(
        label=_("Description"), help_text=_(""), widget=TextareaInput()
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"), help_text=_(""), widget=CheckboxInput()
    )


class MediaUploadForm(forms.Form):
    default_renderer = PortfolioFormRenderer

    source = forms.FileField(
        label=_("Source"),
        help_text=_("Upload a video or an image."),
        widget=FileInput(),
        allow_empty_file=False,
        validators=[validate_media_file_extension],
    )
    thumb = forms.FileField(
        label=_("Thumbnail"),
        help_text=_("Upload an optional thumbnail."),
        widget=FileInput(),
        allow_empty_file=False,
        validators=[validate_image_file_extension],
        required=False,
    )
    title = forms.CharField(label=_("Title"), help_text=_(""), widget=TextInput())
    subtitle = forms.CharField(
        label=_("Subtitle"), help_text=_(""), widget=TextInput(), required=False
    )
    desc = forms.CharField(
        label=_("Description"), help_text=_(""), widget=TextareaInput(), required=False
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"),
        help_text=_(""),
        widget=CheckboxInput(),
        required=False,
    )


class MediaSearchForm(forms.Form):
    default_renderer = PortfolioFormRenderer
    search = forms.CharField(
        max_length=64,
        widget=TextInput(
            attrs={
                "hx-post": reverse_lazy("media search"),
                "hx-trigger": "keyup queue:last",
                "placeholder": "Search...",
                "autofocus": True,
            }
        ),
    )
