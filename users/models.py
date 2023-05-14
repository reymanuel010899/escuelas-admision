from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manayers import usermaneyer, MateriaManayers, NotaManayer
from django.utils import timezone
from django.conf import settings



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True)
    gmail = models.EmailField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatar/archivos')
    ubicacion = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    is_profesor = models.BooleanField(default=False)
    is_registro = models.BooleanField(default=False)
    objects = usermaneyer()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['gmail',]
    

    def __str__(self):
        return str(self.id) + '-'+ self.username
   
   
    
class DirectorModels(models.Model):
    user = models.ForeignKey(User,related_name='director_reverce',  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "director"
        verbose_name_plural = "directores"
        
        
    def __str__(self):
        return self.user.username
    
class EstudiantesModels(models.Model):
    user=models.ForeignKey(User, blank=True, null=True, related_name='user_estudiantes_reverce', on_delete=models.CASCADE)
    carrera = models.ForeignKey('CarrerasModels', blank=True, null=True, related_name='carrera_estudiante_revercs', on_delete=models.CASCADE)
    escuela = models.ForeignKey('EscuelasModels', blank=True, null=True,  related_name='escuela_estudent',  on_delete=models.CASCADE)
    rango = models.CharField(max_length=50, blank=True, null=True)
    cedula = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"
        
        
    def __str__(self):
        return self.user.username  
    
class ProfesoresModels(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='profesor_user_reverce', on_delete=models.CASCADE)
    rango = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "profesore"
        verbose_name_plural = "profesores"
        
        
    def __str__(self):
        return self.user.nombre    
    
    
class SemestreModels(models.Model):
    semestre = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "semestre"
        verbose_name_plural = "semestres"
        
        
    def __str__(self):
        return str(self.semestre)
    
class SecionModels(models.Model):
    estudiante = models.ManyToManyField(EstudiantesModels, blank=True, related_name='estudiante_secion_reverce')
    materia = models.ForeignKey('MateriasModels', related_name='cesion_reverce', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "secion"
        verbose_name_plural = "seciones"
        
        
    def __str__(self):
        return self.codigo
    
    
class MateriasModels(models.Model):
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(ProfesoresModels, blank=True , null=True, related_name='materia_reverce', on_delete=models.CASCADE)
    semestre = models.ForeignKey(SemestreModels, blank=True, related_name='semestre_reverce', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    objects = MateriaManayers()
    
    class Meta:
        verbose_name = 'materias'
        
    def __str__(self):
        return self.nombre
    
    
class Notamodels(models.Model):
    estudiate = models.ForeignKey(EstudiantesModels, blank=True, null=True, related_name='estudiante_nota_reverce', on_delete=models.CASCADE )
    materia = models.ForeignKey(MateriasModels, related_name='nota_reverce', on_delete=models.CASCADE)
    nota = models.PositiveIntegerField()
    objects = NotaManayer()
    created = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "nota"
        verbose_name_plural = "notas"
        
        
    def __str__(self):
        return str(self.nota)
    
    
class CarrerasModels(models.Model):
    nombre = models.CharField(max_length=50)
    pemsum = models.FileField(upload_to='pemsun/')
    materias = models.ManyToManyField(MateriasModels, blank=True,  related_name='materia_carreras_reverce')   
    created = models.DateField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        
        
    def __str__(self):
        return self.nombre  
    
    
    
class EscuelasModels(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.ForeignKey(DirectorModels, blank=True, null=True, related_name='director_reverce', on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(EstudiantesModels, blank=True,  related_name='estudiantes_reverce')
    profesores = models.ManyToManyField(ProfesoresModels, blank=True, related_name='profesores_reverce')
    carreras = models.ManyToManyField(CarrerasModels, blank=True, related_name='carreras_reverce')
    portada = models.ImageField(upload_to="portada/", blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = "escuela"
        verbose_name_plural = "escuelas"
        
        
    def __str__(self):
        return self.nombre    
    
    
    
    
    
    
    
    
    
    