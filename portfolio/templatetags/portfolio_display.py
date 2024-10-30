from typing import Any

from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/media_display.html")
def display(media: Media) -> dict[str, Any]:
    return {
        "url": str(media.url),
        "alttext": str(media.title.title()),
        "image": bool(media.is_image),
        "height": str(media.height) if media.height else None,
        "width": str(media.width) if media.width else None,
    }
