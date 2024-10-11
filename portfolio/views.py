from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from portfolio.models import PublishedMedia

class PublishedMediaDetailView(DetailView):
    template_name = "portfolio/media_detail.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
    queryset = PublishedMedia.objects.filter(hidden__exact=False)

class PublishedMediaEditView(UpdateView):
    template_name = "portfolio/media_edit.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
    queryset = PublishedMedia.objects.filter(hidden__exact=False)

class PublishedMediaDeleteView(DeleteView):
    template_name = "portfolio/media_delete.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
    queryset = PublishedMedia.objects.filter(hidden__exact=False)

class PublishedMediaUploadView(CreateView):
    template_name = "portfolio/media_upload.html"
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
    queryset = PublishedMedia.objects.filter(hidden__exact=False)
