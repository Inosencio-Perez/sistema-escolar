from django.contrib import admin
from .models import Curso, Alumno, Inscripcion, ConfiguracionEscuela

# --- ESTO ES LO NUEVO PARA LA CONFIGURACIÓN ---
@admin.register(ConfiguracionEscuela)
class ConfiguracionEscuelaAdmin(admin.ModelAdmin):
    # Esto evita que se creen múltiples registros accidentalmente
    def has_add_permission(self, request):
        if ConfiguracionEscuela.objects.exists():
            return False
        return True

    # Esto evita que se pueda borrar la configuración una vez creada
    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('nombre_escuela', 'eslogan')

# --- TUS REGISTROS ANTERIORES (MANTENLOS IGUAL) ---
class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor', 'archivo_temario')
    search_fields = ('nombre', 'profesor')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email')
    search_fields = ('nombre', 'apellido', 'email')
    inlines = [InscripcionInline]

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'nota', 'fecha_inscripcion')
    list_filter = ('curso', 'fecha_inscripcion')