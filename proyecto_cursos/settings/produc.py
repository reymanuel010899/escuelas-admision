from proyecto_cursos.settings.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://escuelas-admision-production.up.railway.app']

DATABASE_URL="postgresql://postgres:RFT6afSCVmiKEfxIJefZ@containers-us-west-97.railway.app:6099/railway"


DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

STATIC_URL = 'static/'

