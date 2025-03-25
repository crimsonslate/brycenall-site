from django.conf import settings
from django.views.generic.base import TemplateView

from crimsonslate_portfolio.views.mixins import (
    HtmxTemplateResponseMixin,
    PortfolioProfileMixin,
)


class LandingView(HtmxTemplateResponseMixin, PortfolioProfileMixin, TemplateView):
    content_type = "text/html"
    extra_context = {"title": settings.PORTFOLIO_PROFILE["USER"]["name"]}
    http_method_names = ["get"]
    template_name = "brycenall/landing.html"
    partial_template_name = "brycenall/partials/_landing.html"
