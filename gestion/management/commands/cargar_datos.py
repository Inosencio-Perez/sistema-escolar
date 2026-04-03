from django.core.management.base import BaseCommand
from gestion.models import Alumno, Profesor, Curso

class Command(BaseCommand):
    help = 'Carga masiva de datos iniciales para el Instituto Nueva Alianza'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Iniciando carga de datos...'))

        # 1. CARGA DE PROFESORES (Agregamos DNI para evitar el IntegrityError)
        profesores_data = [
            {"nombre": "Inosencio", "apellido": "Pérez", "especialidad": "Python", "dni": "1001"},
            {"nombre": "Laura", "apellido": "García", "especialidad": "Matemáticas", "dni": "1002"},
        ]
        
        for p in profesores_data:
            # Usamos el DNI como clave para buscar si ya existe
            prof, created = Profesor.objects.get_or_create(dni=p['dni'], defaults=p)
            if created: 
                self.stdout.write(self.style.SUCCESS(f"Profesor {p['nombre']} creado."))
            else:
                self.stdout.write(f"Profesor {p['nombre']} ya existía.")

        # 2. CARGA DE CURSOS
        cursos_nombres = ["Python Básico", "Django Web", "Bases de Datos"]
        for nombre_curso in cursos_nombres:
            curso, created = Curso.objects.get_or_create(nombre=nombre_curso)
            if created: self.stdout.write(self.style.SUCCESS(f"Curso {nombre_curso} creado."))

        # 3. CARGA DE 22 ALUMNOS
        alumnos_nombres = [
            "Juan Pérez", "María Rodríguez", "Carlos Gómez", "Ana Martínez",
            "Luis Hernández", "Elena Díaz", "Pedro Sánchez", "Lucía Álvarez",
            "Jorge Moreno", "Sofía Castro", "Miguel Romero", "Valeria Ruiz",
            "Diego Alonso", "Paula Gutiérrez", "Andrés Navarro", "Marta Serrano",
            "Tomás Ramos", "Sara Blanco", "Felipe Molina", "Julia Morales",
            "Kevin Ortiz", "Ariel Vazquez"
        ]

        for i, full_name in enumerate(alumnos_nombres):
            partes = full_name.split(" ", 1)
            nombre = partes[0]
            apellido = partes[1] if len(partes) > 1 else ""
            
            # Generamos un DNI ficticio para cada alumno (ej: 2001, 2002...)
            dni_alumno = str(2000 + i)
            
            alum, created = Alumno.objects.get_or_create(
                dni=dni_alumno, 
                defaults={'nombre': nombre, 'apellido': apellido}
            )
            if created: 
                self.stdout.write(f"Alumno {full_name} creado.")

        self.stdout.write(self.style.SUCCESS('¡Todo listo, Ino! Datos cargados.'))