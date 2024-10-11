from typing import Any

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    UpdateView,
)
from django.http import HttpResponse
from django.contrib.auth.models import User

from portfolio.models import PublishedMedia
from portfolio.forms import CommentForm


class MediaDetailView(DetailView, FormView):
    form_class = CommentForm
    template_name = "portfolio/media_detail.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments
        return context

    def add_comment(self, user: User, text: str) -> HttpResponse:
        raise NotImplementedError()


class MediaEditView(UpdateView):
    template_name = "portfolio/media_edit.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia


class MediaDeleteView(DeleteView):
    template_name = "portfolio/media_delete.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia


class MediaUploadView(CreateView):
    template_name = "portfolio/media_upload.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
