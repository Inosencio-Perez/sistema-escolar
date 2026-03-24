from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    profesor = models.CharField(max_length=100)
    archivo_temario = models.FileField(
        upload_to='temarios/', 
        blank=True, 
        null=True,
        verbose_name="Material de estudio / Temario"
    )

    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # Cambiamos la relación para usar el modelo intermedio 'Inscripcion'
    cursos = models.ManyToManyField(Curso, through='Inscripcion', related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    # Nota del alumno en este curso (del 1 al 10 o al 100)
    nota = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        # Evita que un alumno se inscriba dos veces al mismo curso
        unique_together = ('alumno', 'curso')


    def __str__(self):
        return f"{self.alumno} en {self.curso} - Nota: {self.nota}"
    

class ConfiguracionEscuela(models.Model):
    nombre_escuela = models.CharField(max_length=100, default="Mi Institución Educativa")
    logo = models.ImageField(upload_to='escuela/', blank=True, null=True)
    eslogan = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Configuración de la Escuela"
        verbose_name_plural = "Configuración de la Escuela"

    def __str__(self):
        return self.nombre_escuela