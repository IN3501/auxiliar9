from django.contrib import admin
from .models import *

# Register your models here.
class CursosAdmin(admin.ModelAdmin):
    list_display=('nombre', 'id')
    readonly_fields = ('id',)
    fieldsets = [
        (None, {'fields':['id', 'nombre']}),
        ('Administrativo', {'fields': ['ud','codigo','horario']}),
    ]


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Departamento)
admin.site.register(RolUsuarioCurso)
admin.site.register(Semestres)
admin.site.register(TipoUsuario)
admin.site.register(UsuarioTipoUsuario)
admin.site.register(Usuarios)

