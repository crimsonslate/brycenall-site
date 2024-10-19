from typing import Any

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from portfolio.models import Comment, Media, NewsletterSubmission
from portfolio.forms import MediaUploadForm, NewsletterSignupForm


class NewsletterSignupFormView(FormView):
    content_type = "text/html"
    form_class = NewsletterSignupForm
    http_method_names = ["get", "post"]
    template_name = "portfolio/newsletter_signup.html"

    def form_valid(self, form: NewsletterSignupForm) -> HttpResponse:
        NewsletterSubmission.objects.create(email=form.cleaned_data["email"])
        return super().form_valid(form=form)


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

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments.all()[:20]
        return context


class MediaEditView(UpdateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_edit.html"
    fields = ["source", "title", "desc"]
    extra_context = {"title": f"{settings.PORTFOLIO_NAME} | Edit"}


class MediaDeleteView(DeleteView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_delete.html"


class MediaUploadView(FormView):
    content_type = "text/html"
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    template_name = "portfolio/media_upload.html"

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.htmx:
            pass
        return super().get(request, *args, **kwargs)
