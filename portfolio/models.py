import imagesize

from django.core.validators import get_available_image_extensions
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.storage import storages
from datetime import date

from portfolio.validators import validate_media_file_extension


class MediaCategory(models.Model):
    name = models.CharField(max_length=64)
    hexcode = models.CharField(max_length=6, default="030303")
    cover_image = models.FileField(upload_to="category/", storage=storages["bucket"])

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name


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
    categories = models.ManyToManyField(MediaCategory)
    is_hidden = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)
    height = models.PositiveIntegerField(default=None, blank=True, null=True)
    width = models.PositiveIntegerField(default=None, blank=True, null=True)

    date_created = models.DateField(default=date.today)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_published = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
            self.validate_constraints()
        self.set_dimensions()
        return super().save(*args, **kwargs)

    def set_dimensions(self) -> None:
        if self.file_extension in get_available_image_extensions():
            self.width, self.height = imagesize.get(self.source.path)

    @property
    def file_extension(self) -> str:
        return self.source.file.name.split(".")[-1]

    @property
    def url(self) -> str:
        return self.source.url
