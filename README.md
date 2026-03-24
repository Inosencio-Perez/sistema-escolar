# 🎓 EduCore Manager | Sistema de Gestión Académica

Un robusto sistema de **Back-office** desarrollado con **Django** y **MySQL** para la administración interna de instituciones educativas. Este software permite la gestión centralizada de alumnos, cursos y calificaciones, optimizando el flujo de trabajo administrativo y la transparencia académica.

## 🚀 Funcionalidades Destacadas

* **Configuración Dinámica (Marca Blanca):** Identidad de la institución (Nombre, Eslogan) personalizable directamente desde el panel administrativo mediante un Context Processor global.
* **Sistema de Calificaciones Visual:** Listado de alumnos con indicadores de notas mediante insignias de colores dinámicas (Verde: Aprobado, Amarillo: En Proceso, Rojo: Reprobado).
* **Gestión de Material Académico:** Interfaz para la carga de temarios en PDF y descarga directa desde el dashboard de cada curso.
* **Reportes Académicos en PDF:** Generación automática de listas de asistencia y actas de notas profesionales utilizando la librería **ReportLab**.
* **Panel Administrativo Avanzado:** Configuración de `Inlines` en el Admin de Django para permitir la carga de notas de alumnos directamente desde la edición del curso.
* **Diseño Responsivo:** Interfaz moderna construida con Bootstrap 5.3, adaptable a dispositivos móviles y escritorio.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.12+ & Django Framework
* **Base de Datos:** MySQL (Relacional)
* **Frontend:** Bootstrap 5.3.3, Bootstrap Icons & Google Fonts (Inter)
* **Generación de Documentos:** ReportLab (PDFs dinámicos)

## 📂 Estructura del Proyecto

```bash
## 📂 Estructura del Proyecto

SISTEMA_ESCOLAR/              # Carpeta raíz del proyecto
├── config/                   # Configuración principal de Django (settings, urls)
├── gestion/                  # Aplicación de lógica de negocio
│   ├── migrations/           # Historial de versiones de la base de datos
│   ├── admin.py              # Personalización del Panel Administrativo
│   ├── context_processors.py # Inyección global del nombre de la escuela
│   ├── models.py             # Modelos relacionales (Curso, Alumno, Inscripcion)
│   ├── views.py              # Vistas y generación de reportes PDF
│   └── ...                   # Archivos internos de la aplicación
├── media/                    # Archivos multimedia y documentos subidos
├── templates/                # Plantillas HTML globales (base.html)
├── venv/                     # Entorno virtual de Python
├── .env                      # Variables de entorno (Seguridad)
├── .gitignore                # Archivos excluidos del control de versiones
├── manage.py                 # Utilidad de comandos de Django
├── poblar_datos.py           # Script para carga inicial de datos de prueba
├── requirements.txt          # Listado de dependencias y librerías
└── README.md                 # Documentación del proyecto (este archivo)
```


## 📦 Instalación y Configuración

Sigue estos pasos para replicar el entorno de desarrollo:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/educore-manager.git
    cd educore-manager
    ```

2.  **Configurar el Entorno Virtual:**
    ```bash
    python -m venv venv
    # Activar en Windows:
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

5.  **Configurar el Administrador:**
    Crea un usuario con acceso total para gestionar la escuela:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Lanzar la aplicación:**
    ```bash
    python manage.py runserver
    ```
    Accede a `http://127.0.0.1:8000/` para el dashboard o a `/admin` para configurar el nombre de tu escuela.

---
Desarrollado con ❤️ por **Inosencio** - 2026