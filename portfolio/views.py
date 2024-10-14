from typing import Any

from django.http import HttpRequest, HttpResponse
from django.db import transaction
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    UpdateView,
)

from portfolio.models import Media, NewsletterSubmission
from portfolio.forms import MediaUploadForm, NewsletterSignupForm


class NewsletterSignupFormView(FormView):
    content_type = "text/html"
    form_class = NewsletterSignupForm
    http_method_names = ["get", "post"]
    template_name = "portfolio/newsletter_signup.html"

    def form_valid(self, form: NewsletterSignupForm) -> HttpResponse:
        NewsletterSubmission.objects.create(email=form.cleaned_data["email"])
        return super().form_valid(form=form)


class MediaDetailView(DetailView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    queryset = Media.objects.filter(hidden__exact=False)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.add_view()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments.all()
        return context

    @transaction.atomic
    def add_view(self) -> None:
        media: Media = self.get_object()
        media.views += 1
        media.save()


class MediaEditView(UpdateView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name_suffix = "_edit"


class MediaDeleteView(DeleteView):
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media
    template_name_suffix = "_delete"


class MediaUploadView(CreateView):
    content_type = "text/html"
    form_class = MediaUploadForm
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_upload.html"
    template_name_suffix = "_upload"
