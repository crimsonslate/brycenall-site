from typing import Any

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, UpdateView


from portfolio.models import Media


class MediaDetailView(DetailView):
    content_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE}
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
    extra_context = {"profile": settings.PORTFOLIO_PROFILE}
    fields = ["source", "thumb", "title", "desc", "is_hidden"]
    http_method_names = ["get", "post"]
    model = Media
    template_name = "portfolio/media_edit.html"
    login_url = reverse_lazy("portfolio login")

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context


class MediaDeleteView(LoginRequiredMixin, DeleteView):
    content_type = "text/html"
    extra_context = {"profile": settings.PORTFOLIO_PROFILE}
    http_method_names = ["get", "post"]
    model = Media
    success_url = reverse_lazy("portfolio profile")
    template_name = "portfolio/media_delete.html"
    login_url = reverse_lazy("portfolio login")

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)
        context["title"] = self.get_object().title
        return context
