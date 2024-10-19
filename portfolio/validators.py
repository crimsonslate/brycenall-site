from django.core.exceptions import ValidationError
from django.core.files import File
from django.core.validators import (
    FileExtensionValidator,
    get_available_image_extensions,
)
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def validate_video_file_extension(value: File) -> None:
    video_extensions: list[str] = ["mp4", "mkv", "m4a", "webm"]
    validator = FileExtensionValidator(allowed_extensions=video_extensions)
    validator(value)
    return


def validate_media_file_extension(value: File) -> None:
    video_extensions: list[str] = ["mp4", "mkv", "m4a", "webm"]
    image_extensions: list[str] = list(get_available_image_extensions())
    validator = FileExtensionValidator(
        allowed_extensions=[
            file_extension for file_extension in video_extensions + image_extensions
        ]
    )
    validator(value)
    return


def validate_unique_media_slug(value: str) -> None:
    return


def validate_sluggable(value: str) -> None:
    if "/" in value or not slugify(value, allow_unicode=True):
        raise ValidationError(
            _("'%(value)s' cannot be slugified."),
            code="invalid",
            params={"value": value},
        )
