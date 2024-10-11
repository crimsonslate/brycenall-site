from django.urls import path

from . import views

urlpatterns = [
    path("<int:pk>/", views.PublishedMediaDetailView.as_view(), name="media detail"),
    path("<int:pk>/edit/", views.PublishedMediaEditView.as_view(), name="edit update"),
]
