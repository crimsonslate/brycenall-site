from django.db import models, transaction
from django.utils import timezone
from django.core.files.storage import storages
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from datetime import date


class PublishedMedia(models.Model):
    class MediaType(models.TextChoices):
        VIDEO = "video", _("Video")
        IMAGE = "image", _("Image")

    source = models.FileField(storage=storages["bucket"])
    thumb = models.FileField(verbose_name="thumbnail", storage=storages["bucket"], null=True, blank=True, default=None)
    _type = models.CharField(max_length=5, choices=MediaType.choices, default=MediaType.VIDEO)

    title = models.CharField(max_length=256)
    desc = models.TextField(verbose_name="description", max_length=2048)
    views = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    datetime_published = models.DateTimeField(default=timezone.now())
    datetime_last_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateField(default=date.today)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)



    def __str__(self) -> str:
        return self.title

    @property
    def url(self) -> str:
        return self.source.url

    @transaction.atomic
    def add_view(self) -> None:
        self.views += 1

    @transaction.atomic
    def add_like(self) -> None:
        self.likes += 1

    @transaction.atomic
    def add_dislike(self) -> None:
        self.dislikes += 1


class PublishedMediaComment(models.Model):
    media = models.ForeignKey(PublishedMedia, on_delete=models.PROTECT)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    @transaction.atomic
    def add_like(self) -> None:
        self.likes += 1

    @transaction.atomic
    def add_dislike(self) -> None:
        self.dislikes += 1
