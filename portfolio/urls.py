from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("<int:pk>/", views.MediaDetailView.as_view(), name="media detail"),
    path("<int:pk>/edit/", views.MediaEditView.as_view(), name="media edit"),
    path("<int:pk>/delete/", views.MediaDeleteView.as_view(), name="media delete"),
    path("upload/", views.MediaUploadView.as_view(), name="media upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
