from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("gallery/", views.MediaListView.as_view(), name="media gallery"),
    path("upload/", views.MediaUploadView.as_view(), name="media upload"),
    path("edit/<slug:slug>/", views.MediaEditView.as_view(), name="media edit"),
    path("delete/<slug:slug>/", views.MediaDeleteView.as_view(), name="media delete"),
    path("<str:slug>/", views.MediaDetailView.as_view(), name="media detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
