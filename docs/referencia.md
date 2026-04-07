# Referencia del código

## config.py

### `_ahora() → str`
Devuelve la fecha y hora actual como cadena con formato `DD/MM/YYYY  HH:MM`.

### `C: dict`
Diccionario con la paleta de colores de la aplicación.

| Clave | Uso |
|---|---|
| `bg` | Fondo principal de la ventana |
| `header` | Fondo de la cabecera |
| `accent` | Color de acento (botones principales, checkboxes) |
| `text` | Color de texto principal |
| `text_muted` | Color de texto secundario/apagado |
| `text_priority` | Color de texto para tareas prioritarias |
| `task_bg` | Fondo de cada fila de tarea |
| `task_hover` | Fondo al pasar el ratón por una tarea |
| `task_priority` | Fondo de tareas prioritarias |
| `task_selected` | Fondo de la tarea seleccionada |

---

## auth/hasher.py

### `hash_password(plain: str) → str`
Genera un hash bcrypt con salt automático (rounds=12).

### `verificar_password(plain: str, hash_guardado: str) → bool`
Verifica una contraseña en texto plano contra un hash bcrypt almacenado.

---

## auth/models.py

### `Usuario` (dataclass)

| Campo | Tipo | Descripción |
|---|---|---|
| `nombre_usuario` | `str` | Identificador único (minúsculas) |
| `nombre_mostrar` | `str` | Nombre visible en la UI |
| `hash_password` | `str` | Hash bcrypt de la contraseña |
| `creado_el` | `str` | Fecha de creación |
| `ultimo_login` | `str` | Fecha del último acceso |

---

## auth/store.py

### `cargar_usuarios() → list[dict]`
Carga todos los usuarios desde `users_data/users.json`. Devuelve lista vacía si no existe.

### `guardar_usuarios(usuarios: list[dict]) → None`
Guarda la lista de usuarios con escritura atómica.

### `buscar_usuario(nombre_usuario: str) → dict | None`
Busca un usuario por nombre (insensible a mayúsculas). Devuelve `None` si no existe.

### `crear_usuario(nombre_usuario, nombre_mostrar, plain_password) → bool`
Crea un nuevo usuario con la contraseña hasheada. Devuelve `False` si el usuario ya existe.

### `actualizar_ultimo_login(nombre_usuario: str) → None`
Actualiza la marca de tiempo del último login.

### `existe_algún_usuario() → bool`
Comprueba si hay al menos un usuario registrado.

### `autenticar(nombre_usuario: str, plain_password: str) → dict | None`
Autentica al usuario. Devuelve el dict del usuario si las credenciales son correctas, `None` en caso contrario.

---

## data/task_store.py

### `obtener_archivo_tareas(nombre_usuario: str) → str`
Devuelve la ruta completa al archivo de tareas del usuario, creando el directorio si no existe.

### `guardar_tareas(tareas: list, nombre_usuario: str) → None`
Guarda la lista de tareas con escritura atómica mediante archivo `.tmp` + `os.replace()`.

### `cargar_tareas(nombre_usuario: str) → list`
Carga las tareas del usuario. Si no existen pero hay un `tasks.json` legado, lo copia a `users_data/pendiente_migracion.json` para ofrecerlo durante el registro.

### `hay_migracion_pendiente() → bool`
Comprueba si existe `users_data/pendiente_migracion.json`.

### `obtener_tareas_migracion() → list`
Devuelve las tareas legadas pendientes de migración.

### `marcar_migracion_completada() → None`
Elimina el archivo `pendiente_migracion.json`.

---

## ui/login_window.py

### `VentanaLogin(ctk.CTk)`

Ventana raíz de la aplicación. Gestiona dos estados internos: `"login"` y `"registro"`.

| Método | Descripción |
|---|---|
| `_construir_ui()` | Construye todos los widgets (se llama una sola vez) |
| `_mostrar_estado_login()` | Muestra el formulario de acceso |
| `_mostrar_estado_registro()` | Muestra el formulario de creación de cuenta |
| `_cambiar_estado()` | Alterna entre login y registro |
| `_intentar_login()` | Valida y ejecuta el login |
| `_intentar_registro()` | Valida y ejecuta el registro |
| `_alternar_visibilidad(entrada)` | Muestra/oculta la contraseña en un campo |
| `_lanzar_app(nombre_usuario)` | Destruye el login y lanza `MisTareasApp` |

---

## ui/main_window.py

### `MisTareasApp(ctk.CTk)`

Ventana principal. Recibe `nombre_usuario: str` en el constructor.

| Método | Descripción |
|---|---|
| `_construir_ui()` | Construye cabecera, entrada y lista |
| `_construir_barra_menus()` | Barra de menús (diferenciada por plataforma) |
| `_añadir_tarea()` | Añade una nueva tarea (máx. 200 caracteres) |
| `_alternar_tarea(indice, var)` | Marca/desmarca una tarea como completada |
| `_eliminar_tarea(indice)` | Elimina una tarea |
| `_alternar_prioridad(indice)` | Activa/desactiva la prioridad de una tarea |
| `_seleccionar_tarea(indice)` | Selecciona una tarea (actualiza colores en sitio) |
| `_mover_seleccionada(direccion)` | Mueve la tarea seleccionada con teclado |
| `_iniciar_arrastre(event, indice)` | Inicia el drag & drop |
| `_bucle_anim_fantasma()` | Bucle a ~60fps para el ghost window durante el arrastre |
| `_iniciar_anim_hueco(nuevo_idx)` | Animación de apertura de hueco al arrastrar |
| `_fin_arrastre(event)` | Finaliza el arrastre y reordena |
| `_renderizar_tareas()` | Reconstruye todos los widgets de la lista |
| `_guardar_tareas()` | Persiste las tareas (escritura atómica) |
| `_cargar_tareas()` | Carga las tareas del usuario actual |
| `_cerrar_sesion()` | Destruye la app y relanza `VentanaLogin` |
| `_salir()` | Guarda y cierra la aplicación |
