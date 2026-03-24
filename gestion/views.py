from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Count, Avg
from .models import Curso, Alumno 

# Importaciones para el PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def home(request):
    busqueda = request.GET.get('buscar')
    
    # Lógica de búsqueda
    if busqueda:
        cursos = Curso.objects.filter(
            Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)
        ).distinct()
    else:
        cursos = Curso.objects.all()

    # --- CÁLCULO DE ESTADÍSTICAS CORREGIDO (POR INSCRIPCIONES) ---
    total_cursos = Curso.objects.count()
    
    # Sumamos la cantidad de alumnos que tiene cada curso individualmente
    # Esto nos da el total de "asientos ocupados" (3 + 2 = 5)
    total_inscripciones = 0
    for curso in Curso.objects.all():
        total_inscripciones += curso.alumnos.count()
    
    # Calculamos el promedio basado en inscripciones reales
    if total_cursos > 0:
        promedio_alumnos = total_inscripciones / total_cursos
    else:
        promedio_alumnos = 0

    context = {
        'cursos': cursos,
        'busqueda': busqueda,
        'stats': {
            'total_cursos': total_cursos,
            'total_alumnos': total_inscripciones, # Ahora muestra 5
            'promedio': round(float(promedio_alumnos), 1)
        }
    }
    return render(request, 'gestion/home.html', context)

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    return render(request, 'gestion/detalle_curso.html', {'curso': curso})

def exportar_alumnos_pdf(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="alumnos_{curso.nombre}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, f"Lista de Alumnos: {curso.nombre}")
    
    p.setFont("Helvetica", 12)
    y = 720
    for alumno in curso.alumnos.all():
        p.drawString(100, y, f"- {alumno.nombre} {alumno.apellido} ({alumno.email})")
        y -= 20
    
    p.showPage()
    p.save()
    return response