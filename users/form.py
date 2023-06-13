from django import forms
from .models import   EscuelasModels, CarrerasModels, DatosSiEsMilitar,HistorialEducativo, DatosPersonales, User

class DatosForms(forms.ModelForm):
    nombre = forms.ModelMultipleChoiceField(queryset=None, required=True)
    class Meta:
        model = CarrerasModels
        fields = (
            'nombre',
            )

    
    def __init__(self, pk,  *args, **kwars):
        super(DatosForms, self).__init__(*args, **kwars)
        self.fields['nombre'].queryset = CarrerasModels.objects.filter(carreras_reverce__id=pk)
    


class RegistrosForm(forms.ModelForm):
    class Meta:
        model= DatosSiEsMilitar
        fields=('sector_educativo',)
        
        
class HistorialEducativoForm(forms.Form):
    nivel = forms.CharField(widget=forms.TextInput( attrs={"class":"input100","placeholder":"username"}))
    institucion_escuelas=forms.CharField()
    lugar = forms.CharField()
    finalizacion=forms.DateField()
    grado=forms.CharField()
    
    
    
    
    
    # class Meta:
    #     model=HistorialEducativo
    #     fields = ('nivel','institucion_escuelas','lugar','finalizacion','grado')
        
class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model=DatosPersonales
        fields=('militar',)
    
        

class RegistrosEstudiantesForm(forms.Form):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    siglas_escuela=forms.CharField(required=True)
    promocion=forms.CharField(required=True)
    matricula=forms.CharField(required=True)
    fecha=forms.DateField()
    fecha_nacimiento = forms.DateField()
    lugar_nacimiento = forms.CharField(required=True) 
    nacionalidad = forms.CharField(required=True)
    provincia=forms.CharField(required=True)
    municipio=forms.CharField(required=True)
    Secion=forms.CharField(required=True)
    estado_civil=forms.CharField(required=True)
    no_cedula=forms.CharField(required=True)
    telefono_res=forms.CharField(required=True)
    direcion=forms.CharField(required=True)
    celular=forms.CharField(required=True)
    telefono_ofic=forms.CharField(required=True)
    lugar_trabajo=forms.CharField(required=True)
    alguna_discapasidad=forms.CharField(required=True)
    tipo_sangre=forms.CharField(required=True)
    funcion_desenpeña=forms.CharField(required=True)
    correo=forms.EmailField(required=True)
    alergico=forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    militar=forms.BooleanField() 
    rango = forms.CharField(required=True)
    institucion = forms.CharField(required=True)
    fecha_ingreso=forms.DateField()
    ultimo_asenso=forms.DateField()
    nombre_liceo=forms.CharField(required=True)
    sector_educativo=forms.CharField(required=True)
    idiomas_dominas=forms.CharField(required=True)
    nivel=forms.CharField(required=True)
    institucion_escuelas=forms.CharField(required=True)
    lugar=forms.CharField(required=True)
    finalizacion=forms.DateField()
    grado=forms.CharField(required=True)
    padre=forms.CharField(required=True)
    madre=forms.CharField(required=True)
    esposa=forms.CharField(required=True)
    hijo=forms.CharField(required=True)
    felefono=forms.CharField(required=True)
    contacto_emergencia=forms.CharField(required=True)
    
    
    
class AvatarFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar',)

