from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.MediaDetailView.as_view(), name="media detail"),
    path("<int:pk>/edit/", views.MediaEditView.as_view(), name="media edit"),
    path("<int:pk>/delete/", views.MediaDeleteView.as_view(), name="media delete"),
    path("<int:pk>/upload/", views.MediaUploadView.as_view(), name="media upload"),
]
