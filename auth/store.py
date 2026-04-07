import os
import json
from config import DIR_BASE, _ahora
from auth.hasher import hash_password, verificar_password

_ARCHIVO_USUARIOS = os.path.join(DIR_BASE, "users_data", "users.json")


def _asegurar_directorio() -> None:
    """Crea el directorio users_data si no existe."""
    os.makedirs(os.path.join(DIR_BASE, "users_data"), exist_ok=True)


def cargar_usuarios() -> list[dict]:
    """Carga la lista de usuarios desde users.json. Devuelve lista vacía si no existe."""
    _asegurar_directorio()
    if not os.path.exists(_ARCHIVO_USUARIOS):
        return []
    try:
        with open(_ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def guardar_usuarios(usuarios: list[dict]) -> None:
    """Guarda la lista de usuarios con escritura atómica."""
    _asegurar_directorio()
    temporal = _ARCHIVO_USUARIOS + ".tmp"
    try:
        with open(temporal, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=2)
        os.replace(temporal, _ARCHIVO_USUARIOS)
    except Exception:
        try:
            os.remove(temporal)
        except Exception:
            pass
        raise


def buscar_usuario(nombre_usuario: str) -> dict | None:
    """Busca un usuario por nombre (insensible a mayúsculas). Devuelve None si no existe."""
    usuarios = cargar_usuarios()
    nombre_lower = nombre_usuario.lower()
    for u in usuarios:
        if u.get("nombre_usuario", "").lower() == nombre_lower:
            return u
    return None


def crear_usuario(nombre_usuario: str, nombre_mostrar: str, plain_password: str) -> bool:
    """
    Crea un nuevo usuario con contraseña hasheada.
    Devuelve False si el nombre de usuario ya está en uso.
    """
    if buscar_usuario(nombre_usuario) is not None:
        return False

    usuarios = cargar_usuarios()
    nuevo = {
        "nombre_usuario": nombre_usuario.lower(),
        "nombre_mostrar": nombre_mostrar,
        "hash_password":  hash_password(plain_password),
        "creado_el":      _ahora(),
        "ultimo_login":   "",
    }
    usuarios.append(nuevo)
    guardar_usuarios(usuarios)
    return True


def actualizar_ultimo_login(nombre_usuario: str) -> None:
    """Actualiza la marca de tiempo del último login del usuario."""
    usuarios = cargar_usuarios()
    nombre_lower = nombre_usuario.lower()
    for u in usuarios:
        if u.get("nombre_usuario", "").lower() == nombre_lower:
            u["ultimo_login"] = _ahora()
            break
    guardar_usuarios(usuarios)


def existe_algún_usuario() -> bool:
    """Comprueba si hay al menos un usuario registrado."""
    return len(cargar_usuarios()) > 0


def autenticar(nombre_usuario: str, plain_password: str) -> dict | None:
    """
    Intenta autenticar al usuario. Devuelve el dict del usuario si las
    credenciales son correctas, None en caso contrario.
    """
    usuario = buscar_usuario(nombre_usuario)
    if usuario is None:
        return None
    if verificar_password(plain_password, usuario.get("hash_password", "")):
        actualizar_ultimo_login(nombre_usuario)
        return usuario
    return None
