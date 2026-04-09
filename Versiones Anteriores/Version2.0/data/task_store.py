import os
import re
import json
from config import DIR_BASE
from auth.crypto import cifrar, descifrar
from cryptography.fernet import InvalidToken


def _sanitizar_usuario(nombre_usuario: str) -> str:
    """Convierte el nombre de usuario a un nombre de directorio seguro."""
    return re.sub(r'[^\w-]', '_', nombre_usuario.lower())


def obtener_archivo_tareas(nombre_usuario: str) -> str:
    """Devuelve la ruta completa al archivo de tareas del usuario."""
    nombre_sanitizado = _sanitizar_usuario(nombre_usuario)
    directorio_usuario = os.path.join(DIR_BASE, "users_data", nombre_sanitizado)
    os.makedirs(directorio_usuario, exist_ok=True)
    return os.path.join(directorio_usuario, "tasks.json")


def guardar_tareas(tareas: list, nombre_usuario: str, clave: bytes = None) -> None:
    """Guarda la lista de tareas del usuario con escritura atómica mediante .tmp.
    Si se proporciona una clave, el archivo se cifra con Fernet."""
    archivo = obtener_archivo_tareas(nombre_usuario)
    temporal = archivo + ".tmp"
    try:
        contenido_json = json.dumps(tareas, ensure_ascii=False, indent=2)
        if clave:
            datos = cifrar(contenido_json, clave)
            with open(temporal, "wb") as f:
                f.write(datos)
        else:
            with open(temporal, "w", encoding="utf-8") as f:
                f.write(contenido_json)
        os.replace(temporal, archivo)
    except Exception:
        try:
            os.remove(temporal)
        except Exception:
            pass
        raise


def cargar_tareas(nombre_usuario: str, clave: bytes = None) -> list:
    """
    Carga las tareas del usuario.
    Si el archivo de usuario no existe pero sí existe un tasks.json legado en la raíz,
    guarda ese legado en users_data/pendiente_migracion.json para que el store de auth
    lo pueda detectar y ofrecer migración al primer usuario registrado.
    """
    archivo = obtener_archivo_tareas(nombre_usuario)

    # Verificar si hay datos legacy pendientes de migración
    archivo_legacy = os.path.join(DIR_BASE, "tasks.json")
    archivo_pendiente = os.path.join(DIR_BASE, "users_data", "pendiente_migracion.json")

    if (not os.path.exists(archivo)
            and os.path.exists(archivo_legacy)
            and not os.path.exists(archivo_pendiente)):
        # Guardar el legado para ofrecerlo durante el registro
        try:
            with open(archivo_legacy, "r", encoding="utf-8") as f:
                tareas_legacy = json.load(f)
            os.makedirs(os.path.join(DIR_BASE, "users_data"), exist_ok=True)
            with open(archivo_pendiente, "w", encoding="utf-8") as f:
                json.dump(tareas_legacy, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    if os.path.exists(archivo):
        try:
            if clave:
                with open(archivo, "rb") as f:
                    datos = f.read()
                try:
                    contenido = descifrar(datos, clave)
                except (InvalidToken, Exception):
                    # Compatibilidad: archivo antiguo en texto plano → migrar a cifrado
                    contenido = datos.decode("utf-8")
                tareas = json.loads(contenido)
            else:
                with open(archivo, "r", encoding="utf-8") as f:
                    tareas = json.load(f)
            for t in tareas:
                t.setdefault("priority",    False)
                t.setdefault("priority_at", None)
            # Si había datos en plano y ahora tenemos clave, re-guardar cifrado
            if clave:
                guardar_tareas(tareas, nombre_usuario, clave)
            return tareas
        except Exception:
            return []
    return []


def hay_migracion_pendiente() -> bool:
    """Comprueba si hay un archivo de tareas legado pendiente de migrar."""
    archivo_pendiente = os.path.join(DIR_BASE, "users_data", "pendiente_migracion.json")
    return os.path.exists(archivo_pendiente)


def obtener_tareas_migracion() -> list:
    """Devuelve las tareas legadas pendientes de migración."""
    archivo_pendiente = os.path.join(DIR_BASE, "users_data", "pendiente_migracion.json")
    if os.path.exists(archivo_pendiente):
        try:
            with open(archivo_pendiente, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def marcar_migracion_completada() -> None:
    """Elimina el archivo de migración pendiente."""
    archivo_pendiente = os.path.join(DIR_BASE, "users_data", "pendiente_migracion.json")
    try:
        os.remove(archivo_pendiente)
    except Exception:
        pass
