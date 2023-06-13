from django.contrib import admin
from .models import User, DirectorModels, EscuelasModels,  EstudiantesModels, ProfesoresModels, SemestreModels, SecionModels, MateriasModels, Notamodels, CarrerasModels, DatosPersonales, DatosSiEsMilitar, DatosFamiliares, HistorialEducativo


# Register your models here.

admin.site.register(User)
admin.site.register(DirectorModels)
admin.site.register(EscuelasModels)
admin.site.register(EstudiantesModels)
admin.site.register(ProfesoresModels)
admin.site.register(SemestreModels)
admin.site.register(SecionModels)
admin.site.register(MateriasModels)
admin.site.register(Notamodels)
admin.site.register(CarrerasModels)
admin.site.register(DatosPersonales)
admin.site.register(DatosFamiliares)
admin.site.register(DatosSiEsMilitar)
admin.site.register(HistorialEducativo)