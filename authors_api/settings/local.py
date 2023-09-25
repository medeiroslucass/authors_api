from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",default="UjB60kcoLhLnI9R395pyI_VPwaLz8aBH9kMIUi_osHQpfzc_pV0",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]