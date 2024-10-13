from django.contrib import admin

from portfolio.models import Media, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "datetime_published"
    list_display = ["user", "datetime_published"]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin): ...
