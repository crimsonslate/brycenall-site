from typing import Any
from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/widgets/carousel.html")
def carousel_item(context: dict[str, Media | str]) -> dict[str, Any]:
    return {
        "media": context["media"],
        "current_url": context["current_url"],
    }
