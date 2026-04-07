# MisTareas 2.0

**MisTareas 2.0** es una aplicación de escritorio multi-usuario para gestionar listas de tareas, desarrollada en Python con CustomTkinter.

## Características principales

- **Multi-usuario**: cada usuario tiene su propia cuenta con lista de tareas independiente
- **Autenticación segura**: contraseñas protegidas con bcrypt
- **Gestión completa de tareas**: crear, completar, eliminar y priorizar
- **Ordenación por arrastre**: reordena tareas arrastrando con el ratón
- **Timestamps automáticos**: registro de fecha y hora de creación y finalización
- **Ventana siempre visible**: opción de mantener la app encima de otras ventanas
- **Compatible con Windows y macOS**

## Novedades respecto a la versión 1.0

| Funcionalidad | v1.0 | v2.0 |
|---|---|---|
| Multi-usuario | No | Sí |
| Pantalla de login | No | Sí |
| Contraseñas seguras (bcrypt) | No | Sí |
| Datos separados por usuario | No | Sí |
| Migración de datos anteriores | No | Sí |
| Arquitectura modular | No | Sí |

## Tecnologías

- **Python 3.12**
- **CustomTkinter** — interfaz gráfica moderna
- **bcrypt** — hashing seguro de contraseñas
- **PyInstaller** — compilación a ejecutable
- **Inno Setup** — instalador Windows

## Capturas de pantalla

=== "Pantalla de login"
    La pantalla de acceso permite iniciar sesión o crear una cuenta nueva desde la misma ventana.

=== "Lista de tareas"
    Vista principal con tareas organizadas por prioridad, checkboxes y opciones de ordenación.
