from django.contrib import admin

# Register your models here.
from .models import Constancia

from unfold.admin import ModelAdmin


from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ConstanciaResource(resources.ModelResource):
    class Meta:
        model = Constancia
        exclude = ('id', 'created_at', 'updated_at',)  # ⛔ No se importan

@admin.register(Constancia)
class ConstanciaAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('noControl', 'nombre', 'apellidoPaterno', 'apellidoMaterno', 'semestre', 'claveCarrera', 'carrera', 'fechaInscripcion', 'horaInscripcion', 'titulo', 'noConsecutivo', 'promedio', 'avance', 'creditosAprobados')
    actions=["ConstanciaPDF"]
    resource_class = ConstanciaResource


