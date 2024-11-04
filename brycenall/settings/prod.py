from pathlib import Path
from brycenall.aws import get_secret

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [".brycenall", "brycenall"]
CSRF_COOKIE_SECURE = True
DEBUG = False
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "en-us"
PORTFOLIO_NAME = "Bryce Nall"
ROOT_URLCONF = "brycenall.urls"
SECRET_KEY = get_secret("BRYCENALL_SECRET_KEY")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
STATIC_URL = "static/"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "brycenall.wsgi.application"
FORM_RENDERER = "portfolio.forms.PortfolioFormRenderer"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

PORTFOLIO_PROFILE = {
    "NAME": "Bryce Nall",
    "FIRST_NAME": "Bryce",
    "LAST_NAME": "Nall",
    "EMAIL": "btn04@gmail.com",
    "PHONE": None,
    "SOCIALS": {
        "FACEBOOK": {
            "display_name": None,
            "profile_link": None,
            "username": None,
        },
        "YOUTUBE": {
            "display_name": "Bryce Nall",
            "profile_link": "https://www.youtube.com/@brycenall7439",
            "username": "brycenall7439",
        },
        "INSTAGRAM": {
            "display_name": "bryce nall",
            "profile_link": "https://www.instagram.com/bybnall/",
            "username": "bybnall",
        },
        "TIKTOK": {
            "display_name": None,
            "profile_link": None,
            "username": None,
        },
        "TWITTER": {
            "display_name": None,
            "profile_link": None,
            "username": None,
        },
        "REDDIT": {
            "profile_link": None,
            "username": None,
        },
    },
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "location": "static/",
            "session_profile": "brycenall-site",
            "bucket_name": "brycenall-bucket",
            "region_name": "us-east-1",
            "verify": False,
        },
    },
    "bucket": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "location": "media/",
            "session_profile": "brycenall-site",
            "bucket_name": "brycenall-bucket",
            "region_name": "us-east-1",
            "verify": False,
        },
    },
}


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "portfolio.apps.PortfolioConfig",
    "django_htmx",
    "theme",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
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
