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
    # estudiante = models.ForeignKey(EstudiantesModels, related_name="estudoante_semestre_reverce", on_delete=models.CASCADE)
    carrera = models.ForeignKey('CarrerasModels', related_name="semestre_carrera", on_delete=models.CASCADE)
    semestre = models.PositiveIntegerField()
    materia  =  models.ManyToManyField('MateriasModels', blank=True, related_name="materia_semestres")
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
    carrera = models.ForeignKey('CarrerasModels', related_name="carrera_materia_reverce", on_delete=models.CASCADE)
    semestre = models.ForeignKey(SemestreModels, blank=True, related_name="materia_semestre_reverce", on_delete=models.CASCADE )
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(ProfesoresModels, blank=True , null=True, related_name='materia_reverce', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    credito = models.PositiveIntegerField(default=1)
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
    
    # la materias es que tienen que tener carreras
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
    nombre = models.CharField(max_length=80)
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



GENDER=(('m','MASCULINO'),('f','FEMENINO'))
ESTADO_CIVIL=(('s','SOLTERO'),('c', 'CASADO'),('u','UNION LIBRE' ))

class DatosPersonales(models.Model):
    estudiante = models.ForeignKey(EstudiantesModels, blank=True, related_name="Datos_personales_reverce", on_delete=models.CASCADE)
    siglas_escuela=models.CharField(max_length=75, blank=True, null=True)
    promocion=models.CharField(max_length=75, blank=True, null=True)
    matricula=models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True,  null=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True, null=True) 
    nacionalidad = models.CharField(max_length=20, blank=True, null=True)
    provincia=models.CharField(max_length=50, blank=True, null=True)
    municipio=models.CharField(max_length=50, blank=True, null=True)
    Secion=models.CharField(max_length=35, blank=True, null=True)
    estado_civil=models.CharField(max_length=20, choices=ESTADO_CIVIL, blank=True, null=True)
    no_cedula=models.CharField(max_length=15, blank=True, null=True)
    telefono_res=models.CharField(max_length=20, blank=True, null=True)
    direcion=models.CharField(max_length=150, blank=True, null=True)
    celular=models.CharField(max_length=20, blank=True, null=True)
    telefono_ofic=models.CharField(max_length=20, blank=True, null=True)
    lugar_trabajo=models.CharField(max_length=75, blank=True, null=True)
    alguna_discapasidad=models.CharField(max_length=20, blank=True, null=True)
    tipo_sangre=models.CharField(max_length=25, blank=True, null=True)
    funcion_desenpeña=models.CharField(max_length=100, blank=True, null=True)
    correo=models.EmailField(blank=True, null=True)
    alergico=models.CharField(max_length=50, blank=True, null=True)
    sexo = models.CharField(max_length=20, choices=GENDER, blank=True, null=True)
    militar=models.BooleanField(default=False, blank=True, null=True)
    
    class Meta:
        verbose_name = "Datos Personale"
        verbose_name_plural = "Datos Personales"
        
    def __str__(self):
        return "hola"
    
    
SECTOR_EDUCATIVO=(('P', 'PUBLICO'),('PR','PRIVADO'))
IDIOMAS=(('español','ESPAÑOL'),('ingles', 'INGLES'),('otros', 'OTROS'))

class DatosSiEsMilitar(models.Model):
    estudiante = models.ForeignKey(EstudiantesModels, blank=True, related_name="Datos_militar_reverce", on_delete=models.CASCADE)
    rango=models.CharField(max_length=35, blank=True, null=True)
    institucion=models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso=models.DateField(blank=True, null=True)
    ultimo_asenso=models.DateField(blank=True, null=True)
    nombre_liceo=models.CharField(max_length=45)
    sector_educativo=models.CharField(max_length=10, choices=SECTOR_EDUCATIVO)
    idiomas_dominas=models.CharField(max_length=10, choices=IDIOMAS)

    
    class Meta:
        verbose_name = "Datos Del Militar"
        verbose_name_plural = "Datos Del Militar"
        
    def __str__(self):
        return self.estudiante
    
    
    
    
class HistorialEducativo(models.Model):
    estudiante = models.ForeignKey(EstudiantesModels, blank=True, related_name="historia_educativo_reverce", on_delete=models.CASCADE)
    nivel_basico =models.CharField(max_length=50, blank=True, null=True)
    institucion_escuelas_basico =models.CharField(max_length=50, blank=True, null=True)
    lugar_basico = models.CharField(max_length=50, blank=True, null=True)
    finalizacion_basico =models.DateField()
    grado_basico =models.CharField(max_length=15, blank=True, null=True)
    nivel_bachiller =models.CharField(max_length=50, blank=True, null=True)
    institucion_escuelas_bachiller =models.CharField(max_length=50, blank=True, null=True)
    lugar_bachiller = models.CharField(max_length=50, blank=True, null=True)
    finalizacion_bachiller = models.DateField()
    grado_bachiller = models.CharField(max_length=15, blank=True, null=True)
    nivel_uni = models.CharField(max_length=50, blank=True, null=True)
    institucion_escuelas_uni = models.CharField(max_length=50, blank=True, null=True)
    lugar_uni = models.CharField(max_length=50, blank=True, null=True)
    finalizacion_uni = models.DateField()
    grado_uni = models.CharField(max_length=15, blank=True, null=True)


    
    class Meta:
        verbose_name = "historial educativo"
        verbose_name_plural = "historial educativos"
        
    def __str__(self):
        return self.estudiante.user.nombre
    
    
class DatosFamiliares(models.Model):
    estudiante = estudiante = models.ForeignKey(EstudiantesModels, blank=True, related_name="datos_familiares_reverce", on_delete=models.CASCADE)
    padre = models.CharField(max_length=50, blank=True, null=True)
    madre =models.CharField(max_length=50, blank=True, null=True)
    esposa=models.CharField(max_length=50, null=True, blank=True)
    hijos=models.CharField(max_length=75, blank=True, null=True)
    telefono=models.CharField(max_length=15, blank=True, null=True)
    contacto_emergencia=models.CharField(max_length=70, blank=True, null=True)

    
    class Meta:
        verbose_name = "Datos De la familia"
        verbose_name_plural = "Datos De las familia"
        
    def __str__(self):
        return self.estudiante
    