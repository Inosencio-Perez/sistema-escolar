from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion.urls')), # Esto conecta tu página principal
    path('accounts/', include('django.contrib.auth.urls')),
]