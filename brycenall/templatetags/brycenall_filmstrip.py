from typing import Any
from django.template import Library


register = Library()


@register.inclusion_tag("brycenall/filmstrip.html")
def filmstrip(
    width: int = 220, rect_width: int = 6, css_class: str | None = None
) -> dict[str, Any]:
    if width % rect_width != 0:
        raise ValueError("Invalid width combination")
    return {
        "total_width": width,
        "rect_width": rect_width,
        "rect_height": rect_width,
        "class": css_class,
    }
