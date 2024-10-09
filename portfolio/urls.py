from django.urls import path

from . import views

urlpatterns = [
    path("<str:slug>/", views.PublishedMediaDetailView.as_view(), name="media view"),
    path("<int:pk>/", views.PublishedMediaDetailView.as_view(), name="media pk view"),
]
