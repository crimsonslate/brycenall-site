from django.contrib import admin

from portfolio.models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["source", "thumb", "comments"]}),
        ("Text", {"fields": ["title", "desc", "slug"]}),
        ("Stats", {"fields": ["likes", "dislikes", "hidden", "is_image"]}),
        ("Dates", {"fields": ["date_created"]}),
    ]
