from django.forms import ModelForm
from django import forms
from .models import NotasProfesor

class RegistroNotaForm(ModelForm):
    class Meta:
        model = NotasProfesor
        fields = ('asistencia','participacion','parcial', 'filnal_ex','nota_final')
        