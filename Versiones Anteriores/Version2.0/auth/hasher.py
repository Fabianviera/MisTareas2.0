import bcrypt


def hash_password(plain: str) -> str:
    """Genera un hash bcrypt de la contraseña en texto plano."""
    return bcrypt.hashpw(plain.encode('utf-8'), bcrypt.gensalt(rounds=12)).decode('utf-8')


def verificar_password(plain: str, hash_guardado: str) -> bool:
    """Verifica una contraseña en texto plano contra un hash bcrypt almacenado."""
    return bcrypt.checkpw(plain.encode('utf-8'), hash_guardado.encode('utf-8'))
