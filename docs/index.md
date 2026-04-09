# MisTareas 2.0

**MisTareas 2.0** es una aplicación de escritorio multi-usuario para gestionar listas de tareas, desarrollada en Python con CustomTkinter.

## Características principales

- **Multi-usuario**: cada usuario tiene su propia cuenta con lista de tareas independiente
- **Autenticación segura**: contraseñas protegidas con bcrypt
- **Tareas cifradas**: archivos de tareas cifrados con Fernet (clave derivada de la contraseña via PBKDF2)
- **Cambio de usuario**: selector en el pie de la app para cambiar de usuario sin cerrar
- **Multiidioma**: interfaz disponible en español e inglés (menú «Idioma / Language»)
- **Gestión completa de tareas**: crear, completar, eliminar y priorizar
- **Ordenación por arrastre**: reordena tareas arrastrando con el ratón
- **Timestamps automáticos**: registro de fecha y hora de creación y finalización
- **Ventana siempre visible**: opción de mantener la app encima de otras ventanas
- **Compatible con Windows y macOS**

## Descargas

| Archivo | Descripción |
|---------|-------------|
| [Installer_MisTareas2.1.exe](https://github.com/Fabianviera/MisTareas2.0/releases/latest/download/Installer_MisTareas2.1.exe) | Instalador para Windows (recomendado) |
| [MisTareas2.1.exe](https://github.com/Fabianviera/MisTareas2.0/releases/latest/download/MisTareas2.1.exe) | Ejecutable portable (sin instalación) |

## Novedades respecto a la versión 1.0

| Funcionalidad | v1.0 | v2.0 |
|---|---|---|
| Multi-usuario | No | Sí |
| Pantalla de login | No | Sí |
| Contraseñas seguras (bcrypt) | No | Sí |
| Tareas cifradas (Fernet/PBKDF2) | No | Sí |
| Datos separados por usuario | No | Sí |
| Cambio de usuario sin cerrar | No | Sí |
| Migración de datos anteriores | No | Sí |
| Arquitectura modular | No | Sí |

## Tecnologías

- **Python 3.12**
- **CustomTkinter** — interfaz gráfica moderna
- **bcrypt** — hashing seguro de contraseñas
- **cryptography** — cifrado Fernet de archivos de tareas
- **PyInstaller** — compilación a ejecutable
- **Inno Setup** — instalador Windows

## Capturas de pantalla

=== "Pantalla de login"
    La pantalla de acceso permite iniciar sesión o crear una cuenta nueva desde la misma ventana.

=== "Lista de tareas"
    Vista principal con tareas organizadas por prioridad, checkboxes y opciones de ordenación.
