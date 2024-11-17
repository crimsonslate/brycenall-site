from typing import Any

from django.template import Library

register = Library()


@register.inclusion_tag("portfolio/backgrounds/terrain.html")
def background_terrain() -> dict[str, Any]: ...


@register.inclusion_tag("portfolio/backgrounds/wireframe.html")
def background_wireframe() -> dict[str, Any]: ...
