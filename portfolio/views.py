from typing import Any

from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    TemplateView,
    UpdateView,
)
from django.views.generic.list import MultipleObjectMixin

from portfolio.models import Media
from portfolio.forms import MediaUploadForm


class GalleryView(MultipleObjectMixin, TemplateView):
    template_name = "portfolio/gallery.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]
    extra_context = {"title": "Gallery", "porfolio_name": settings.PORTFOLIO_NAME}
    context_object_name = "media_list"
    paginate_by = 12
    model = Media
    ordering = "-date_created"
    queryset = Media.objects.filter(is_hidden__exact=False)
    object_list = Media.objects.filter(is_hidden__exact=False)


class MediaDetailView(DetailView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    template_name = "portfolio/media_detail.html"
    model = Media
    queryset = Media.objects.filter(is_hidden__exact=False)
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaUpdateView(UpdateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_edit.html"
    fields = ["source", "title", "desc"]
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaDeleteView(DeleteView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_delete.html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
    success_url = reverse_lazy("media gallery")

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaUploadView(FormView):
    content_type = "text/html"
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    template_name = "portfolio/media_upload.html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME, "title": "Upload"}
    success_url = reverse_lazy("media gallery")
