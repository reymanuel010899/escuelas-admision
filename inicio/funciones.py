from django.db.models import Q, Sum, Avg
from django.db.models.functions import Lower
from users.models  import SecionModels, MateriasModels, EstudiantesModels, SemestreModels, Notamodels

def sacar_seciones(materia_id):
    if materia_id != '':
        Seciones = SecionModels.objects.filter(materia__id=materia_id)
        return Seciones
    return
      
        
def sacar_secion_y_estudiantes(pk_secion, user):
    # secion_id = request.GET.get('secion','')
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
      
      
      
    # materias = MateriasModels.objects.filter(materia_semestres__id__in=id_semestre)
    # for mat in materias:
    #     id_materias.append(mat.id)



    # notas = Notamodels.objects.filter(estudiate=estudiante, materia__id__in=id_materias).annotate(indices = Sum('nota',) )
    
    return semestres, cantidad

      


def sumar_creditos(semestres):
    pass