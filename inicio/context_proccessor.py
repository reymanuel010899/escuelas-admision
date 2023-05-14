from users.models import EscuelasModels, CarrerasModels, EstudiantesModels

def context_user(request):
    if request.user.is_authenticated:
        user = request.user
        curso = EstudiantesModels.objects.filter(user=user).first()
        
        return {
            'escuela':curso,
        }
        
    else:
        return {
          
        }