from proyecto_cursos.settings.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://escuelas-admision-production.up.railway.app']

DATABASE_URL="postgresql://postgres:G6eCEBb4CdC1eFa5gC*b26C5FEgCd6**@monorail.proxy.rlwy.net:39205/railway"


DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

STATIC_URL = 'static/'

