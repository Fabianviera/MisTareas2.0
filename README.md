# MisTareas 2.1

Aplicación de escritorio multi-usuario para gestionar listas de tareas, desarrollada en Python con CustomTkinter.

📖 **[Documentación completa](https://fabianviera.github.io/MisTareas2.0)**

---

## Características

- Multi-usuario con autenticación segura (bcrypt)
- Cada usuario tiene su lista de tareas independiente
- Crear, completar, eliminar y priorizar tareas
- Drag & drop con animaciones para reordenar
- Timestamps automáticos de creación y finalización
- Ventana siempre visible (pin)
- Interfaz disponible en español e inglés
- Compatible con Windows y macOS
- Migración automática desde MisTareas 1.0

## Instalación

### Windows
Descarga el instalador desde [Releases](https://github.com/Fabianviera/MisTareas2.0/releases).

> **Aviso SmartScreen**: si Windows muestra "Windows protegió su equipo", haz clic en **"Más información"** → **"Ejecutar de todas formas"**.

### Desde el código fuente

```bash
git clone https://github.com/Fabianviera/MisTareas2.0.git
cd MisTareas2.0
pip install -r requirements.txt
python main.py
```

## Tecnologías

- Python 3.12
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [bcrypt](https://pypi.org/project/bcrypt/)
- PyInstaller
- Inno Setup

## Autor

Juan Fabián Viera Rosales — 2026 · Versión 2.1
