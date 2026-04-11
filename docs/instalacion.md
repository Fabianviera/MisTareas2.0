# Instalación

## Descargas

| Archivo | Plataforma | Descripción | Enlace |
|---------|-----------|-------------|--------|
| `Installer_MisTareas2.1.exe` | Windows | Instalador (recomendado) | [Descargar](https://github.com/Fabianviera/MisTareas2.0/releases/latest/download/Installer_MisTareas2.1.exe) |
| `MisTareas2.1.exe` | Windows | Ejecutable portable (sin instalación) | [Descargar](https://github.com/Fabianviera/MisTareas2.0/releases/latest/download/MisTareas2.1.exe) |
| `MisTareas2.1.dmg` | macOS | Imagen de disco | [Descargar](https://github.com/Fabianviera/MisTareas2.0/releases/latest/download/MisTareas2.1.dmg) |

## Windows

### Opción 1 — Instalador (recomendado)

1. Descarga `Installer_MisTareas2.1.exe` desde la tabla anterior o desde la sección [Releases](https://github.com/Fabianviera/MisTareas2.0/releases)
2. Ejecuta el instalador y sigue el asistente
3. Se creará acceso directo en el escritorio y en el menú inicio

!!! warning "Aviso de Windows SmartScreen"
    Al ejecutar el instalador, Windows puede mostrar el mensaje **"Windows protegió su equipo"**.
    Esto ocurre porque el archivo no está firmado digitalmente. Para continuar:

    1. Haz clic en **"Más información"**
    2. Haz clic en **"Ejecutar de todas formas"**

### Opción 2 — Desde el código fuente

Requiere Python 3.10 o superior.

```bash
# 1. Clona el repositorio
git clone https://github.com/Fabianviera/MisTareas2.0.git
cd MisTareas2.0

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Ejecuta la aplicación
python main.py
```

## macOS

### Opción 1 — DMG (recomendado)

1. Descarga `MisTareas2.1.dmg` desde la tabla anterior o desde la sección [Releases](https://github.com/Fabianviera/MisTareas2.0/releases)
2. Abre el archivo `.dmg`
3. Arrastra `MisTareas2.1.app` a tu carpeta **Aplicaciones**
4. Abre la app desde el Launchpad o desde la carpeta Aplicaciones

!!! warning "Aviso de seguridad de macOS (Gatekeeper)"
    Al abrir la app por primera vez, macOS puede mostrar el mensaje **"no se puede abrir porque no se puede verificar el desarrollador"**.
    Esto ocurre porque la app no está firmada con un certificado de Apple. Para continuar:

    1. Ve a **Ajustes del Sistema → Privacidad y seguridad**
    2. En la sección **Seguridad**, haz clic en **"Abrir igualmente"**

### Opción 2 — Desde el código fuente

Requiere Python 3.10 o superior.

```bash
git clone https://github.com/Fabianviera/MisTareas2.0.git
cd MisTareas2.0
pip install -r requirements.txt
python main.py
```

## Dependencias

| Paquete | Versión mínima | Descripción |
|---|---|---|
| `customtkinter` | 5.2.0 | Interfaz gráfica moderna |
| `bcrypt` | 4.0 | Hashing seguro de contraseñas |
| `cryptography` | 42.0 | Cifrado de archivos de tareas (Fernet/PBKDF2) |

## Primer arranque

Al ejecutar la app por primera vez, verás la **pantalla de login**. Como no hay usuarios registrados todavía, haz clic en **"Crear cuenta nueva →"** para registrarte.

Si tienes tareas guardadas de la versión 1.0, la app te ofrecerá importarlas automáticamente al registrar tu primera cuenta.
