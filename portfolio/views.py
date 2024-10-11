from typing import Any

from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.models import User

from portfolio.models import PublishedMedia

class PublishedMediaDetailView(DetailView):
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

class PublishedMediaEditView(UpdateView):
    template_name = "portfolio/media_edit.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia

class PublishedMediaDeleteView(DeleteView):
    template_name = "portfolio/media_delete.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia

class PublishedMediaUploadView(CreateView):
    template_name = "portfolio/media_upload.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
