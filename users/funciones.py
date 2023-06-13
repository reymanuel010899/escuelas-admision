from django.shortcuts import redirect
from .models import DatosPersonales, DatosSiEsMilitar, DatosFamiliares, HistorialEducativo


def  definir_militar(form_is_militar):
    if form_is_militar.is_valid():
        activo_o_no = form_is_militar.cleaned_data['militar']
        return activo_o_no
    return False

def buscar_sector(form_sector):
    if form_sector.is_valid():
        sector = form_sector.cleaned_data['sector_educativo']
        return sector
    return 'p'

def guardar_historial(form_historia):
    if form_historia.is_valid():
        form_historia.save()
        print(form_historia)
        # return form_historia
 


def registrar_datos(request, estudiante, form_is_militar, form_sector, form_historia):
    siglas_escuela = request.POST.get('sigla-escuela','')
    promocion = request.POST.get('promocion','')
    matricula = request.POST.get('matricula','')
    fecha_actual = request.POST.get('fecha-actual','')
    nombre = request.POST.get('nombre','')
    apellido = request.POST.get('apellido','')
    fecha_nacimiento = request.POST.get('fecha-nacimiento','')
    lugar_nacimiento = request.POST.get('lugar-nacimiento','')
    nacionalidad = request.POST.get('nacionalidad','')
    provincia = request.POST.get('provincia','')
    municipio = request.POST.get('municipio','')
    secion = request.POST.get('secion','')
    estado_civil = request.POST.get('estado-civil','')
    cedula = request.POST.get('cedula','')
    telefono_res = request.POST.get('telefono-res','')
    telefono_ofi = request.POST.get('telefono-ofi','')
    direcion = request.POST.get('direcion','')
    celular = request.POST.get('celular','')
    lugar_trabajo = request.POST.get('lugar-trabajo','')
    discapasidad = request.POST.get('discapasidad','')
    sangre = request.POST.get('sangre','')
    funcion_desenpeña = request.POST.get('funcion-desenpeña','')
    sexo = request.POST.get('sexo','')
    correo = request.POST.get('correo','')
    alergico = request.POST.get('alergico','')
    militar_o_no = definir_militar(form_is_militar)
    estudiante.user.nombre=nombre
   
    DatosPersonales.objects.create(estudiante=estudiante,
                                    siglas_escuela=siglas_escuela,
                                    promocion=promocion, matricula=matricula, fecha=fecha_actual,
                                    fecha_nacimiento=fecha_nacimiento, lugar_nacimiento=lugar_nacimiento, 
                                    nacionalidad=nacionalidad, provincia=provincia, 
                                    municipio=municipio, Secion=secion,
                                    estado_civil=estado_civil, no_cedula=cedula,
                                    telefono_res=telefono_res,direcion=direcion,
                                    celular=celular, telefono_ofic=telefono_ofi,
                                    lugar_trabajo=lugar_trabajo,
                                    alguna_discapasidad=discapasidad,
                                    tipo_sangre=sangre, funcion_desenpeña=funcion_desenpeña,
                                    correo=correo, alergico=alergico, sexo=sexo, militar=militar_o_no)
    
    if militar_o_no:
        rango = request.POST.get('rango','')
        institucion = request.POST.get('institucion','')
        fecha_ingreso = request.POST.get('fecha-ingreso','')
        ultimo_ascenso = request.POST.get('ultimo-ascenso','')
        nombre_educativo = request.POST.get('nombre-educativo','')
        idiomas = request.POST.get('idiomas','')
        sector_educativo = buscar_sector(form_sector)
        DatosSiEsMilitar.objects.create(estudiante=estudiante, rango=rango,
                                        institucion=institucion,
                                        fecha_ingreso=fecha_ingreso,
                                        ultimo_asenso=ultimo_ascenso, nombre_liceo=nombre_educativo,
                                        sector_educativo=sector_educativo, idiomas_dominas=idiomas)
        
        
        padre = request.POST.get('padre')
        madre = request.POST.get('madre')
        esposa = request.POST.get('esposa')   
        hijo  = request.POST.get('hijos')   
        telefono = request.POST.get('telefono')
        contacto = request.POST.get('telefono-emergencia')
        
        
        DatosFamiliares.objects.create(estudiante=estudiante,
                                       padre=padre, madre=madre,
                                       esposa=esposa, hijos=hijo,
                                       telefono=telefono, contacto_emergencia=contacto)
        
        
   
        if form_historia.is_valid():
            nivel= form_historia.cleaned_data['nivel']
            institucion_escuela =form_historia.cleaned_data['institucion_escuelas']
            lugar= form_historia.cleaned_data['lugar']
            finalizacion=form_historia.cleaned_data['finalizacion']
            grado=form_historia.cleaned_data['grado']
         
            
            
            HistorialEducativo.objects.create(estudiante=estudiante,nivel=nivel,
                                              institucion_escuelas=institucion_escuela,
                                              lugar=lugar, finalizacion=finalizacion, grado=grado )
            return redirect('/')
        print('no es valido')