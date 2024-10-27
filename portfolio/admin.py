from django.contrib import admin

from portfolio.models import Media, MediaCategory


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["source", "thumb"]}),
        ("Text", {"fields": ["title", "subtitle", "desc", "slug"]}),
        ("Stats", {"fields": ["is_hidden", "is_image", "categories"]}),
        ("Dates", {"fields": ["date_created"]}),
    ]


@admin.register(MediaCategory)
class MediaCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "cover_image"]}),
    ]
