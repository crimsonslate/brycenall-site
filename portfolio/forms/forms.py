from typing import Any

from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext_lazy as _

from portfolio.forms.renderer import PortfolioFormRenderer
from portfolio.forms.widgets import FileInput, TextInput, TextareaInput, CheckboxInput
from portfolio.validators import validate_media_file_extension


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
    is_image = forms.FileField(
        label=_("Set as image?"), help_text=_(""), widget=CheckboxInput()
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
    )
    title = forms.CharField(label=_("Title"), help_text=_(""), widget=TextInput())
    subtitle = forms.CharField(label=_("Subtitle"), help_text=_(""), widget=TextInput())
    desc = forms.CharField(
        label=_("Description"), help_text=_(""), widget=TextareaInput()
    )
    is_hidden = forms.FileField(
        label=_("Set as hidden?"), help_text=_(""), widget=CheckboxInput()
    )
    is_image = forms.FileField(
        label=_("Set as image?"), help_text=_(""), widget=CheckboxInput()
    )
