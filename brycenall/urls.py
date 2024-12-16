from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/docs/", include("django.contrib.admindocs.urls")),
    path(
        "login/",
        views.LoginView.as_view(),
        name="login",
    ),
    path("", views.LandingView.as_view(), name="landing"),
    path("", include("crimsonslate_portfolio.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
