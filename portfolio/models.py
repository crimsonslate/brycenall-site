from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.storage import storages
from datetime import date

from portfolio.validators import validate_media_file_extension


class Media(models.Model):
    title = models.CharField(
        max_length=64,
        unique=True,
    )
    source = models.FileField(
        upload_to="source/",
        storage=storages["bucket"],
        validators=[validate_media_file_extension],
    )
    thumb = models.ImageField(
        verbose_name="thumbnail",
        storage=storages["bucket"],
        upload_to="thumb/",
        null=True,
        blank=True,
        default=None,
    )
    subtitle = models.CharField(max_length=128, blank=True, null=True, default=None)
    desc = models.TextField(
        verbose_name="description", max_length=2048, blank=True, null=True, default=None
    )
    slug = models.SlugField(
        max_length=64, unique=True, blank=True, null=True, default=None
    )
    hidden = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)

    date_created = models.DateField(default=date.today)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_published = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
            self.validate_constraints()
        return super().save(*args, **kwargs)

    @property
    def url(self) -> str:
        return self.source.url
