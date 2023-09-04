from pathlib import Path
# Build paths inside the project like this: BASE_DIR / &#39;subdir&#39;.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = &#39;django-insecure-!aga#hcx4$&amp;f3i-k4ltxnp&amp;2=oshp85@dg9zj2i7)r3al(44dw&#39;
# SECURITY WARNING: don&#39;t run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    &#39;django.contrib.admin&#39;,
    &#39;django.contrib.auth&#39;,
    &#39;django.contrib.contenttypes&#39;,
    &#39;django.contrib.sessions&#39;,
    &#39;django.contrib.messages&#39;,
    &#39;django.contrib.staticfiles&#39;,
    &#39;member&#39;,
]
MIDDLEWARE = [
    &#39;django.middleware.security.SecurityMiddleware&#39;,
    &#39;django.contrib.sessions.middleware.SessionMiddleware&#39;,
    &#39;django.middleware.common.CommonMiddleware&#39;,
    &#39;django.middleware.csrf.CsrfViewMiddleware&#39;,
    &#39;django.contrib.auth.middleware.AuthenticationMiddleware&#39;,
    &#39;django.contrib.messages.middleware.MessageMiddleware&#39;,
    &#39;django.middleware.clickjacking.XFrameOptionsMiddleware&#39;,
]
ROOT_URLCONF = &#39;bot.urls&#39;
TEMPLATES = [
    {
        &#39;BACKEND&#39;: &#39;django.template.backends.django.DjangoTemplates&#39;,
        &#39;DIRS&#39;: [],
        &#39;APP_DIRS&#39;: True,
        &#39;OPTIONS&#39;: {
            &#39;context_processors&#39;: [
                &#39;django.template.context_processors.debug&#39;,
                &#39;django.template.context_processors.request&#39;,
                &#39;django.contrib.auth.context_processors.auth&#39;,
                &#39;django.contrib.messages.context_processors.messages&#39;,
            ],
        },
    },
]
WSGI_APPLICATION = &#39;bot.wsgi.application&#39;

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    &#39;default&#39;: {
        &#39;ENGINE&#39;: &#39;django.db.backends.sqlite3&#39;,
        &#39;NAME&#39;: BASE_DIR / &#39;db.sqlite3&#39;,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        &#39;NAME&#39;:
&#39;django.contrib.auth.password_validation.UserAttributeSimilarityValidator&#39;,
    },
    {
        &#39;NAME&#39;: &#39;django.contrib.auth.password_validation.MinimumLengthValidator&#39;,
    },
    {
        &#39;NAME&#39;: &#39;django.contrib.auth.password_validation.CommonPasswordValidator&#39;,
    },
    {
        &#39;NAME&#39;: &#39;django.contrib.auth.password_validation.NumericPasswordValidator&#39;,
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = &#39;en-us&#39;
TIME_ZONE = &#39;UTC&#39;
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = &#39;static/&#39;
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = &#39;django.db.models.BigAutoField&#39;
