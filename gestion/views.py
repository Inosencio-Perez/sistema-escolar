from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Alumno, Profesor, Curso

# Intentamos importar xhtml2pdf para el reporte
try:
    from xhtml2pdf import pisa
except ImportError:
    pisa = None

# --- DASHBOARD PRINCIPAL ---
def home(request):
    cursos_activos = Curso.objects.count()
    total_inscripciones = Alumno.objects.filter(cursos__isnull=False).count()
    
    promedio_inscriptos = total_inscripciones / cursos_activos if cursos_activos > 0 else 0

    # Obtenemos los últimos cursos para las tarjetas
    ultimos_cursos = Curso.objects.all().order_by('-id')[:6]

    context = {
        'cursos_activos': cursos_activos,
        'total_inscripciones': total_inscripciones,
        'promedio_inscriptos': round(promedio_inscriptos, 1),
        'cursos': ultimos_cursos,
    }
    return render(request, 'gestion/home.html', context)

# --- VISTAS DE LISTADOS ---
def lista_alumnos(request):
    alumnos = Alumno.objects.all().order_by('apellido')
    return render(request, 'gestion/lista_alumnos.html', {'alumnos': alumnos})

def lista_profesores(request):
    profesores = Profesor.objects.all().order_by('apellido')
    return render(request, 'gestion/lista_profesores.html', {'profesores': profesores})

def lista_cursos(request):
    cursos = Curso.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_cursos.html', {'cursos': cursos})

# --- DETALLES Y PDF ---
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    alumnos_inscritos = Alumno.objects.filter(cursos=curso).order_by('apellido')
    return render(request, 'gestion/detalle_curso.html', {
        'curso': curso,
        'alumnos': alumnos_inscritos,
        'total_inscriptos': alumnos_inscritos.count(),
    })

def exportar_alumnos_pdf(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    alumnos = Alumno.objects.filter(cursos=curso).order_by('apellido')
    template_path = 'gestion/exportar_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="lista_{curso.nombre}.pdf"'
    template = get_template(template_path)
    html = template.render({'curso': curso, 'alumnos': alumnos})
    if pisa:
        pisa_status = pisa.CreatePDF(html, dest=response)
        return response if not pisa_status.err else HttpResponse('Error', status=500)
    return HttpResponse('Instala xhtml2pdf')