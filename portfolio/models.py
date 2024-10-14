from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils import timezone
from django.core.files.storage import storages
from django.contrib.auth import get_user_model
from datetime import date

from portfolio.validators import (
    validate_media_file_extension,
    validate_video_file_extension,
)


class Comment(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.PROTECT, default=None, blank=True, null=True
    )
    text = models.TextField(max_length=2048, blank=False, null=True, default=None)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    datetime_published = models.DateTimeField(default=timezone.now)
    datetime_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comment #{self.pk}"


class Media(models.Model):
    title = models.CharField(max_length=256, unique=True)
    source = models.FileField(
        storage=storages["bucket"], validators=[validate_media_file_extension]
    )
    thumb = models.ImageField(
        verbose_name="thumbnail",
        storage=storages["bucket"],
        upload_to="thumb/",
        null=True,
        blank=True,
        default=None,
    )
    desc = models.TextField(verbose_name="description", max_length=2048)
    slug = models.SlugField(
        max_length=64, unique=True, blank=True, null=True, default=None
    )

    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)

    date_created = models.DateField(default=date.today)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_published = models.DateTimeField(default=timezone.now)

    comments = models.ManyToManyField(Comment, default=None, blank=True)
    previous_title = models.CharField(
        max_length=256, blank=True, null=True, default=None
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        if self.is_image:
            self.source.validators = [validate_image_file_extension]
        else:
            self.source.validators = [validate_video_file_extension]
        return super().save(*args, **kwargs)

    @property
    def url(self) -> str:
        return self.source.url


class NewsletterSubmission(models.Model):
    email = models.EmailField(max_length=64, unique=True)
    datetime_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.email
