from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.GalleryView.as_view(), name="gallery"),
    path("upload/", views.MediaUploadView.as_view(), name="media upload"),
    path("<str:slug>/", views.MediaDetailView.as_view(), name="media detail"),
    path("<str:slug>/edit/", views.MediaUpdateView.as_view(), name="media edit"),
    path("<str:slug>/delete/", views.MediaDeleteView.as_view(), name="media delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
