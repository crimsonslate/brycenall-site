from typing import Any
from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/media/display_gallery.html")
def display_gallery(media: Media, css_class: str | None = None) -> dict[str, Any]:
    return {
        "url": media.source.url if media.is_image else media.thumb.url,
        "alttext": media.title,
        "class": css_class,
    }


@register.inclusion_tag("portfolio/media/display_search_result.html")
def display_search_result(media: Media, css_class: str | None = None) -> dict[str, Any]:
    return {
        "source_url": media.source.url if media.is_image else media.thumb.url,
        "detail_url": media.get_absolute_url(),
        "title": media.title,
        "class": css_class,
        "width": 64,
        "height": 64,
    }


@register.inclusion_tag("portfolio/media/display_detail.html")
def display_detail(media: Media, css_class: str | None = None) -> dict[str, Any]:
    width, height = media.dimensions
    return {
        "source_url": media.source.url,
        "width": width,
        "height": height,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "image": media.is_image,
        "class": css_class,
    }
