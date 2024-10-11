from django.contrib import admin

from portfolio.models import PublishedMedia, PublishedMediaComment


admin.site.register(PublishedMedia)
admin.site.register(PublishedMediaComment)
