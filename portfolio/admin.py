from django.contrib import admin

from portfolio.models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["source", "thumb"]}),
        ("Text", {"fields": ["title", "subtitle", "desc", "slug"]}),
        ("Stats", {"fields": ["hidden", "is_image"]}),
        ("Dates", {"fields": ["date_created"]}),
    ]
