from django.db import models, transaction
from django.utils import timezone
from django.utils.text import slugify
from django.core.files.storage import storages
from django.contrib.auth import get_user_model
from datetime import date


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    text = models.TextField(max_length=2048, blank=False, null=True, default=None)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    datetime_published = models.DateTimeField(default=timezone.now)
    datetime_last_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comment #{self.pk}"

    @transaction.atomic
    def add_like(self) -> None:
        self.likes += 1

    @transaction.atomic
    def add_dislike(self) -> None:
        self.dislikes += 1


class Media(models.Model):
    title = models.CharField(max_length=256)
    source = models.FileField(storage=storages["bucket"])
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

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    hidden = models.BooleanField(default=False)
    is_image = models.BooleanField(default=False)

    date_created = models.DateField(default=date.today)
    datetime_last_modified = models.DateTimeField(auto_now=True)
    datetime_published = models.DateTimeField(default=timezone.now)

    comments = models.ManyToManyField(Comment, default=None, blank=True)

    def __str__(self) -> str:
        return self.title

    @property
    def url(self) -> str:
        return self.source.url

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @transaction.atomic
    def add_dislike(self) -> None:
        self.dislikes += 1

    @transaction.atomic
    def add_like(self) -> None:
        self.likes += 1

    @transaction.atomic
    def add_view(self) -> None:
        self.views += 1


class NewsletterSubmission(models.Model):
    email = models.EmailField(max_length=64, unique=True)
    datetime_submitted = models.DateTimeField(default=timezone.now)
