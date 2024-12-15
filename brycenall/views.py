from typing import Any
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse_lazy
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
    success_url = reverse_lazy("landing")
    template_name = "brycenall/login.html"
    field_classes = {
        "unbound": "m-4 p-4 grow rounded bg-white text-gray-800",
        "invalid": "m-4 p-4 grow rounded bg-red-100 text-red-500",
    }
    extra_context = {
        "profile": settings.PORTFOLIO_PROFILE,
        "title": "Login",
    }

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        print(kwargs)
        return kwargs

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        form.fields["username"].widget.attrs.update(
            {"class": self.field_classes["invalid"]}
        )
        form.fields["password"].widget.attrs.update(
            {"class": self.field_classes["invalid"]}
        )
        return super().form_invalid(form=form)


class LogoutView(LogoutViewBase):
    template_name = "brycenall/logged_out.html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE}
