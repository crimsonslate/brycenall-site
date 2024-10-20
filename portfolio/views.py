from typing import Any

from django.conf import settings
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from portfolio.models import Comment, Media
from portfolio.forms import MediaUploadForm


class CommentListView(ListView):
    allow_empty = True
    content_type = "text/html"
    context_object_name = "comments"
    http_method_names = ["get"]
    model = Comment


class MediaListView(ListView):
    allow_empty = True
    content_type = "text/html"
    context_object_name = "medias"
    http_method_names = ["get"]
    model = Media


class MediaDetailView(DetailView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    queryset = Media.objects.filter(hidden__exact=False)
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments.all()
        context["title"] = self.get_object().title
        return context


class MediaEditView(UpdateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_edit.html"
    fields = ["source", "title", "desc"]
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments.all()
        context["title"] = self.get_object().title
        return context


class MediaDeleteView(DeleteView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_delete.html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}


class MediaUploadView(FormView):
    content_type = "text/html"
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    template_name = "portfolio/media_upload.html"
    extra_context = {"portfolio_name": settings.PORTFOLIO_NAME}
