# Changelog

## [2.1.0] — 2026-04-09

### Nuevo
- **Soporte multiidioma**: la app ahora está disponible en español e inglés; se cambia desde el menú «Idioma / Language»
- **Globos de error en el registro**: si la contraseña es corta o las dos contraseñas no coinciden, aparece un globo rojo justo debajo del campo con el mensaje de error
- **Ventana de registro redimensionable**: la ventana se amplía automáticamente (660 px) al pasar al formulario de registro y vuelve a su tamaño original (520 px) al volver al login, para que todos los campos sean siempre visibles
- **Botón «← Ya tengo cuenta»** siempre visible en la pantalla de creación de cuenta

### Mejorado
- «v2.1» visible en el pie de la ventana de login y de la ventana principal
- Código de internacionalización centralizado en `lang.py`

---

## [2.0.0] — 2026-04-07

### Nuevo
- Sistema multi-usuario: cada usuario tiene su propia cuenta y lista de tareas independiente
- Pantalla de login con formularios de acceso y registro en la misma ventana
- Autenticación segura con bcrypt (rounds=12)
- **Cifrado de tareas**: archivos `tasks.json` cifrados con Fernet (clave derivada de la contraseña via PBKDF2)
- Datos de cada usuario almacenados en `users_data/{usuario}/tasks.json`
- Migración automática de tareas desde MisTareas 1.0
- **Selector de usuario**: pie de la app con nombre del usuario activo y cambio de usuario sin cerrar la app
- Opción "Cerrar sesión" en el menú de la aplicación
- Arquitectura modular: `config`, `auth`, `data`, `ui`
- Documentación completa con MkDocs Material
- GitHub Actions para despliegue automático de la documentación y publicación de releases

### Mejorado
- Menús diferenciados por plataforma (Windows y macOS)
- Escritura atómica en todos los archivos de datos (via `.tmp` + `os.replace()`)
- Aviso al usuario si el archivo de tareas está corrupto al cargar
- Acerca de: nombre completo del autor y contacto

---

## [1.0.0] — 2026-03-29 *(MisTareas 1.0)*

### Funcionalidades iniciales
- Crear, completar y eliminar tareas
- Registro de fecha y hora de creación y finalización
- Sistema de prioridades con reordenación automática
- Drag & drop con animaciones (ghost window, smoothstep)
- Navegación con teclado (↑↓)
- Ventana siempre visible (pin)
- Menú contextual ⋮
- Persistencia local en `tasks.json`
- Instalador Windows con Inno Setup
