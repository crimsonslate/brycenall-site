from pathlib import Path


ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
INTERNAL_IPS = ["127.0.0.1", "0.0.0.0"]
LANGUAGE_CODE = "en-us"
MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "media/"
ROOT_URLCONF = "brycenall.urls"
SECRET_KEY = "django-insecure-#ezlo7tqc&h07y4g^1i3jqg78^z*jgsyd11kq812^=k4%!lk6b"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = "/static/"
STATIC_URL = "static/"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "brycenall.wsgi.application"

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "easy_thumbnails.processors.scale_and_crop",
    # "easy_thumbnails.processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

PORTFOLIO_PROFILE = {
    "USER": {
        "name": "Bryce Nall",
        "first_name": "Bryce",
        "last_name": "Nall",
        "email": "bryce@llandv.com",
        "phone": None,
    },
    "SOCIALS": [
        {"NAME": "Discord", "OPTIONS": {}},
        {"NAME": "Facebook", "OPTIONS": {}},
        {
            "NAME": "Instagram",
            "OPTIONS": {
                "display_name": "bryce nall",
                "profile_link": "https://www.instagram.com/bybnall/",
                "username": "bybnall",
                "icon": "portfolio/icons/instagram.svg",
            },
        },
        {"NAME": "Reddit", "OPTIONS": {}},
        {
            "NAME": "TikTok",
            "OPTIONS": {
                "display_name": "bnall",
                "profile_link": "https://www.tiktok.com/@by_bnall",
                "username": "by_bnall",
                "icon": "portfolio/icons/tiktok.svg",
            },
        },
        {
            "NAME": "Youtube",
            "OPTIONS": {
                "display_name": "Bryce Nall",
                "profile_link": "https://www.youtube.com/@bybnall/",
                "username": "bybnall",
                "icon": "portfolio/icons/youtube.svg",
            },
        },
    ],
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    "bucket": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
    "django_browser_reload",
    "easy_thumbnails",
    "filer",
    "crimsonslate_portfolio.apps.CrimsonslatePortfolioConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
