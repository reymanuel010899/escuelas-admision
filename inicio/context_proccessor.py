from users.models import EscuelasModels, CarrerasModels, DatosPersonales, EstudiantesModels, DatosSiEsMilitar

def context_user(request):
    if request.user.is_authenticated:
        user = request.user
        estudiante = EstudiantesModels.objects.filter(user=user).first()
        personales = DatosPersonales.objects.filter(estudiante=estudiante).first()
        datos_militare = DatosSiEsMilitar.objects.filter(estudiante=estudiante).first()
    
        
        return {
            'escuela':estudiante,
            'personales':personales,
            'datosmilitares':datos_militare 
        }
        
    else:
        return {
          
        }