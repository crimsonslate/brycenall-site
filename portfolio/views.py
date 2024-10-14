from typing import Any

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    UpdateView,
)

from portfolio.models import Media, Comment, NewsletterSubmission
from portfolio.forms import CommentForm, MediaUploadForm, NewsletterSignupForm


class NewsletterSignupFormView(FormView):
    form_class = NewsletterSignupForm
    template_name = "portfolio/newsletter_signup.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]

    def form_valid(self, form: NewsletterSignupForm) -> HttpResponse:
        NewsletterSubmission.objects.create(email=form.cleaned_data["email"])
        return super().form_valid(form=form)


class MediaDetailView(DetailView, FormView):
    form_class = CommentForm
    template_name = "portfolio/media_detail.html"
    content_type = "text/html"
    http_method_names = ["get", "post"]
    model = Media

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["comments"] = self.get_object().comments.all()
        return context

    def form_valid(self, form: CommentForm) -> HttpResponseRedirect:
        comment = Comment.objects.create(
            user=form.cleaned_data["user"], text=form.cleaned_data["text"]
        )
        media = self.get_object()
        media.add(comment)
        media.save()
        return HttpResponseRedirect(self.get_success_url())


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
