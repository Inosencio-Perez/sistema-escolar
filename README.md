# 🎓 Sistema de Gestión Escolar - Instituto Nueva Alianza

**Este es un sistema integral de gestión educativa desarrollado con **Django 6.0**, diseñado para centralizar la administración de alumnos, cursos y profesores en una plataforma ágil y moderna.**

## 🚀 Características Principales
* **Dashboard Interactivo:** Visualización en tiempo real de métricas clave (Total de alumnos, cursos activos y docentes).
* **Gestión de Alumnos:** Registro completo, edición y visualización de perfiles estudiantiles.
* **Administración de Cursos:** Organización jerárquica de la oferta académica.
* **Arquitectura Limpia:** Estructura de proyecto optimizada siguiendo las mejores prácticas de Django.
* **Base de Datos Robusta:** Implementación profesional con **MySQL**.

## 📂 Estructura del Proyecto (Árbol de Directorios)
```text
sistema_escolar/
├── config/                  # Configuración central del proyecto
│   ├── settings.py          # Ajustes principales (Base de datos, Apps, Middleware)
│   ├── urls.py              # Enrutamiento principal
│   └── wsgi.py              # Interfaz de servidor web
├── gestion/                 # Aplicación principal del sistema
│   ├── migrations/          # Historial de cambios en la base de datos
│   ├── admin.py             # Configuración del panel de administración
│   ├── models.py            # Definición de tablas (Alumnos, Cursos, Profesores)
│   ├── views.py             # Lógica de las páginas y el dashboard
│   └── urls.py              # Rutas específicas de la aplicación
├── templates/               # Plantillas HTML
│   ├── base.html            # Plantilla maestra con Footer y Navbar
│   └── gestion/             # Páginas específicas (dashboard.html, alumnos.html)
├── static/                  # Archivos estáticos (CSS, JS, Imágenes)
├── manage.py                # Utilidad de línea de comandos de Django
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del sistema
```

## 🛠️ Tecnologías Utilizadas

* Lenguaje: Python 3.14

* Framework Web: Django 6.0.3

* Base de Datos: MySQL (con integración mysqlclient)

* Frontend: HTML5, CSS3, Bootstrap 5 (Diseño responsive)

* Control de Versiones: Git & GitHub


## 📦 Instalación y Configuración

Sigue estos pasos para replicar el entorno de desarrollo:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/sistema_escolar.git](https://github.com/tu-usuario/sistema_escolar.git)
    ```

2.  **Configurar el Entorno Virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la Base de Datos:**
    Crea una base de datos en MySQL y actualiza las credenciales en `sistema_escolar/settings.py`. Luego, ejecuta las migraciones:
    ```bash
    python manage.py migrate
    ```

5.  **Lanzar la aplicación:**
    ```bash
    python manage.py runserver
    ```
    Accede a `http://127.0.0.1:8000/` para el dashboard o a `/admin`

## 🌐 Demo en Vivo (Próximamente)


* El sistema será desplegado en PythonAnywhere.

* Estado: En proceso de despliegue.

* Usuario Invitado (Reclutadores): invitado (Próximamente disponible).


---
Desarrollado con ❤️ por **Inosencio** - 2026