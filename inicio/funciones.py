from users.models  import SecionModels, MateriasModels, EstudiantesModels

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
    