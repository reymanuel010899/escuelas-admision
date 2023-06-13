from users.models import EscuelasModels, CarrerasModels, DatosPersonales, EstudiantesModels, DatosSiEsMilitar

def context_user(request):
    if request.user.is_authenticated:
        user = request.user
        curso = EstudiantesModels.objects.filter(user=user).first()
        personales = DatosPersonales.objects.get(estudiante=curso)
        #datos_militares = DatosSiEsMilitar.objects.get(estudiante=curso)
    
        
        return {
            'escuela':curso,
            'personales':personales,
            #'datosmilitares':datos_militares
        }
        
    else:
        return {
          
        }