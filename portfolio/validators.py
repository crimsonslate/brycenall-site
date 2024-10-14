from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.core.files import File
from django.utils.translation import gettext_lazy as _


def validate_video_extension(value: File) -> None:
    valid_extensions: tuple = "mp4", "mkv", "m4a", "webm"
