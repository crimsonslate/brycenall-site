from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/media/display.html")
def display(media: Media, css_class: str | None = None) -> dict[str, str | bool | None]:
    if media.is_image:
        height, width = media.dimensions
    else:
        height, width = None, None

    return {
        "url": media.url,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "image": media.is_image,
        "height": str(height),
        "width": str(width),
        "class": css_class if css_class else "",
    }


@register.inclusion_tag("portfolio/media/search_result.html")
def search_result(
    media: Media, css_class: str | None = None
) -> dict[str, str | bool | None]:
    return {
        "url": media.url if media.is_image else media.thumb.url,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "class": css_class if css_class else "",
        "height": str(32),
        "width": str(32),
    }
