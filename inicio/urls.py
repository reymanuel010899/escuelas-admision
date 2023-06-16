from django.urls import path
from . import views

app_name = 'inicio_app'

urlpatterns =[
    path('home/', views.home_views, name="inicio"),
    path('plan-estudios/', views.pemsum_views, name="pemsum-carrera"),
    path('avances-academicos/', views.avances_academicos, name="avances-academicos"),
    path('acerca-escuela/', views.acerca_scholl, name="correo-cemtro"),
    path('notas-alunno/', views.notas_del_alunno, name="notas-alunno"),
    path('registro-nota/', views.registrar_nota, name="registro-nota"),
    path('ultima-secion/', views.seccines_ultimas, name='ultima-secciones'),
    path('seciones-alunnos/<pk>/', views.alunnos_seciones, name="seciones-alunnos"),
    path('actualizar-mis-datos/', views.actualizar_datos, name="actualizar-datos")


]