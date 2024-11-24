from django.views.generic import TemplateView
from django.conf import settings


class LandingView(TemplateView):
    content_type = "text/html"
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": "Bryce Nall",
    }
    http_method_names = ["get"]
    template_name = "brycenall/landing.html"
