# Arquitectura

## Estructura del proyecto

```
MisTareas2.0/
├── main.py                  # Punto de entrada
├── config.py                # Constantes globales y paleta de colores
├── requirements.txt         # Dependencias
├── .github/
│   └── workflows/
│       └── docs.yml         # GitHub Actions: despliegue de documentación
├── auth/
│   ├── __init__.py
│   ├── hasher.py            # Hash y verificación de contraseñas (bcrypt)
│   ├── models.py            # Dataclass Usuario
│   └── store.py             # CRUD de usuarios en users.json
├── data/
│   ├── __init__.py
│   └── task_store.py        # Persistencia de tareas por usuario
├── ui/
│   ├── __init__.py
│   ├── login_window.py      # Pantalla de login y registro
│   └── main_window.py       # Ventana principal de la app
└── users_data/              # Creado en runtime (no en el repo)
    ├── users.json           # Registro de usuarios y hashes
    └── {usuario}/
        └── tasks.json       # Tareas de cada usuario
```

---

## Módulos

### `config.py`

Centraliza todo lo que es compartido entre módulos:

- Paleta de colores `C` (diccionario con todos los colores de la UI)
- `DIR_BASE` — directorio raíz de la app (funciona tanto en desarrollo como compilado con PyInstaller)
- `_ahora()` — devuelve la fecha y hora actual formateada

### `auth/`

Capa de autenticación completamente independiente de la UI.

| Archivo | Responsabilidad |
|---|---|
| `hasher.py` | Genera y verifica hashes bcrypt |
| `models.py` | Dataclass `Usuario` |
| `store.py` | Lee/escribe `users_data/users.json` |

**Flujo de autenticación:**

```
VentanaLogin → auth.store.autenticar()
                    ↓
              buscar_usuario()  →  users.json
                    ↓
              hasher.verificar_password()  →  bcrypt.checkpw()
                    ↓
              actualizar_ultimo_login()
                    ↓
              MisTareasApp(nombre_usuario)
```

### `data/task_store.py`

Gestiona la persistencia de tareas. Todas las funciones son puras (no tienen estado interno).

- `obtener_archivo_tareas(usuario)` — devuelve la ruta `users_data/{usuario}/tasks.json`
- `guardar_tareas(tareas, usuario)` — escritura atómica via archivo `.tmp` + `os.replace()`
- `cargar_tareas(usuario)` — carga con retrocompatibilidad de campos
- `hay_migracion_pendiente()` / `obtener_tareas_migracion()` / `marcar_migracion_completada()` — gestión de migración desde v1.0

### `ui/login_window.py`

Ventana raíz (`ctk.CTk`) con dos estados internos:

- **LOGIN**: campos de usuario y contraseña
- **REGISTRO**: campos adicionales de nombre, confirmación de contraseña

Al login exitoso: `self.destroy()` → `MisTareasApp(nombre_usuario).mainloop()`

### `ui/main_window.py`

Clase principal `MisTareasApp(ctk.CTk)`. Recibe `nombre_usuario` en el constructor.
Toda la lógica de tareas, drag & drop, menús y persistencia vive aquí.

---

## Modelo de datos

### `users_data/users.json`

```json
[
  {
    "nombre_usuario": "fabian",
    "nombre_mostrar": "Fabián",
    "hash_password": "$2b$12$...",
    "creado_el": "07/04/2026  14:00",
    "ultimo_login": "07/04/2026  15:30"
  }
]
```

### `users_data/{usuario}/tasks.json`

```json
[
  {
    "text": "Revisar informe",
    "done": false,
    "created_at": "07/04/2026  09:00",
    "done_at": null,
    "priority": true,
    "priority_at": "07/04/2026  09:01"
  }
]
```

---

## Seguridad

### Modelo de amenaza

El sistema está diseñado para el caso de uso de **múltiples usuarios en el mismo ordenador con el mismo perfil de Windows**. No está diseñado para proteger contra:

- Administradores del sistema con acceso al disco
- Acceso físico al equipo

### Contraseñas

- Nunca se almacenan en texto plano
- Se usa **bcrypt** con factor de trabajo `rounds=12`
- El salt se genera automáticamente en cada hash
- En caso de fallo de login, el mensaje de error es genérico ("Usuario o contraseña incorrectos") para no revelar si el usuario existe

### Rutas de archivos

Los nombres de usuario se sanitizan antes de usarlos como nombres de directorio:

```python
re.sub(r'[^\w-]', '_', username.lower())
```

Esto previene ataques de **path traversal** (ej. un usuario llamado `../../etc`).

---

## Compilación y distribución

### Windows (PyInstaller + Inno Setup)

```bash
# Compilar el ejecutable
pyinstaller --onefile --windowed --icon=icon.ico main.py

# El instalador se genera con Inno Setup usando installer_windows.iss
```

### macOS

En construcción.
