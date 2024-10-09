from django.views.generic import DetailView

from portfolio.models import PublishedMedia

class PublishedMediaDetailView(DetailView):
    content_type = "text/html"
    context_object_name = "media"
    http_method_names = ["get", "post"]
    model = PublishedMedia
    queryset = PublishedMedia.objects.filter(hidden__exact=False)
