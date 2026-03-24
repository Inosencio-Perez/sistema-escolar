from .models import ConfiguracionEscuela

def datos_escuela(request):
    config = ConfiguracionEscuela.objects.first()
    if not config:
        # Valor por defecto si no han creado la configuración en el admin
        return {'NOMBRE_ESCUELA': "Gestión Académica"}
    return {'NOMBRE_ESCUELA': config.nombre_escuela}