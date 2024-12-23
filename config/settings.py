import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DEBUG', '0') == '1'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Lee la clave secreta desde el entorno
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-if-not-set')

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['backend-yw41.onrender.com', 'localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'contact',  # Aquí faltaba la coma
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Este middleware debe estar antes de CommonMiddleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('SQLITE_ENGINE'),
            'NAME': os.path.join(BASE_DIR, os.getenv('SQLITE_NAME')),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('POSTGRES_ENGINE'),
            'NAME': os.getenv('POSTGRES_NAME'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
        }
    }

# Información para correo:

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'True'
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Agrega la URL de tu aplicación React en desarrollo
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "https://josee2701.github.io",
    "https://backend-yw41.onrender.com",  # Asegúrate de incluir el protocolo
    "https://jose-campos.netlify.app"
    
    # Otras URL permitidas pueden ir aquí
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# STATICFILES_DIRS = [
#     # os.path.join(BASE_DIR, "static"),
#     os.path.join(APPS_DIR, "static"),
#     os.path.join(APPS_DIR, "build", "static"),
# ]
# MEDIA_ROOT = os.path.join(APPS_DIR, "media")
# MEDIA_URL = "media/"
# STATIC_URL = "static/"
# # Archivos Static para producción
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# AZURE_ACCOUNT_NAME = os.environ.get("AZURE_ACCOUNT_NAME")
# AZURE_BLOB_AVAIL = all([AZURE_ACCOUNT_NAME])
# if AZURE_BLOB_AVAIL:
#     AZURE_CUSTOM_DOMAIN = f"{AZURE_ACCOUNT_NAME}.blob.core.windows.net"
#     AZURE_LOCATION = ""
#     DEFAULT_FILE_STORAGE = "config.azureblob.AzureMediaStorage"
#     STATICFILES_STORAGE = "config.azureblob.AzureStaticStorage"
#     STATIC_LOCATION = "static"
#     MEDIA_LOCATION = "media"
#     STATIC_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
#     STATIC_ROOT = STATIC_URL
#     MEDIA_URL = f"https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/"
#     MEDIA_ROOT = MEDIA_URL
#     AZURE_OVERWRITE_FILES = True
# STATICFILES_DIRS = [
#     os.path.join(APPS_DIR, "static"),
#     os.path.join(APPS_DIR, "media"),
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
