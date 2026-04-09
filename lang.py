import json
import os
from config import DIR_BASE

_SETTINGS_FILE = os.path.join(DIR_BASE, "users_data", "settings.json")

_TRANSLATIONS = {
    "es": {
        # Login window
        "login_title_window":    "MisTareas — Acceder",
        "login_title":           "Iniciar sesión",
        "register_title":        "Crear cuenta",
        "lbl_display_name":      "Nombre para mostrar",
        "lbl_username_reg":      "Usuario (letras, números, - y _)",
        "lbl_password_reg":      "Contraseña (mínimo 6 caracteres)",
        "lbl_confirm_password":  "Confirmar contraseña",
        "lbl_username_login":    "Usuario",
        "lbl_password_login":    "Contraseña",
        "ph_display_name":       "Ej: Fabián",
        "ph_username_reg":       "Ej: fabian_viera",
        "ph_password":           "Contraseña",
        "ph_confirm":            "Repetir contraseña",
        "ph_username_login":     "Nombre de usuario",
        "btn_login":             "Entrar",
        "btn_register":          "Registrarse",
        "btn_new_account":       "Crear cuenta nueva →",
        "btn_have_account":      "← Ya tengo cuenta",
        "err_fill_all":          "Por favor, rellena todos los campos.",
        "err_wrong_credentials": "Usuario o contraseña incorrectos.",
        "err_display_name":      "El nombre para mostrar no puede estar vacío.",
        "err_username_empty":    "El nombre de usuario no puede estar vacío.",
        "err_username_invalid":  "El usuario solo puede contener letras, números, - y _",
        "err_user_exists":       "El usuario «{}» ya existe.",
        "tip_password_short":    "La contraseña debe tener\nal menos 6 caracteres.",
        "tip_password_mismatch": "Las contraseñas no coinciden,\nvuelve a intentarlo.",
        "migration_title":       "MisTareas — Importar datos",
        "migration_msg":         "Se han encontrado tareas guardadas de una versión anterior.\n\n¿Deseas importarlas a tu nueva cuenta?",
        # Main window
        "app_title":             "MisTareas",
        "ph_add_task":           "Añadir nueva tarea…",
        "empty_state":           "Sin tareas por el momento.\n¡Añade una arriba!",
        "ts_created":            "🕐 Creada: {}",
        "ts_done":               "   ✅ Hecha: {}",
        "menu_file":             "Archivo",
        "menu_logout":           "Cerrar sesión",
        "menu_quit":             "Salir",
        "menu_tasks":            "Tareas",
        "menu_clear_done":       "Borrar completadas",
        "menu_clear_all":        "Borrar todas",
        "menu_help":             "Ayuda",
        "menu_help_item":        "Ayuda de MisTareas",
        "menu_about":            "Acerca de MisTareas",
        "menu_license":          "Licencia",
        "menu_language":         "Idioma / Language",
        "ctx_clear_done":        "🗑   Borrar completadas",
        "ctx_clear_all":         "🗑   Borrar todas",
        "about_title":           "Acerca de MisTareas",
        "about_created":         "Creado por Juan Fabián Viera Rosales · 2026",
        "about_version":         "Versión 2.0  ·  Para uso no comercial",
        "btn_close":             "Cerrar",
        "license_title":         "Licencia",
        "license_header":        "Licencia — GNU General Public License v3",
        "help_title":            "Ayuda — MisTareas",
        "help_header":           "✓  MisTareas  —  Guía rápida",
        "help_footer":           "Fabián Viera · 2026 · Versión 2.0",
        "help_s1_title":         "Crear una tarea",
        "help_s1_1":             "Escribe el texto en el campo superior.",
        "help_s1_2":             "Pulsa [+] o la tecla Enter para añadirla.",
        "help_s2_title":         "Completar y descompletar",
        "help_s2_1":             "Haz clic en el checkbox (☐) para marcarla como hecha.",
        "help_s2_2":             "Vuelve a hacer clic para desmarcarla.",
        "help_s2_3":             "Se registra la fecha y hora de creación y de finalización.",
        "help_s3_title":         "Tareas prioritarias",
        "help_s3_1":             "Pulsa la estrella (☆) para marcarla como prioritaria.",
        "help_s3_2":             "Las tareas prioritarias suben al inicio de la lista.",
        "help_s3_3":             "Pulsa [★] de nuevo para quitar la prioridad.",
        "help_s3_4":             "Al completar una tarea prioritaria, pierde la prioridad.",
        "help_s4_title":         "Ordenar tareas",
        "help_s4_1":             "Arrastra el icono [≡] para reordenar con el ratón.",
        "help_s4_2":             "Selecciona una tarea y usa ↑ ↓ para moverla con el teclado.",
        "help_s4_3":             "Solo puedes mover tareas dentro de su sección.",
        "help_s5_title":         "Eliminar tareas",
        "help_s5_1":             "Pulsa [✕] en la fila para eliminar esa tarea.",
        "help_s5_2":             "Menú [⋮] → «Borrar completadas» para limpiar las tareas hechas.",
        "help_s5_3":             "«Borrar todas» elimina toda la lista sin posibilidad de recuperación.",
        "help_s6_title":         "Fijar la ventana",
        "help_s6_1":             "El botón [📌] mantiene la ventana siempre encima de las demás apps.",
        "help_s6_2":             "Al activarse cambia a [📍] con fondo azul. Pulsa de nuevo para desactivarlo.",
        "help_s7_title":         "Cuentas de usuario",
        "help_s7_1":             "Menú Archivo → «Cerrar sesión» para cambiar de cuenta.",
        "help_s7_2":             "Cada usuario tiene sus propias tareas guardadas de forma segura.",
        "warn_task_long":        "El texto no puede superar los 200 caracteres.",
        "info_no_done":          "No hay tareas completadas.",
        "info_no_tasks":         "No hay tareas.",
        "confirm_title":         "Confirmar",
        "confirm_clear_done":    "¿Borrar {} tarea(s) completada(s)?",
        "confirm_clear_all":     "¿Borrar las {} tarea(s)?",
        "footer_user":           "👤  Usuario activo: {}",
        "err_save_tasks":        "Error al guardar las tareas:\n{}",
        "err_load_tasks":        "No se pudo leer el archivo de tareas.\nSe empezará con la lista vacía.\n\nDetalle: {}",
        "switch_title":          "Cambiar a {}",
        "switch_password_lbl":   "Contraseña de «{}»",
        "err_wrong_password":    "Contraseña incorrecta.",
        "lang_restart_msg":      "El idioma se aplicará al reiniciar la aplicación.",
        "lang_restart_title":    "Idioma cambiado",
    },
    "en": {
        # Login window
        "login_title_window":    "MisTareas — Sign In",
        "login_title":           "Sign In",
        "register_title":        "Create Account",
        "lbl_display_name":      "Display name",
        "lbl_username_reg":      "Username (letters, numbers, - and _)",
        "lbl_password_reg":      "Password (minimum 6 characters)",
        "lbl_confirm_password":  "Confirm password",
        "lbl_username_login":    "Username",
        "lbl_password_login":    "Password",
        "ph_display_name":       "E.g.: John",
        "ph_username_reg":       "E.g.: john_doe",
        "ph_password":           "Password",
        "ph_confirm":            "Repeat password",
        "ph_username_login":     "Username",
        "btn_login":             "Sign In",
        "btn_register":          "Sign Up",
        "btn_new_account":       "Create new account →",
        "btn_have_account":      "← I already have an account",
        "err_fill_all":          "Please fill in all fields.",
        "err_wrong_credentials": "Incorrect username or password.",
        "err_display_name":      "Display name cannot be empty.",
        "err_username_empty":    "Username cannot be empty.",
        "err_username_invalid":  "Username can only contain letters, numbers, - and _",
        "err_user_exists":       "The user «{}» already exists.",
        "tip_password_short":    "Password must be\nat least 6 characters.",
        "tip_password_mismatch": "Passwords do not match,\nplease try again.",
        "migration_title":       "MisTareas — Import data",
        "migration_msg":         "Tasks from a previous version were found.\n\nDo you want to import them to your new account?",
        # Main window
        "app_title":             "MisTareas",
        "ph_add_task":           "Add new task…",
        "empty_state":           "No tasks yet.\nAdd one above!",
        "ts_created":            "🕐 Created: {}",
        "ts_done":               "   ✅ Done: {}",
        "menu_file":             "File",
        "menu_logout":           "Log out",
        "menu_quit":             "Quit",
        "menu_tasks":            "Tasks",
        "menu_clear_done":       "Clear completed",
        "menu_clear_all":        "Clear all",
        "menu_help":             "Help",
        "menu_help_item":        "MisTareas Help",
        "menu_about":            "About MisTareas",
        "menu_license":          "License",
        "menu_language":         "Idioma / Language",
        "ctx_clear_done":        "🗑   Clear completed",
        "ctx_clear_all":         "🗑   Clear all",
        "about_title":           "About MisTareas",
        "about_created":         "Created by Juan Fabián Viera Rosales · 2026",
        "about_version":         "Version 2.0  ·  For non-commercial use",
        "btn_close":             "Close",
        "license_title":         "License",
        "license_header":        "License — GNU General Public License v3",
        "help_title":            "Help — MisTareas",
        "help_header":           "✓  MisTareas  —  Quick Guide",
        "help_footer":           "Fabián Viera · 2026 · Version 2.0",
        "help_s1_title":         "Create a task",
        "help_s1_1":             "Type the text in the field above.",
        "help_s1_2":             "Press [+] or Enter to add it.",
        "help_s2_title":         "Complete and uncomplete",
        "help_s2_1":             "Click the checkbox (☐) to mark it as done.",
        "help_s2_2":             "Click again to unmark it.",
        "help_s2_3":             "Creation and completion date/time are recorded.",
        "help_s3_title":         "Priority tasks",
        "help_s3_1":             "Click the star (☆) to mark it as priority.",
        "help_s3_2":             "Priority tasks move to the top of the list.",
        "help_s3_3":             "Click [★] again to remove priority.",
        "help_s3_4":             "Completing a priority task removes its priority.",
        "help_s4_title":         "Sort tasks",
        "help_s4_1":             "Drag the [≡] icon to reorder with the mouse.",
        "help_s4_2":             "Select a task and use ↑ ↓ to move it with the keyboard.",
        "help_s4_3":             "You can only move tasks within their section.",
        "help_s5_title":         "Delete tasks",
        "help_s5_1":             "Click [✕] in the row to delete that task.",
        "help_s5_2":             "Menu [⋮] → «Clear completed» to remove done tasks.",
        "help_s5_3":             "«Clear all» deletes the entire list with no recovery.",
        "help_s6_title":         "Pin the window",
        "help_s6_1":             "The [📌] button keeps the window always on top of other apps.",
        "help_s6_2":             "When active it changes to [📍] with blue background. Click again to deactivate.",
        "help_s7_title":         "User accounts",
        "help_s7_1":             "File menu → «Log out» to switch accounts.",
        "help_s7_2":             "Each user has their own tasks saved securely.",
        "warn_task_long":        "Text cannot exceed 200 characters.",
        "info_no_done":          "No completed tasks.",
        "info_no_tasks":         "No tasks.",
        "confirm_title":         "Confirm",
        "confirm_clear_done":    "Delete {} completed task(s)?",
        "confirm_clear_all":     "Delete all {} task(s)?",
        "footer_user":           "👤  Active user: {}",
        "err_save_tasks":        "Error saving tasks:\n{}",
        "err_load_tasks":        "Could not read the tasks file.\nStarting with an empty list.\n\nDetails: {}",
        "switch_title":          "Switch to {}",
        "switch_password_lbl":   "Password for «{}»",
        "err_wrong_password":    "Incorrect password.",
        "lang_restart_msg":      "The language will be applied on restart.",
        "lang_restart_title":    "Language changed",
    }
}


def get_lang() -> str:
    try:
        with open(_SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("lang", "es")
    except Exception:
        return "es"


def set_lang(lang: str) -> None:
    os.makedirs(os.path.dirname(_SETTINGS_FILE), exist_ok=True)
    try:
        try:
            with open(_SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
        data["lang"] = lang
        with open(_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
    except Exception:
        pass
    _reload()


def _reload():
    lang = get_lang()
    T.clear()
    T.update(_TRANSLATIONS.get(lang, _TRANSLATIONS["es"]))


# Diccionario activo de traducciones — se actualiza en memoria al cambiar idioma
T: dict = {}
_reload()
