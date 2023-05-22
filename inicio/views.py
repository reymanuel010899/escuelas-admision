from django.shortcuts import render, redirect
from .models import NotasProfesor
from users.models import CarrerasModels, MateriasModels, EstudiantesModels, Notamodels, SecionModels, ProfesoresModels
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Sum
from django.views.generic import UpdateView
from .form import RegistroNotaForm
from django.urls import reverse_lazy
from .funciones import sacar_seciones



@login_required(login_url='users_app:escuelas')
def home_views(request):
   return render(request, 'inicio.html')


@login_required(login_url='users_app:escuelas')
def pemsum_views(request):
   return render(request, 'plan-estudio.html' )



@login_required(login_url='users_app:escuelas')
def avances_academicos(request):
   if request.method == 'GET':
      user = request.user
      estudiante = EstudiantesModels.objects.get(user=user)
      materias = MateriasModels.objects.filter(materia_carreras_reverce__id=estudiante.carrera.id).order_by('-created')
   return render(request, 'avances-academicos.html', {"carrera":materias})



@login_required(login_url='users_app:escuelas')
def acerca_scholl(request):
   return render(request, 'acerca-scholl.html')




@login_required(login_url='users_app:escuelas')
def notas_del_alunno(request):

   user = request.user
   estudiante = EstudiantesModels.objects.get(user=user)
   notas, promedio = Notamodels.objects.sacar_promedio(estudiante)
   return render(request, 'notas-alunnos.html', {"materia":notas, "promedio":promedio ,"estudiante":estudiante})




def  registrar_nota(request):
   user = request.user
   materias_inpartidad = MateriasModels.objects.filter(profesor__user=user)
   materia_id = request.GET.get('materia','')
   if materia_id != '':
      Seciones = SecionModels.objects.filter(materia__id=materia_id)
      
      secion_id = request.GET.get('secion','')
      if secion_id != '':
         estudiantes_por_secion = SecionModels.objects.get(id=secion_id)
         estudiante = estudiantes_por_secion.estudiante.all()
    
         
         return render(request, 'registrar-nota.html', {"materias":materias_inpartidad, 'seciones':Seciones, 'estudiantes':estudiante})
      return render(request, 'registrar-nota.html', {"materias":materias_inpartidad, 'seciones':Seciones, })
   return render(request, 'registrar-nota.html', {"materias":materias_inpartidad})



def alunnos_seciones(request, pk):
   if request.user.is_profesor:
      form = RegistroNotaForm
      user = request.user
      materias_inpartidad = MateriasModels.objects.filter(profesor__user=user)
      materia_id = request.GET.get('materia','')
      seciones =  sacar_seciones(materia_id)
  


      estudiantes_por_secion = SecionModels.objects.get(id=pk)
      materia = MateriasModels.objects.get(cesion_reverce__id=pk, profesor=estudiantes_por_secion.materia.profesor)
      estudiante = estudiantes_por_secion.estudiante.all()
      alunno = request.GET.get('alunno','')
      notas = NotasProfesor.objects.filter(alunno__in=estudiante, materia=materia).order_by('created')
      if request.method == 'GET':   
         añadir_alunno = request.GET.get('buscar','')
         if añadir_alunno != '':
            encontrado=EstudiantesModels.objects.filter(user__username__icontains = añadir_alunno ).first()
            if encontrado:
               estudiantes_por_secion.estudiante.add(encontrado)
               estudiantes_por_secion.save()
               return render(request, 'registrar-alunnos-notas.html', {'form':form,'estudiantes':estudiante, 'notas':notas, 'alunno':encontrado,'materia':materias_inpartidad})
            return render(request, 'registrar-alunnos-notas.html', {'form':form,'estudiantes':estudiante, 'notas':notas,'materia': materias_inpartidad})
         return render(request, 'registrar-alunnos-notas.html', {'form':form,'estudiantes':estudiante, 'notas':notas, 'materia': materias_inpartidad, 'seciones':seciones})
      
      
      else:
         if alunno != '':
            alunno  = EstudiantesModels.objects.get(id=alunno)
            form = RegistroNotaForm(request.POST)
            if form.is_valid():
               asistencia = form.cleaned_data.get('asistencia','')
               participacion = form.cleaned_data.get('participacion','')
               parcial = form.cleaned_data.get('parcial','')
               final_ex = form.cleaned_data.get('filnal_ex','')
               nota_final = form.cleaned_data.get('nota_final','')
               nota, create =  NotasProfesor.objects.get_or_create(
                                                materia=materia,
                                                alunno=alunno,
                                                    defaults={
                                                       'alunno':alunno,
                                                       'asistencia':asistencia,
                                                       'participacion':participacion,
                                                       'parcial':parcial,
                                                      'filnal_ex':final_ex
                                                    }
               
               )
               
               if nota:
                  if participacion:
                     nota.participacion = participacion
                     nota.save()
                  elif asistencia:
                     nota.asistencia = asistencia
                     nota.save()
                  elif parcial:
                     nota.parcial = parcial
                     nota.save()
                  elif final_ex:
                     nota.filnal_ex = final_ex
                     nota.save()
                  elif nota_final:
                     nota.nota_final = nota_final
                     nota.save() 
                     nota_fix, crd = Notamodels.objects.get_or_create(materia=nota.materia, estudiate=nota.alunno, defaults={'nota':nota.nota_final})
                     nota_fix.nota = nota.nota_final
                     nota_fix.save()
                      
         return redirect('inicio_app:seciones-alunnos', pk=pk) 
   else:
      return redirect('inicio_app:inicio')
 
   
   
def seccines_ultimas(request):
   user = request.user
   secion = SecionModels.objects.filter(materia__profesor__user=user).first()
   if secion:
      return redirect('inicio_app:seciones-alunnos', pk=secion.pk)