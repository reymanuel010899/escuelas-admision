from django.db import models
from django.db.models import Q, Avg
from django.contrib.auth.models import BaseUserManager


class usermaneyer(BaseUserManager):
    def _create_user(self, username, gmail,  password, is_active, is_staff, is_superuser,  **extra_fields):
        user =  self.model(
            username=username,
            gmail=gmail,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
             **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_user(self, username, gmail,  password, **extra_fields):
        return self._create_user(username, gmail, password, True, False,False, **extra_fields)    



    def create_superuser(self, username, gmail, password, **extra_fields ):
        return self._create_user(username, gmail,  password, True, True, True, **extra_fields)
    
    
class MateriaManayers(models.Manager):
    def listar_materia_y_promedio(self, estudiante):
        materias = self.filter(estudiantes__id=estudiante.id,materia_carreras_reverce__id=estudiante.carrera.id)
        
        lista = list()
        for mate in materias:
            if mate == None:
                continue
            else:
                lista.append(mate.id)
            
        
        # 
        
        return  lista
    
class NotaManayer(models.Manager):
    def sacar_promedio(self, estudiante):
        
        
        id_semestre = set()
        
        notas = self.filter(estudiate=estudiante)
        for nat in notas:
            id_semestre.add(nat.materia.semestre.id)
            
            
        lista = list()
        if  notas:
            for  noa in notas:
                lista.append(noa.nota)  
            try:
                promedio = sum(lista) / len(lista)
            except:
                return 0
            return notas, promedio, id_semestre
        else:
            return [],[], list(id_semestre)
            
     