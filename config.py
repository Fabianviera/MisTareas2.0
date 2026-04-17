import os
import sys
from datetime import datetime
import customtkinter as ctk

# ── Función de fecha/hora ─────────────────────────────────────────────────────

def _ahora() -> str:
    return datetime.now().strftime("%d/%m/%Y  %H:%M")

# ── Apariencia ────────────────────────────────────────────────────────────────

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# ── Paleta de colores ─────────────────────────────────────────────────────────

C = {
    "bg":            "#EBF2F8",
    "header":        "#C8DAF0",
    "header_border": "#B0C8E8",
    "task_bg":       "#F4F8FC",
    "task_hover":    "#D9EAF7",
    "task_priority": "#FFF5F5",
    "task_selected": "#D0E8F5",
    "accent":        "#5B9BD5",
    "accent_hover":  "#4A87BF",
    "text":          "#2C3E50",
    "text_muted":    "#8FA8C0",
    "text_priority": "#C0392B",
    "drag_handle":   "#A0B8D0",
    "drag_source":   "#D0D8E0",
    "drag_target":   "#A8CCE8",
    "input_bg":      "#FFFFFF",
    "border":        "#C5D5E8",
    "del_hover":     "#FDDEDE",
    "scroll":        "#C5D5E8",
}

# ── Rutas base ────────────────────────────────────────────────────────────────

if getattr(sys, 'frozen', False):
    DIR_BASE = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "MisTareas")
    os.makedirs(DIR_BASE, exist_ok=True)
else:
    DIR_BASE = os.path.dirname(os.path.abspath(__file__))

# ARCHIVO_TAREAS solo se mantiene como referencia para migración legacy
ARCHIVO_TAREAS = os.path.join(DIR_BASE, "tasks.json")
