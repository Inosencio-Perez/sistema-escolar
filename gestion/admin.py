from django.contrib import admin
from .models import Alumno, Profesor, Curso, ConfiguracionEscuela

# --- CONFIGURACIÓN DE LA ESCUELA ---
@admin.register(ConfiguracionEscuela)
class ConfiguracionEscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    
    # Esto evita que se creen múltiples configuraciones
    def has_add_permission(self, request):
        if ConfiguracionEscuela.objects.exists():
            return False
        return True

    # Esto evita que se borre la configuración accidentalmente
    def has_delete_permission(self, request, obj=None):
        return False

# --- PROFESORES ---
@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'especialidad', 'email')
    search_fields = ('apellido', 'nombre', 'dni', 'especialidad')
    list_filter = ('especialidad',)
    ordering = ('apellido',)

# --- ALUMNOS ---
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'email')
    search_fields = ('apellido', 'nombre', 'dni')
    filter_horizontal = ('cursos',) # Esto hace que asignar cursos sea mucho más fácil (interfaz de dos columnas)
    ordering = ('apellido',)

# --- CURSOS ---
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesor')
    search_fields = ('nombre',)
    list_filter = ('profesor',)