from typing import Any
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q, QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, FormView


from portfolio.forms import (
    MediaSearchForm,
    PortfolioAuthenticationForm,
    MediaUploadForm,
)
from portfolio.models import Media


class PortfolioLoginView(LoginView):
    authentication_form = PortfolioAuthenticationForm
    content_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE, "title": "Login"}
    http_method_names = ["get", "post"]
    template_name = "portfolio/login.html"


class PortfolioLogoutView(LogoutView):
    content_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE, "title": "Logout"}
    http_method_names = ["get", "post"]
    success_url_allowed_hosts = settings.ALLOWED_HOSTS
    template_name = "portfolio/logout.html"


class PortfolioContactView(TemplateView):
    content_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE, "title": "Contact"}
    http_method_names = ["get", "post"]
    template_name = "portfolio/contact.html"


class PortfolioGalleryView(ListView):
    content_type = "text/html"
    context_object_name = "medias"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE, "title": "Gallery"}
    http_method_names = ["get", "post"]
    model = Media
    ordering = "-date_created"
    paginate_by = 12
    queryset = Media.objects.filter(is_hidden__exact=False)
    template_name = "portfolio/gallery.html"


class PortfolioSearchView(TemplateView, FormView):
    context_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE, "title": "Search"}
    http_method_names = ["get", "post"]
    template_name = "portfolio/search.html"
    form_class = MediaSearchForm
    success_url = reverse_lazy("portfolio search")

    def form_valid(self, form: MediaSearchForm) -> HttpResponse:
        results = Media.objects.filter(
            Q(title__iexact=form.cleaned_data["search"])
            | Q(title__contains=form.cleaned_data["search"])
        )
        print(results)
        return self.render_to_response(context=self.get_context_data(results))

    def get_context_data(
        self, results: QuerySet[Media, Media] | None = None, **kwargs
    ) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        if results:
            context["results"] = results
        return context


class PortfolioUploadView(LoginRequiredMixin, FormView):
    content_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE, "title": "Upload"}
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    login_url = reverse_lazy("portfolio login")
    success_url = reverse_lazy("portfolio gallery")
    template_name = "portfolio/upload.html"

    def get_success_url(self, media: Media | None = None) -> str:
        if media is not None:
            return reverse("media detail", kwargs={"slug": media.slug})
        return reverse("portfolio gallery")

    def form_valid(self, form: MediaUploadForm) -> HttpResponseRedirect:
        media = Media.objects.create(
            title=form.cleaned_data["title"],
            subtitle=form.cleaned_data["subtitle"],
            desc=form.cleaned_data["desc"],
            source=form.cleaned_data["source"],
        )
        if form.cleaned_data["subtitle"]:
            media.subtitle = form.cleaned_data["subtitle"]
        if form.cleaned_data["thumb"]:
            media.thumb = form.cleaned_data["thumb"]
        media.save()
        return HttpResponseRedirect(self.get_success_url(media))
