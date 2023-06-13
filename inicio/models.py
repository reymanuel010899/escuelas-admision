from django.db import models

from users.models import EstudiantesModels, SecionModels, MateriasModels


# Create your models here.


class NotasProfesor(models.Model):
    materia  = models.ForeignKey(MateriasModels, blank=True, null=True, related_name="materia_cecion_reverce", on_delete=models.CASCADE)
    alunno = models.ForeignKey(EstudiantesModels, blank=True, null=True,  related_name='alunno_reverce', on_delete=models.CASCADE)
    asistencia = models.PositiveIntegerField(blank=True, null=True)
    participacion = models.PositiveIntegerField(blank=True, null=True)
    parcial = models.PositiveIntegerField(blank=True, null=True)
    filnal_ex = models.PositiveIntegerField(blank=True, null=True)
    nota_final = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.alunno.user.nombre