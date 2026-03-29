from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    path('curso/<int:curso_id>/pdf/', views.exportar_alumnos_pdf, name='exportar_alumnos_pdf'),
]