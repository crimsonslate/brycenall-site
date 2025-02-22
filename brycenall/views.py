from django.conf import settings
from django.contrib.auth.views import LoginView as LoginViewBase
from django.contrib.auth.views import LogoutView as LogoutViewBase

from crimsonslate_portfolio.views.base import HtmxTemplateView, PortfolioProfileMixin

from brycenall.forms import AuthenticationForm


class LandingView(HtmxTemplateView, PortfolioProfileMixin):
    content_type = "text/html"
    extra_context = {"title": settings.PORTFOLIO_PROFILE["USER"]["name"]}
    http_method_names = ["get"]
    template_name = "brycenall/landing.html"
    partial_template_name = "brycenall/partials/_landing.html"


class ContactView(HtmxTemplateView, PortfolioProfileMixin):
    content_type = "text/html"
    http_method_names = ["get"]
    template_name = "brycenall/contact.html"
    partial_template_name = "brycenall/partials/_contact.html"
    extra_context = {"title": "Contact"}


class LoginView(LoginViewBase, HtmxTemplateView, PortfolioProfileMixin):
    authentication_form = AuthenticationForm
    content_type = "text/html"
    extra_context = {"title": "Login"}
    http_method_names = ["get", "post"]
    template_name = "brycenall/login.html"
    partial_template_name = "brycenall/partials/_login.html"


class LogoutView(LogoutViewBase, HtmxTemplateView, PortfolioProfileMixin):
    content_type = "text/html"
    extra_context = {"title": "Logout"}
    http_method_names = ["get", "post"]
    template_name = "brycenall/logout.html"
    partial_template_name = "brycenall/partials/_logout.html"
