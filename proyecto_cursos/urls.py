
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users_app')),
    path('inicio/', include('inicio.urls', namespace='inicio_app'))
]


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
