import re
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from config import C
import auth.store as auth_store
import data.task_store as task_store


class VentanaLogin(ctk.CTk):
    """
    Ventana de autenticación con dos estados:
    - LOGIN: formulario de acceso con usuario y contraseña.
    - REGISTRO: formulario de creación de cuenta nueva.
    """

    _REGEX_USUARIO = re.compile(r'^[a-zA-Z0-9_-]+$')

    def __init__(self):
        super().__init__()

        self.title("MisTareas — Acceder")
        self.geometry("400x520")
        self.resizable(False, False)
        self.configure(fg_color=C["bg"])

        # Centrar la ventana en pantalla
        self.update_idletasks()
        ancho_pantalla  = self.winfo_screenwidth()
        alto_pantalla   = self.winfo_screenheight()
        x = (ancho_pantalla  - 400) // 2
        y = (alto_pantalla   - 520) // 2
        self.geometry(f"400x520+{x}+{y}")

        self._estado = "login"   # "login" | "registro"
        self._construir_ui()

    # ── Construcción de la UI ─────────────────────────────────────────────────

    def _construir_ui(self):
        """Construye todos los widgets. Se llama una sola vez."""

        # ── Cabecera ──
        cabecera = ctk.CTkFrame(self, fg_color=C["header"], corner_radius=0, height=72)
        cabecera.pack(fill="x")
        cabecera.pack_propagate(False)
        ctk.CTkLabel(
            cabecera, text="✓  MisTareas",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=C["text"]
        ).pack(expand=True)

        # ── Contenedor central ──
        self._contenedor = ctk.CTkFrame(self, fg_color="transparent")
        self._contenedor.pack(fill="both", expand=True, padx=36, pady=20)

        # Título del formulario
        self._lbl_titulo = ctk.CTkLabel(
            self._contenedor, text="Iniciar sesión",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=C["text"]
        )
        self._lbl_titulo.pack(pady=(0, 18))

        # ── Campos de REGISTRO ──
        self._frame_registro = ctk.CTkFrame(self._contenedor, fg_color="transparent")

        ctk.CTkLabel(
            self._frame_registro, text="Nombre para mostrar",
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        self._ent_nombre_mostrar = ctk.CTkEntry(
            self._frame_registro,
            placeholder_text="Ej: Fabián",
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_nombre_mostrar.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            self._frame_registro, text="Usuario (letras, números, - y _)",
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        self._ent_usuario_reg = ctk.CTkEntry(
            self._frame_registro,
            placeholder_text="Ej: fabian_viera",
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_usuario_reg.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            self._frame_registro, text="Contraseña (mínimo 6 caracteres)",
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        fila_pass_reg = ctk.CTkFrame(self._frame_registro, fg_color="transparent")
        fila_pass_reg.pack(fill="x", pady=(0, 10))
        self._ent_pass_reg = ctk.CTkEntry(
            fila_pass_reg, show="•",
            placeholder_text="Contraseña",
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_pass_reg.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._btn_ver_pass_reg = ctk.CTkButton(
            fila_pass_reg, text="👁", width=40, height=40, corner_radius=10,
            fg_color=C["task_bg"], hover_color=C["task_hover"],
            text_color=C["text_muted"], font=ctk.CTkFont(size=14),
            command=lambda: self._alternar_visibilidad(self._ent_pass_reg)
        )
        self._btn_ver_pass_reg.pack(side="right")

        ctk.CTkLabel(
            self._frame_registro, text="Confirmar contraseña",
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        fila_pass_conf = ctk.CTkFrame(self._frame_registro, fg_color="transparent")
        fila_pass_conf.pack(fill="x", pady=(0, 10))
        self._ent_pass_conf = ctk.CTkEntry(
            fila_pass_conf, show="•",
            placeholder_text="Repetir contraseña",
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_pass_conf.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._btn_ver_pass_conf = ctk.CTkButton(
            fila_pass_conf, text="👁", width=40, height=40, corner_radius=10,
            fg_color=C["task_bg"], hover_color=C["task_hover"],
            text_color=C["text_muted"], font=ctk.CTkFont(size=14),
            command=lambda: self._alternar_visibilidad(self._ent_pass_conf)
        )
        self._btn_ver_pass_conf.pack(side="right")

        # ── Campos de LOGIN ──
        self._frame_login = ctk.CTkFrame(self._contenedor, fg_color="transparent")

        ctk.CTkLabel(
            self._frame_login, text="Usuario",
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        self._ent_usuario_login = ctk.CTkEntry(
            self._frame_login,
            placeholder_text="Nombre de usuario",
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_usuario_login.pack(fill="x", pady=(0, 14))

        ctk.CTkLabel(
            self._frame_login, text="Contraseña",
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        fila_pass_login = ctk.CTkFrame(self._frame_login, fg_color="transparent")
        fila_pass_login.pack(fill="x", pady=(0, 14))
        self._ent_pass_login = ctk.CTkEntry(
            fila_pass_login, show="•",
            placeholder_text="Contraseña",
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_pass_login.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self._btn_ver_pass_login = ctk.CTkButton(
            fila_pass_login, text="👁", width=40, height=40, corner_radius=10,
            fg_color=C["task_bg"], hover_color=C["task_hover"],
            text_color=C["text_muted"], font=ctk.CTkFont(size=14),
            command=lambda: self._alternar_visibilidad(self._ent_pass_login)
        )
        self._btn_ver_pass_login.pack(side="right")
        self._ent_pass_login.bind("<Return>", lambda _: self._intentar_login())

        # ── Botón de acción principal ──
        self._btn_accion = ctk.CTkButton(
            self._contenedor, text="Entrar",
            height=44, corner_radius=12,
            fg_color=C["accent"], hover_color=C["accent_hover"],
            text_color="white", font=ctk.CTkFont(size=15, weight="bold"),
            command=self._accion_principal
        )
        self._btn_accion.pack(fill="x", pady=(4, 0))

        # ── Mensaje de error / información ──
        self._lbl_error = ctk.CTkLabel(
            self._contenedor, text="",
            font=ctk.CTkFont(size=12),
            text_color=C["text_priority"]
        )
        self._lbl_error.pack(pady=(6, 0))

        # ── Enlace para cambiar de estado ──
        self._btn_cambiar_estado = ctk.CTkButton(
            self._contenedor, text="Crear cuenta nueva →",
            fg_color="transparent", hover_color=C["task_hover"],
            text_color=C["accent"], font=ctk.CTkFont(size=13, underline=True),
            height=32, corner_radius=8,
            command=self._cambiar_estado
        )
        self._btn_cambiar_estado.pack(pady=(4, 0))

        # Mostrar el formulario inicial
        self._mostrar_estado_login()

    # ── Cambio de estado ──────────────────────────────────────────────────────

    def _mostrar_estado_login(self):
        self._frame_registro.pack_forget()
        self._frame_login.pack(fill="x", before=self._btn_accion)
        self._lbl_titulo.configure(text="Iniciar sesión")
        self._btn_accion.configure(text="Entrar", command=self._intentar_login)
        self._btn_cambiar_estado.configure(text="Crear cuenta nueva →")
        self._lbl_error.configure(text="")
        self._ent_usuario_login.focus_set()

    def _mostrar_estado_registro(self):
        self._frame_login.pack_forget()
        self._frame_registro.pack(fill="x", before=self._btn_accion)
        self._lbl_titulo.configure(text="Crear cuenta")
        self._btn_accion.configure(text="Registrarse", command=self._intentar_registro)
        self._btn_cambiar_estado.configure(text="← Ya tengo cuenta")
        self._lbl_error.configure(text="")
        self._ent_nombre_mostrar.focus_set()

    def _cambiar_estado(self):
        if self._estado == "login":
            self._estado = "registro"
            self._mostrar_estado_registro()
        else:
            self._estado = "login"
            self._mostrar_estado_login()

    def _accion_principal(self):
        if self._estado == "login":
            self._intentar_login()
        else:
            self._intentar_registro()

    # ── Autenticación ─────────────────────────────────────────────────────────

    def _intentar_login(self):
        usuario    = self._ent_usuario_login.get().strip()
        contrasena = self._ent_pass_login.get()

        if not usuario or not contrasena:
            self._mostrar_error("Por favor, rellena todos los campos.")
            return

        resultado = auth_store.autenticar(usuario, contrasena)
        if resultado is None:
            self._mostrar_error("Usuario o contraseña incorrectos.")
            return

        nombre_usuario = resultado["nombre_usuario"]
        self._lanzar_app(nombre_usuario)

    # ── Registro ──────────────────────────────────────────────────────────────

    def _intentar_registro(self):
        nombre_mostrar  = self._ent_nombre_mostrar.get().strip()
        nombre_usuario  = self._ent_usuario_reg.get().strip()
        contrasena      = self._ent_pass_reg.get()
        contrasena_conf = self._ent_pass_conf.get()

        # Validaciones
        if not nombre_mostrar:
            self._mostrar_error("El nombre para mostrar no puede estar vacío.")
            return

        if not nombre_usuario:
            self._mostrar_error("El nombre de usuario no puede estar vacío.")
            return

        if not self._REGEX_USUARIO.match(nombre_usuario):
            self._mostrar_error("El usuario solo puede contener letras, números, - y _")
            return

        if len(contrasena) < 6:
            self._mostrar_error("La contraseña debe tener al menos 6 caracteres.")
            return

        if contrasena != contrasena_conf:
            self._mostrar_error("Las contraseñas no coinciden.")
            return

        creado = auth_store.crear_usuario(nombre_usuario, nombre_mostrar, contrasena)
        if not creado:
            self._mostrar_error(f"El usuario «{nombre_usuario}» ya existe.")
            return

        nombre_usuario_lower = nombre_usuario.lower()

        # Ofrecer migración de tareas legadas si las hay
        if task_store.hay_migracion_pendiente():
            respuesta = messagebox.askyesno(
                "MisTareas — Importar datos",
                "Se han encontrado tareas guardadas de una versión anterior.\n\n"
                "¿Deseas importarlas a tu nueva cuenta?"
            )
            if respuesta:
                tareas_legacy = task_store.obtener_tareas_migracion()
                task_store.guardar_tareas(tareas_legacy, nombre_usuario_lower)
            task_store.marcar_migracion_completada()

        self._lanzar_app(nombre_usuario_lower)

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _mostrar_error(self, mensaje: str):
        self._lbl_error.configure(text=mensaje)

    def _alternar_visibilidad(self, entrada: ctk.CTkEntry):
        """Alterna la visibilidad de la contraseña en un campo de entrada."""
        actual = entrada.cget("show")
        entrada.configure(show="" if actual else "•")

    def _lanzar_app(self, nombre_usuario: str):
        """Destruye la ventana de login y abre la ventana principal de la app."""
        self.destroy()
        from ui.main_window import MisTareasApp
        app = MisTareasApp(nombre_usuario=nombre_usuario)
        app.mainloop()
