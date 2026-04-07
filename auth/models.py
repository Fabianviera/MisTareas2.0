from dataclasses import dataclass, field


@dataclass
class Usuario:
    nombre_usuario: str
    nombre_mostrar: str
    hash_password: str
    creado_el: str
    ultimo_login: str = ""
