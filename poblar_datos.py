import os
import django

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gestion.models import Alumno, Profesor, Curso
from datetime import date

def poblar():
    print("Iniciando la carga de datos de prueba...")

    # 1. Crear Profesores
    prof1, _ = Profesor.objects.get_or_create(
        nombre="Guido", apellido="van Rossum", 
        email="guido@python.org", especialidad="Backend con Django"
    )
    prof2, _ = Profesor.objects.get_or_create(
        nombre="Ada", apellido="Lovelace", 
        email="ada@computacion.com", especialidad="Algoritmos y Lógica"
    )

    # 2. Crear Alumnos
    alumnos_datos = [
        ("Juan", "Pérez", "ALU001", "2005-05-15"),
        ("María", "García", "ALU002", "2004-10-20"),
        ("Carlos", "Sánchez", "ALU003", "2006-01-10"),
    ]

    lista_alumnos = []
    for nom, ape, mat, fec in alumnos_datos:
        alu, _ = Alumno.objects.get_or_create(
            nombre=nom, apellido=ape, matricula=mat, 
            email=f"{nom.lower()}@escuela.com",
            fecha_nacimiento=fec
        )
        lista_alumnos.append(alu)

    # 3. Crear Cursos y asignar Profesores
    curso1, _ = Curso.objects.get_or_create(
        nombre="Master en Python 3", 
        descripcion="Aprende desde las bases hasta POO avanzada.",
        profesor=prof1
    )
    curso2, _ = Curso.objects.get_or_create(
        nombre="Bases de Datos con MySQL", 
        descripcion="Diseño relacional y optimización de consultas SQL.",
        profesor=prof2
    )

    # 4. Inscribir Alumnos a los cursos (Many-to-Many)
    curso1.alumnos.add(*lista_alumnos) # Inscribe a todos en el curso 1
    curso2.alumnos.add(lista_alumnos[0], lista_alumnos[1]) # Solo a Juan y María en el curso 2

    print("--- ¡Éxito! Datos creados y relacionados correctamente ---")

if __name__ == '__main__':
    poblar()