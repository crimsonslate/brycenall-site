from django.db import models, transaction
from django.utils import timezone
from django.core.files.storage import storages
from django.contrib.auth import get_user_model
from datetime import date


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    text = models.TextField(max_length=2048)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    @transaction.atomic
    def add_like(self) -> None:
        self.likes += 1

    @transaction.atomic
    def add_dislike(self) -> None:
        self.dislikes += 1


class PublishedMedia(models.Model):
    class Meta:
        verbose_name = "Published Media"
        verbose_name_plural = "Published Medias"

    title = models.CharField(max_length=256)
    source = models.FileField(storage=storages["bucket"])
    thumb = models.FileField(
        verbose_name="thumbnail",
        storage=storages["bucket"],
        null=True,
        blank=True,
        default=None,
    )
    desc = models.TextField(verbose_name="description", max_length=2048)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)

    date_created = models.DateField(default=date.today)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_published = models.DateTimeField(default=timezone.now)

    comments = models.ManyToManyField(Comment)

    def __str__(self) -> str:
        return self.title

    @property
    def url(self) -> str:
        return self.source.url

    @transaction.atomic
    def add_dislike(self) -> None:
        self.dislikes += 1

    @transaction.atomic
    def add_like(self) -> None:
        self.likes += 1

    @transaction.atomic
    def add_view(self) -> None:
        self.views += 1
