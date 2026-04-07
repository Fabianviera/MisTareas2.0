import base64
import hashlib
from cryptography.fernet import Fernet, InvalidToken

# Salt fijo de la aplicación (no se almacena ninguna clave en disco)
_APP_SALT = b"MisTareas2.0_cifrado_v1"


def derivar_clave(nombre_usuario: str, plain_password: str) -> bytes:
    """
    Deriva una clave Fernet de 32 bytes a partir del usuario y contraseña
    usando PBKDF2-HMAC-SHA256. La clave nunca se almacena en disco.
    """
    salt = _APP_SALT + nombre_usuario.lower().encode("utf-8")
    key_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        plain_password.encode("utf-8"),
        salt,
        iterations=100_000,
        dklen=32,
    )
    return base64.urlsafe_b64encode(key_bytes)


def cifrar(texto: str, clave: bytes) -> bytes:
    """Cifra una cadena de texto y devuelve bytes cifrados."""
    return Fernet(clave).encrypt(texto.encode("utf-8"))


def descifrar(datos: bytes, clave: bytes) -> str:
    """
    Descifra bytes y devuelve la cadena original.
    Lanza InvalidToken si la clave es incorrecta o los datos están corruptos.
    """
    return Fernet(clave).decrypt(datos).decode("utf-8")
