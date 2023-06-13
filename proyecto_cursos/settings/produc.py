from proyecto_cursos.settings.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://escuelas-admision-production.up.railway.app']

DATABASE_URL="postgresql://postgres:ILcxPxkJYSaesnwmLmjV@containers-us-west-10.railway.app:7190/railway"


DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

STATIC_URL = 'static/'

