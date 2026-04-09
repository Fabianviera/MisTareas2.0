import re
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from config import C
from lang import T
import auth.store as auth_store
import auth.crypto as crypto
import data.task_store as task_store


class VentanaLogin(ctk.CTk):
    _REGEX_USUARIO = re.compile(r'^[a-zA-Z0-9_-]+$')

    def __init__(self):
        super().__init__()

        self.title(T["login_title_window"])
        self.resizable(False, False)
        self.configure(fg_color=C["bg"])

        self._ancho  = 400
        self._alto_login    = 520
        self._alto_registro = 660

        self.update_idletasks()
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla  = self.winfo_screenheight()
        self._centrar(self._alto_login)

        self._estado = "login"
        self._construir_ui()

    def _centrar(self, alto: int):
        self.update_idletasks()
        x = (self.winfo_screenwidth()  - self._ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{self._ancho}x{alto}+{x}+{y}")

    # ── Construcción de la UI ─────────────────────────────────────────────────

    def _construir_ui(self):
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

        self._lbl_titulo = ctk.CTkLabel(
            self._contenedor, text=T["login_title"],
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=C["text"]
        )
        self._lbl_titulo.pack(pady=(0, 18))

        # ── Campos de REGISTRO ──
        self._frame_registro = ctk.CTkFrame(self._contenedor, fg_color="transparent")

        ctk.CTkLabel(
            self._frame_registro, text=T["lbl_display_name"],
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        self._ent_nombre_mostrar = ctk.CTkEntry(
            self._frame_registro, placeholder_text=T["ph_display_name"],
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_nombre_mostrar.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            self._frame_registro, text=T["lbl_username_reg"],
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        self._ent_usuario_reg = ctk.CTkEntry(
            self._frame_registro, placeholder_text=T["ph_username_reg"],
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_usuario_reg.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(
            self._frame_registro, text=T["lbl_password_reg"],
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        fila_pass_reg = ctk.CTkFrame(self._frame_registro, fg_color="transparent")
        fila_pass_reg.pack(fill="x", pady=(0, 10))
        self._ent_pass_reg = ctk.CTkEntry(
            fila_pass_reg, show="•", placeholder_text=T["ph_password"],
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
            self._frame_registro, text=T["lbl_confirm_password"],
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        fila_pass_conf = ctk.CTkFrame(self._frame_registro, fg_color="transparent")
        fila_pass_conf.pack(fill="x", pady=(0, 10))
        self._ent_pass_conf = ctk.CTkEntry(
            fila_pass_conf, show="•", placeholder_text=T["ph_confirm"],
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
            self._frame_login, text=T["lbl_username_login"],
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        self._ent_usuario_login = ctk.CTkEntry(
            self._frame_login, placeholder_text=T["ph_username_login"],
            fg_color=C["input_bg"], border_color=C["border"],
            text_color=C["text"], placeholder_text_color=C["text_muted"],
            height=40, corner_radius=10
        )
        self._ent_usuario_login.pack(fill="x", pady=(0, 14))

        ctk.CTkLabel(
            self._frame_login, text=T["lbl_password_login"],
            font=ctk.CTkFont(size=12), text_color=C["text_muted"], anchor="w"
        ).pack(fill="x", pady=(0, 2))
        fila_pass_login = ctk.CTkFrame(self._frame_login, fg_color="transparent")
        fila_pass_login.pack(fill="x", pady=(0, 14))
        self._ent_pass_login = ctk.CTkEntry(
            fila_pass_login, show="•", placeholder_text=T["ph_password"],
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
            self._contenedor, text=T["btn_login"],
            height=44, corner_radius=12,
            fg_color=C["accent"], hover_color=C["accent_hover"],
            text_color="white", font=ctk.CTkFont(size=15, weight="bold"),
            command=self._accion_principal
        )
        self._btn_accion.pack(fill="x", pady=(4, 0))

        self._lbl_error = ctk.CTkLabel(
            self._contenedor, text="",
            font=ctk.CTkFont(size=12),
            text_color=C["text_priority"]
        )
        self._lbl_error.pack(pady=(6, 0))

        self._btn_cambiar_estado = ctk.CTkButton(
            self._contenedor, text=T["btn_new_account"],
            fg_color="transparent", hover_color=C["task_hover"],
            text_color=C["accent"], font=ctk.CTkFont(size=13, underline=True),
            height=32, corner_radius=8,
            command=self._cambiar_estado
        )
        self._btn_cambiar_estado.pack(pady=(4, 0))

        # ── Footer ──
        pie = ctk.CTkFrame(self, fg_color=C["header"], corner_radius=0, height=24)
        pie.pack(fill="x", side="bottom")
        pie.pack_propagate(False)
        ctk.CTkLabel(
            pie, text="v2.1",
            font=ctk.CTkFont(size=10), text_color=C["text_muted"]
        ).pack(expand=True)

        self._mostrar_estado_login()

    # ── Cambio de estado ──────────────────────────────────────────────────────

    def _mostrar_estado_login(self):
        self._frame_registro.pack_forget()
        self._frame_login.pack(fill="x", before=self._btn_accion)
        self._lbl_titulo.configure(text=T["login_title"])
        self._btn_accion.configure(text=T["btn_login"], command=self._intentar_login)
        self._btn_cambiar_estado.configure(text=T["btn_new_account"])
        self._lbl_error.configure(text="")
        self._centrar(self._alto_login)
        self._ent_usuario_login.focus_set()

    def _mostrar_estado_registro(self):
        self._frame_login.pack_forget()
        self._frame_registro.pack(fill="x", before=self._btn_accion)
        self._lbl_titulo.configure(text=T["register_title"])
        self._btn_accion.configure(text=T["btn_register"], command=self._intentar_registro)
        self._btn_cambiar_estado.configure(text=T["btn_have_account"])
        self._lbl_error.configure(text="")
        self._centrar(self._alto_registro)
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
            self._mostrar_error(T["err_fill_all"])
            return

        resultado = auth_store.autenticar(usuario, contrasena)
        if resultado is None:
            self._mostrar_error(T["err_wrong_credentials"])
            return

        nombre_usuario = resultado["nombre_usuario"]
        clave = crypto.derivar_clave(nombre_usuario, contrasena)
        self._lanzar_app(nombre_usuario, clave)

    # ── Registro ──────────────────────────────────────────────────────────────

    def _intentar_registro(self):
        nombre_mostrar  = self._ent_nombre_mostrar.get().strip()
        nombre_usuario  = self._ent_usuario_reg.get().strip()
        contrasena      = self._ent_pass_reg.get()
        contrasena_conf = self._ent_pass_conf.get()

        if not nombre_mostrar:
            self._mostrar_error(T["err_display_name"])
            return
        if not nombre_usuario:
            self._mostrar_error(T["err_username_empty"])
            return
        if not self._REGEX_USUARIO.match(nombre_usuario):
            self._mostrar_error(T["err_username_invalid"])
            return
        if len(contrasena) < 6:
            self._mostrar_globo(self._ent_pass_reg, T["tip_password_short"])
            return
        if contrasena != contrasena_conf:
            self._mostrar_globo(self._ent_pass_conf, T["tip_password_mismatch"])
            return

        creado = auth_store.crear_usuario(nombre_usuario, nombre_mostrar, contrasena)
        if not creado:
            self._mostrar_error(T["err_user_exists"].format(nombre_usuario))
            return

        nombre_usuario_lower = nombre_usuario.lower()
        clave = crypto.derivar_clave(nombre_usuario_lower, contrasena)

        if task_store.hay_migracion_pendiente():
            respuesta = messagebox.askyesno(
                T["migration_title"], T["migration_msg"]
            )
            if respuesta:
                tareas_legacy = task_store.obtener_tareas_migracion()
                task_store.guardar_tareas(tareas_legacy, nombre_usuario_lower, clave)
            task_store.marcar_migracion_completada()

        self._lanzar_app(nombre_usuario_lower, clave)

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _mostrar_globo(self, widget, mensaje: str):
        if hasattr(self, "_globo") and self._globo.winfo_exists():
            self._globo.destroy()

        globo = tk.Toplevel(self)
        globo.overrideredirect(True)
        globo.attributes("-topmost", True)
        self._globo = globo

        self.update_idletasks()
        x = widget.winfo_rootx()
        y = widget.winfo_rooty() + widget.winfo_height() + 4

        fondo = C["text_priority"]
        frame = tk.Frame(globo, bg=fondo, padx=10, pady=6)
        frame.pack()
        tk.Label(frame, text=mensaje, bg=fondo, fg="white",
                 font=("Segoe UI", 10), justify="left").pack()

        globo.geometry(f"+{x}+{y}")
        globo.after(3000, lambda: globo.destroy() if globo.winfo_exists() else None)
        globo.bind("<Button-1>", lambda _: globo.destroy())
        self.bind("<Button-1>", lambda _: globo.destroy() if globo.winfo_exists() else None, add="+")

    def _mostrar_error(self, mensaje: str):
        self._lbl_error.configure(text=mensaje)

    def _alternar_visibilidad(self, entrada: ctk.CTkEntry):
        actual = entrada.cget("show")
        entrada.configure(show="" if actual else "•")

    def _lanzar_app(self, nombre_usuario: str, clave: bytes):
        self.destroy()
        from ui.main_window import MisTareasApp
        app = MisTareasApp(nombre_usuario=nombre_usuario, clave=clave)
        app.mainloop()
