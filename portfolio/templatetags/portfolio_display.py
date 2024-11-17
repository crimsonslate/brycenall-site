from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/media/display_gallery.html")
def display_gallery(
    media: Media, css_class: str | None = None
) -> dict[str, str | bool | None]:
    return {
        "url": media.source.url if media.is_image else media.thumb.url,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "image": media.is_image,
        "class": css_class,
    }


@register.inclusion_tag("portfolio/media/display_detail.html")
def display_detail(
    media: Media, css_class: str | None = None
) -> dict[str, str | bool | None]:
    return {
        "source_url": media.source.url,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "image": media.is_image,
        "class": css_class,
    }
