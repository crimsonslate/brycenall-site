from django.conf import settings
from django.views.generic import TemplateView


class LandingView(TemplateView):
    content_type = "text/html"
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": settings.PORTFOLIO_PROFILE["NAME"],
    }
    http_method_names = ["get"]
    template_name = "brycenall/landing.html"
