from pathlib import Path

# 1. Главные пути проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Настройки безопасности (Для деплоя на продакшене их нужно прятать в .env)
SECRET_KEY = 'django-insecure-^cgm2hci_3(ruwe4snu=8a8c37kowg#e(z6y!pt@plu7i9w+r9'

DEBUG = True

# Разрешаем открывать сайт по абсолютно любому адресу в интернете
ALLOWED_HOSTS = ['*']
# Доверяем сайту Render для безопасной работы форм входа и регистрации
CSRF_TRUSTED_ORIGINS = ['https://onrender.com']


# 3. Список всех подключенных приложений
INSTALLED_APPS = [
    # ⚠️ Добавляем плагин WhiteNoise на самый верх для правильного перехвата статики
    'whitenoise.runserver_nostatic',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Системные приложения для работы django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Твое личное приложение интернет-магазина
    'shop',
]

# 4. Прослойки обработки запросов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ⚠️ ВАЖНО: Прослойка WhiteNoise для красивого отображения стилей в интернете
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Прослойка аккаунтов allauth
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Твой процессор контекста для корзины покупок
                'shop.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# 5. База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. Валидация паролей
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

# 7. Международные настройки (Язык и время)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 8. ⚠️ РАБОТА СО СТАТИКОЙ И МЕДИА (Исправлено для успешной сборки в интернете)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
# Указываем, куда собирать все файлы стилей
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Добавляем умное хранилище (STORAGES) для сжатия и оптимизации файлов
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
# Картинки товаров, которые загружают пользователи
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 9. Дополнительные внутренние настройки магазина
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Маршруты перенаправления при входе и выходе
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Настройки авторизации django-allauth
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_METHODS = {"username", "email"}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# ID сессии для твоей корзины товаров
CART_SESSION_ID = "cart"

# 10. Отправка писем (Вывод в консоль в режиме разработки)
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

CSRF_TRUSTED_ORIGINS = ['https://onrender.com']
