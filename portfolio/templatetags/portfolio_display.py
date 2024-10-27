from typing import Any

from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/media_display.html")
def display(media: Media) -> dict[str, Any]:
    return {
        "title": str(media.title),
        "subtitle": str(media.subtitle) if media.subtitle else None,
        "desc": str(media.desc) if media.desc else None,
        "url": str(media.url),
        "categories": list([str(category.name) for category in media.categories.all()]),
        "date_created": media.date_created,
        "alttext": str(media.title.title()),
        "image": bool(media.is_image),
    }
