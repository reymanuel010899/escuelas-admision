from users.models import EscuelasModels, CarrerasModels, DatosPersonales, EstudiantesModels, DatosSiEsMilitar

def context_user(request):
    if request.user.is_authenticated:
        user = request.user
        curso = EstudiantesModels.objects.filter(user=user).first()
        personales = DatosPersonales.objects.filter(estudiante=curso).first()
        # datos_militare = DatosSiEsMilitar.objects.filter(estudiante=curso).first()
    
        
        return {
            'escuela':curso,
            'personales':personales,
            # 'datosmilitares':datos_militare
        }
        
    else:
        return {
          
        }