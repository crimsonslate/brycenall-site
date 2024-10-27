from django.template import Library

from portfolio.models import Media

register = Library()


@register.inclusion_tag("portfolio/widgets/display_media.html")
def display_media(media: Media) -> dict[str, Media]:
    return {"media": media}
