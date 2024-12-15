from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as LoginViewBase
from django.contrib.auth.views import LogoutView as LogoutViewBase

from brycenall.forms import AuthenticationForm


class LandingView(TemplateView):
    content_type = "text/html"
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": settings.PORTFOLIO_PROFILE["NAME"],
    }
    http_method_names = ["get"]
    template_name = "brycenall/landing.html"


class LoginView(LoginViewBase):
    authentication_form = AuthenticationForm
    template_name = "brycenall/login.html"
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": "Login",
    }


class LogoutView(LogoutViewBase):
    template_name = "brycenall/logout.html"
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": "Logout",
    }
