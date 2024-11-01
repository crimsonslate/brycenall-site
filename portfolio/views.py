from typing import Any

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView,
)

from portfolio.forms.forms import MediaSearchForm
from portfolio.models import Media
from portfolio.forms import MediaUploadForm


class MediaGalleryView(ListView):
    content_type = "text/html"
    context_object_name = "medias"
    extra_context = {"title": "Gallery", "portfolio_name": settings.PORTFOLIO_NAME}
    http_method_names = ["get", "post"]
    model = Media
    ordering = "-date_created"
    paginate_by = 2
    queryset = Media.objects.filter(is_hidden__exact=False)  # No hidden media retreived
    template_name = "portfolio/gallery.html"


class MediaSearchView(FormView, TemplateView):
    form_class = MediaSearchForm
    context_type = "text/html"
    extra_context = {"title": "Search", "portfolio_name": settings.PORTFOLIO_NAME}
    template_name = "portfolio/media_search.html"
    http_method_names = ["get", "post"]

    def form_valid(self, form: MediaSearchForm) -> HttpResponse:
        return super().form_valid(form=form)


class MediaDetailView(DetailView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
    http_method_names = ["get", "post"]
    model = Media
    queryset = Media.objects.filter(is_hidden__exact=False)
    template_name = "portfolio/media_detail.html"

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaUpdateView(LoginRequiredMixin, UpdateView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
    fields = ["source", "thumb", "title", "desc", "is_hidden"]
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_edit.html"
    login_url = reverse_lazy("admin/login/")

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaDeleteView(LoginRequiredMixin, DeleteView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
    http_method_names = ["get", "post"]
    model = Media
    success_url = reverse_lazy("media gallery")
    template_name = "portfolio/media_delete.html"
    login_url = reverse_lazy("admin/login/")

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaUploadView(LoginRequiredMixin, FormView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME, "title": "Upload"}
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    success_url = reverse_lazy("media gallery")
    template_name = "portfolio/media_upload.html"
    login_url = reverse_lazy("admin/login/")

    def get_success_url(self, media: Media | None = None) -> str:
        if media is not None:
            return reverse("media detail", kwargs={"slug": media.slug})
        return reverse("gallery")

    def form_valid(self, form: MediaUploadForm) -> HttpResponseRedirect:
        media = Media.objects.create(
            title=form.cleaned_data["title"],
            subtitle=form.cleaned_data["subtitle"],
            desc=form.cleaned_data["desc"],
            source=form.cleaned_data["source"],
        )
        return HttpResponseRedirect(self.get_success_url(media))
