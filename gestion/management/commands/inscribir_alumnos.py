import random
from django.core.management.base import BaseCommand
from gestion.models import Alumno, Curso

class Command(BaseCommand):
    help = 'Asocia alumnos existentes a cursos de manera aleatoria'

    def handle(self, *args, **kwargs):
        alumnos = Alumno.objects.all()
        cursos = list(Curso.objects.all())

        if not alumnos or not cursos:
            self.stdout.write(self.style.ERROR('Faltan alumnos o cursos en la base de datos.'))
            return

        self.stdout.write('Iniciando proceso de asociación...')
        contador = 0

        for alumno in alumnos:
            # Elegimos 1 o 2 cursos al azar de la lista
            cantidad = random.randint(1, 2)
            cursos_a_asignar = random.sample(cursos, k=min(len(cursos), cantidad))
            
            # Usamos .add() para agregar los cursos al alumno
            # Django se encarga de no duplicar si ya estaba inscripto
            alumno.cursos.add(*cursos_a_asignar)
            contador += len(cursos_a_asignar)

        self.stdout.write(self.style.SUCCESS(f'¡Éxito! Se realizaron {contador} asociaciones de alumnos a cursos.'))