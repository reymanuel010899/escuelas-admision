from django.urls import path
from . import views
app_name = 'users_app'


urlpatterns = [
    path('', views.escuelas_views, name="escuelas"),
    path('login/<pk>/', views.login_views, name="login"),
    path('registra-alunnos/<pk>/', views.registrar_alunnos, name="registra-alunnos"),
    path('cerrar-seccion/', views.cerrar_seccion, name="cerrar-seccion")
 ]