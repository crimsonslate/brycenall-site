from typing import Any

from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    UpdateView,
)

from portfolio.models import Media, Comment
from portfolio.forms import CommentForm, MediaUploadForm


class MediaDetailView(DetailView, FormView):
    form_class = CommentForm
    template_name = "portfolio/media_detail.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments
        return context

    def add_comment(self, user: User, text: str) -> None:
        comment = Comment.objects.create(user=user, text=text)
        media = self.get_object()
        media.add(comment)
        media.save()
        return


class MediaEditView(UpdateView):
    template_name = "portfolio/media_edit.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media


class MediaDeleteView(DeleteView):
    template_name = "portfolio/media_delete.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media


class MediaUploadView(CreateView):
    form_class = MediaUploadForm
    template_name = "portfolio/media_upload.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
