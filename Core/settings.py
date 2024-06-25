

from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# CSRF_COOKIE_DOMAIN = "solopython.com"
# Cuales son las redes que van a tener permiso a la pagina!
#in this place put on all the domain that will have access to the applications
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3000",
  
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3000',
 
] 

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3000',
   
]

# Esto es para poder desplegar la pagina en render!
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

DJANGO_APPS  = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Core',
    'import_export'
]


PROJECT_APPS = [
 'apps.user','apps.ml'
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    # 'import_export',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
}
CKEDITOR_UPLOAD_PATH = "/media/"



MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": env.db("DATABASE_URL"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True


PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 16,
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'