from django import forms
from .models import   EscuelasModels, CarrerasModels

class DatosForms(forms.ModelForm):
    nombre = forms. ModelMultipleChoiceField(queryset=None, required=True)
    class Meta:
        model = CarrerasModels
        fields = (
            'nombre',
            )

    
    def __init__(self, pk,  *args, **kwars):
        super(DatosForms, self).__init__(*args, **kwars)
        self.fields['nombre'].queryset = CarrerasModels.objects.filter(carreras_reverce__id=pk)
        

