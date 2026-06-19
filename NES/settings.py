import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY читается из окружения (на Beget — переменная Python-приложения
# DJANGO_SECRET_KEY). Фолбэк оставлен, чтобы прод не падал без переменной, но
# в публичном репозитории ключ стоит переопределить через окружение.
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-#waun7n%*v6qp8@k&1%-vxl4^0#*e8=v())e3w%ew=bdroqsi0',
)

# DEBUG включается ТОЛЬКО переменной окружения DJANGO_DEBUG=1 (для локальной
# разработки). На проде переменная не задаётся → DEBUG=False. Так больше не
# нужно держать «временный» DEBUG=True в файле и следить, чтобы не закоммитить.
DEBUG = os.environ.get('DJANGO_DEBUG', '') == '1'

ALLOWED_HOSTS = ['nes-agency.ru', 'www.nes-agency.ru']

# Локальная разработка: пускаем localhost только при DEBUG, прод-список не трогаем.
if DEBUG:
    ALLOWED_HOSTS += ['localhost', '127.0.0.1', '[::1]']

# Формы отправляются POST'ом по HTTPS. При DEBUG=False без доверенных origin'ов
# Django отвергает такие запросы с 403 (CSRF) — поэтому перечисляем их явно.
CSRF_TRUSTED_ORIGINS = ['https://nes-agency.ru', 'https://www.nes-agency.ru']

# Сайт работает за nginx/Passenger, который терминирует TLS и проксирует по
# HTTP. Этот заголовок говорит Django, что исходный запрос был по HTTPS.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Куки только по HTTPS на проде; на локальном http (DEBUG=True) — обычные.
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG


# Application definition

INSTALLED_APPS = [
    'lending',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NES.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["lending/templates"],
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

WSGI_APPLICATION = 'NES.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Статика приложения лежит в lending/static и подхватывается
# AppDirectoriesFinder автоматически. STATIC_ROOT — отдельная папка для
# collectstatic (её раздаёт nginx в проде). Раньше STATIC_ROOT='static/'
# совпадал с STATICFILES_DIRS=[BASE_DIR/'static'], и Django падал с
# ошибкой staticfiles.E002 на старте — поэтому STATICFILES_DIRS убран,
# а STATIC_ROOT вынесен в отдельный каталог.
STATIC_URL = '/static/'
# collectstatic складывает сюда; nginx Beget'а отдаёт /static/ из этой же папки.
# Путь совпадает с прежним прод-значением ('static/'), чтобы не перенастраивать
# веб-сервер. STATICFILES_DIRS не задаём — иначе конфликт с STATIC_ROOT (E002).
STATIC_ROOT = BASE_DIR / 'static'

# Медиа-файлы (изображения проектов из модели Project).
# Было 'NES/NES/media/' — двойной NES ломал src картинок портфолио.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'NES/media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
