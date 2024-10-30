from typing import Any

from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from portfolio.models import Media
from portfolio.forms import MediaUploadForm


class GalleryView(ListView):
    content_type = "text/html"
    context_object_name = "medias"
    extra_context = {"title": "Gallery", "portfolio_name": settings.PORTFOLIO_NAME}
    http_method_names = ["get", "post"]
    model = Media
    ordering = "-date_created"
    paginate_by = 12
    queryset = Media.objects.filter(is_hidden__exact=False)  # No hidden media retreived
    template_name = "portfolio/gallery.html"


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


class MediaUpdateView(UpdateView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
    fields = ["source", "title", "desc"]
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_edit.html"

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaDeleteView(DeleteView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
    http_method_names = ["get", "post"]
    model = Media
    success_url = reverse_lazy("media gallery")
    template_name = "portfolio/media_delete.html"

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaUploadView(FormView):
    content_type = "text/html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME, "title": "Upload"}
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    success_url = reverse_lazy("media gallery")
    template_name = "portfolio/media_upload.html"
