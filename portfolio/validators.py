from django.core.validators import (
    FileExtensionValidator,
    get_available_image_extensions,
)
from django.core.files import File


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
