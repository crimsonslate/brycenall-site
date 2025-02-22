from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/docs/", include("django.contrib.admindocs.urls")),
    path("", views.LandingView.as_view(), name="landing"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("", include("crimsonslate_portfolio.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
