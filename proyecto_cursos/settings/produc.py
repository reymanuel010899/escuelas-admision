from proyecto_cursos.settings.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://escuelas-admision-production.up.railway.app']

DATABASE_URL="postgresql://postgres:cpajwVSzQI3qVsMei8KA@containers-us-west-169.railway.app:7489/railway"


DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}

STATIC_URL = 'static/'

