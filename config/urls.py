"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# Importamos las configuraciones de Django para manejar archivos
from django.conf import settings
from django.conf.urls.static import static

# Importamos las funciones de views.py
from gestion.views import home, detalle_curso, exportar_alumnos_pdf

urlpatterns = [
    # 1. Panel de Administración de Django
    path('admin/', admin.site.urls),
    
    # 2. Sistema de Autenticación (Login/Logout)
    path('accounts/', include('django.contrib.auth.urls')),

    # 3. Página de Inicio (Catálogo de Cursos + Buscador)
    path('', home, name='home'),

    # 4. Vista de Detalles de un Curso específico
    path('curso/<int:curso_id>/', detalle_curso, name='detalle_curso'),

    # 5. Generador de PDF para la lista de alumnos
    path('curso/<int:curso_id>/pdf/', exportar_alumnos_pdf, name='exportar_pdf'),
]

# Permite que Django sirva los archivos PDF/Media en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)