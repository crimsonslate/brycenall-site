from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("upload/", views.MediaUploadView.as_view(), name="media upload"),
    path("media/edit/<int:pk>/", views.MediaEditView.as_view(), name="media edit"),
    path(
        "media/delete/<int:pk>/", views.MediaDeleteView.as_view(), name="media delete"
    ),
    path("<str:slug>/", views.MediaDetailView.as_view(), name="media detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
