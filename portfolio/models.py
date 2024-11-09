import imagesize
import datetime
from datetime import date

from django.core.files import File
from django.core.files.storage import storages
from django.core.validators import get_available_image_extensions
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from portfolio.validators import validate_media_file_extension


class MediaCategory(models.Model):
    name = models.CharField(max_length=64)
    cover = models.ImageField(
        verbose_name="cover image",
        storage=storages["bucket"],
        upload_to="category/",
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        ordering = ["name"]
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
    is_hidden = models.BooleanField(default=False)
    is_image = models.BooleanField(default=None, blank=True, null=True)
    width = models.PositiveIntegerField(default=None, blank=True, null=True)
    height = models.PositiveIntegerField(default=None, blank=True, null=True)
    categories = models.ManyToManyField(MediaCategory)

    date_created = models.DateField(default=date.today)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["date_created"]
        constraints = [
            models.UniqueConstraint(
                fields=["title", "slug"],
                name="%(app_label)s_%(class)s_unique_title_and_slug",
            )
        ]

    def __str__(self) -> str:
        return self.title

    def save(self, **kwargs) -> None:
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)

        if self.file_extension in get_available_image_extensions():
            self.is_image = True
        else:
            self.is_image = False
            self.set_thumbnail(file=None)
        return super().save(**kwargs)

    def get_absolute_url(self) -> str:
        return reverse("media detail", kwargs={"slug": self.slug})

    def set_thumbnail(self, file: File | None = None) -> None:
        self.thumb = file if file else self.generate_thumbnail()

    def generate_thumbnail(self, name: str | None = None) -> File:
        if not name:
            name = f"default_{datetime.datetime.now():%y%m%d%f}"

        with open(name, mode="w") as f:
            default_thumbnail = File(f)
        return default_thumbnail

    @property
    def dimensions(self) -> tuple[int, int]:
        image: File = self.source.path if self.is_image else self.thumb.path
        return imagesize.get(image)

    @property
    def file_extension(self) -> str:
        return self.source.file.name.split(".")[-1]

    @property
    def url(self) -> str:
        return self.source.url
