from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Profesores"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    # Relación uno a muchos: Un profesor tiene muchos cursos
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name='cursos')
    
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    fecha_inscripcion = models.DateField(auto_now_add=True)
    # Relación muchos a muchos: Un alumno en varios cursos, un curso con varios alumnos
    cursos = models.ManyToManyField(Curso, related_name='alumnos', blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class ConfiguracionEscuela(models.Model):
    nombre = models.CharField(max_length=100, default="Mi Escuela Pro")
    logo = models.ImageField(upload_to='escuela/', null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Configuración de la Escuela"
        verbose_name_plural = "Configuración de la Escuela"

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        # Este truco asegura que solo exista un registro en la tabla
        if not self.pk and ConfiguracionEscuela.objects.exists():
            return 
        return super().save(*args, **kwargs)
