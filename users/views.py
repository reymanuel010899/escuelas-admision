from django.shortcuts import render, redirect
from .models import  EscuelasModels , User, CarrerasModels, EstudiantesModels
from django.contrib.auth import  login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .form import DatosForms
from django.contrib.auth.decorators import permission_required
# Create your views here.


# listas de  escuelas 
def escuelas_views(request):
    escuelas = EscuelasModels.objects.all()
    return render(request, 'escuela.html', {"escuelas":escuelas})



#login y redirectciones
def login_views(request, pk):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            if user.is_registro:
                escuela = EstudiantesModels.objects.filter(escuela__id=pk, user=user).first()
                if escuela:
                    login(request, user)
                    return redirect('users_app:registra-alunnos', pk=pk)
                else:
                    return render(request, 'login.html', {'error':'no perteneces a esta escuela'})  
           
                
            else:
                escuela = EstudiantesModels.objects.filter(escuela__id=pk, user=user).first()
                if escuela:
                    login(request, user)
                    return redirect('inicio_app:inicio')
                else:
                    return render(request, 'login.html', {'error':'No perteneces a esta Escuela'})
        else:
            return render(request, 'login.html', {'error':'introduzca sus datos bien',})
                             
                
  

#CERRANDO CECCION
def cerrar_seccion(request):
    if request.method == 'GET':
        logout(request)
        return redirect('/')
        
        
        

def registrar_alunnos(request, pk):
    form = DatosForms(pk,  initial={"nombre":None, "Currently":None})
    if request.method == 'POST':
        username = request.POST.get('matricula')
        gmail = request.POST.get('gmail')
        password = request.POST.get('Password')
        curso = request.POST.get('nombre')
        
        user = User.objects.create_superuser(username, gmail, password)
        user.is_superuser = True
        user.save()
        
        carrera =  CarrerasModels.objects.get(id=curso)
        
        escuela = EscuelasModels.objects.get(id=pk)
           
        EstudiantesModels.objects.create(user=user, carrera=carrera, escuela=escuela )
        logout(request)
        return redirect('/')  
    
    return render(request, 'registrar-alunnos.html', {"form":form})


