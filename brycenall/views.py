from typing import Any
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView


class LandingView(TemplateView):
    content_type = "text/html"
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": settings.PORTFOLIO_PROFILE["NAME"],
    }
    http_method_names = ["get"]
    template_name = "brycenall/landing.html"


class BackgroundView(TemplateView):
    content_type = "text/html"
    http_method_names = ["get"]
    template_name = "brycenall/background.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        frame: int = request.session.get("frame", 0)
        match frame:
            case 23:
                frame = 0
            case _:
                frame += 1
        request.session["frame"] = frame

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context["next_frame"] = self.request.session.get("frame", 0)
        return context
