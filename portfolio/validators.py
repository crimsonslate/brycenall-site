from django.core.exceptions import ValidationError
from django.db.models.fields.files import File
from django.utils.translation import gettext_lazy as _


def validate_media_file_extension(value: File) -> None:
    valid_file_extensions: tuple = "webm", "mkv", "mp4", "webm", "jpg", "jpeg", "png"
    file_extension: str = value.file.name.split(".")[-1]

    if file_extension not in valid_file_extensions:
        raise ValidationError(
            _("Invalid file extension: %(value)s"),
            params={"value": file_extension},
            code="invalid",
        )


def validate_video_file_extension(value: File) -> None:
    valid_file_extensions: tuple = "webm", "mkv", "mp4"
    file_extension: str = value.file.name.split(".")[-1]

    if file_extension not in valid_file_extensions:
        raise ValidationError(
            _("Invalid file extension: %(value)s"),
            params={"value": file_extension},
            code="invalid",
        )
