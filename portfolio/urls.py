from django.urls import path

from . import views

urlpatterns = [
    path("", views.MediaGalleryView.as_view(), name="media gallery"),
    path("upload/", views.MediaUploadView.as_view(), name="media upload"),
    path("search/", views.MediaSearchView.as_view(), name="media search"),
    path("<str:slug>/", views.MediaDetailView.as_view(), name="media detail"),
    path("<str:slug>/edit/", views.MediaUpdateView.as_view(), name="media edit"),
    path("<str:slug>/delete/", views.MediaDeleteView.as_view(), name="media delete"),
]
