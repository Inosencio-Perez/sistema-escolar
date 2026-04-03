from django.core.management.base import BaseCommand
from gestion.models import Profesor, Curso

class Command(BaseCommand):
    help = 'Carga un equipo docente completo y los asigna a los cursos'

    def handle(self, *args, **kwargs):
        profesores_data = [
            {'nombre': 'Carlos', 'apellido': 'Duarte', 'dni': '30111222', 'especialidad': 'Bases de Datos', 'email': 'carlos@escuela.com'},
            {'nombre': 'Marina', 'apellido': 'Silva', 'dni': '35444555', 'especialidad': 'Desarrollo Web', 'email': 'marina@escuela.com'},
            {'nombre': 'Roberto', 'apellido': 'Gómez', 'dni': '28777888', 'especialidad': 'Python Avanzado', 'email': 'roberto@escuela.com'},
            {'nombre': 'Luciana', 'apellido': 'Paz', 'dni': '40999000', 'especialidad': 'Frontend', 'email': 'luciana@escuela.com'},
        ]

        self.stdout.write('Cargando nuevos profesores...')
        
        for p in profesores_data:
            profesor, created = Profesor.objects.get_or_create(
                dni=p['dni'],
                defaults=p
            )
            if created:
                self.stdout.write(f'Profesor {profesor.nombre} {profesor.apellido} creado.')

        # Asignación automática a los cursos existentes
        self.stdout.write('Asignando profesores a cursos...')
        
        cursos = Curso.objects.all()
        profs = Profesor.objects.all()

        if cursos.exists():
            for i, curso in enumerate(cursos):
                # Asignamos un profesor diferente a cada curso usando el índice
                curso.profesor = profs[i % profs.count()]
                curso.save()
                self.stdout.write(f'Curso "{curso.nombre}" asignado a {curso.profesor}')

        self.stdout.write(self.style.SUCCESS('¡Equipo docente actualizado y cursos asignados!'))