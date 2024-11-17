from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/media/gallery_display.html")
def gallery_display(
    media: Media, css_class: str | None = None
) -> dict[str, str | bool | None]:
    return {
        "url": media.source.url if media.is_image else media.thumb.url,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "image": media.is_image,
        "class": css_class,
    }


@register.inclusion_tag("portfolio/media/search_result.html")
def search_result(
    media: Media, css_class: str | None = None
) -> dict[str, str | bool | None]:
    return {
        "url": media.source.url if media.is_image else media.thumb.url,
        "detail_url": media.get_absolute_url(),
        "alttext": media.title,
        "class": css_class if css_class else "",
        "height": str(32),
        "width": str(32),
    }
