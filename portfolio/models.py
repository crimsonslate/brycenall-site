from django.db import models
from django.utils import timezone
from django.core.files.storage import storages
from datetime import date


class PublishedMedia(models.Model):
    # The media itself
    source = models.FileField(storage=storages["bucket"])

    # Info
    title = models.CharField(max_length=256)
    desc = models.TextField(verbose_name="description", max_length=2048)
    datetime_published = models.DateTimeField(default=timezone.now())
    datetime_last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.title


class PublishedVideo(PublishedMedia, models.Model):
    ...


class PublishedImage(PublishedMedia, models.Model):
    ...
