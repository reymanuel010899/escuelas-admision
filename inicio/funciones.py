from django.db.models import Q, Sum, Avg
from django.db.models.functions import Lower
from users.models  import SecionModels, MateriasModels, EstudiantesModels, SemestreModels, Notamodels, DatosPersonales, DatosSiEsMilitar

def sacar_seciones(materia_id):
    if materia_id != '':
        Seciones = SecionModels.objects.filter(materia__id=materia_id)
        return Seciones
    return
      
def sacar_secion_y_estudiantes(pk_secion, user):
    if pk_secion != '':
        secion = SecionModels.objects.get(id=pk_secion)
        estudiante = secion.estudiante.all()
        materia = MateriasModels.objects.get(cesion_reverce__id=pk_secion, profesor=secion.materia.profesor)
        return secion, estudiante, materia
    else:
        secion = SecionModels.objects.filter(materia__profesor__user=user).first()
        estudiante = secion.estudiante.all()
        materia = MateriasModels.objects.get(cesion_reverce__id=secion.id, profesor=secion.materia.profesor)
        return secion, estudiante, materia


def buscar_y_añadir_alunnos(añadir_alunno, secion):
    if añadir_alunno != '':
        encontrado=EstudiantesModels.objects.filter(user__username__icontains = añadir_alunno ).first()
        if encontrado:
            secion.estudiante.add(encontrado)
            secion.save()
            return encontrado
    
    
def calcular_indice(indice, estudiante):
    semestre = SemestreModels.objects.filter(carrera=estudiante.carrera)
    cantidad = []
    for sem in semestre:
        if estudiante == sem.materia.nota_reverce.estudiante:
            cantidad += 1
        return cantidad
            

def avances_matriz(estudiante):
    cantidad = 0
    semestres = SemestreModels.objects.filter(carrera=estudiante.carrera).annotate(indice_semestral=Avg('materia__nota_reverce__nota', filter=Q(materia__nota_reverce__estudiate=estudiante)), creditos=Sum('materia__credito')).order_by('created')
    for sem in semestres:
        cantidad += sem.creditos
    return semestres, cantidad

      

def sumar_creditos(semestres):
    pass


def actualizar(request):
    user = request.user
    estudiante = EstudiantesModels.objects.filter(user=user).first()
    actualizar_user(request, user)
    actualizar_datos_personales(request, estudiante)
    actualizar_datos_militar(request, estudiante)
    
  
def actualizar_user(request, user):
    user.nombre = request.POST.get('nombre')
    user.apellido = request.POST.get('apellido')
    user.correo = request.POST.get('correo')
    user.save()


def actualizar_datos_personales(request, estudiante):
    datos_personales = DatosPersonales.objects.filter(estudiante=estudiante).first()
    datos_personales.nacionalidad = request.POST.get('nacionalidad')
    datos_personales.estado_civil = request.POST.get('estado-civil')
    datos_personales.no_cedula = request.POST.get('cedula')
    datos_personales.celular = request.POST.get('celular')
    datos_personales.tipo_sangre = request.POST.get('samgre')
    datos_personales.direcion = request.POST.get('direcion')
    datos_personales.fecha_nacimiento = request.POST.get('nacimiento')
    datos_personales.save()


def actualizar_datos_militar(request, estudiante):
    datos_militar =  DatosSiEsMilitar.objects.get(estudiante=estudiante)
    datos_militar.rango = request.POST.get('rango')
    datos_militar.fecha_ingreso = request.POST.get('ingreso')
    datos_militar.ultimo_asenso = request.POST.get('ultimo')
    datos_militar.institucion = request.POST.get('institucion')
    datos_militar.save()