from django.contrib import admin

from portfolio.models import Media, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "datetime_published"
    list_display = ["user", "datetime_published"]
    empty_value_display = "None"


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["source", "thumb", "comments"]}),
        ("Text", {"fields": ["title", "desc", "slug"]}),
        ("Stats", {"fields": ["likes", "dislikes", "hidden", "is_image"]}),
        ("Dates", {"fields": ["date_created"]}),
    ]
