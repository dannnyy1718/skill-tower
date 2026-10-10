"""Arranque automático: hook SessionStart de Claude Code.

Si la torre no está corriendo, la lanza en segundo plano (solo en este PC, sin abrir el
navegador) y termina enseguida para no demorar el inicio de la sesión.
Lo que imprime entra al contexto de Claude, así que se mantiene en una sola línea.
"""

import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import panel  # noqa: E402


def main():
    if not panel.ping(panel.PUERTO):
        opciones = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL,
                    "close_fds": True, "cwd": str(AQUI)}
        if sys.platform == "win32":
            # Proceso independiente y sin ventana: sigue vivo aunque se cierre la sesión de Claude.
            opciones["creationflags"] = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        else:
            opciones["start_new_session"] = True
        subprocess.Popen([sys.executable, str(AQUI / "panel.py"), "--no-abrir"], **opciones)
    print(f"Skill Tower activa en http://127.0.0.1:{panel.PUERTO}; el guardián hace cumplir el semáforo de skills.")


if __name__ == "__main__":
    # Claude Code lee la salida en UTF-8; en Windows Python escribiría en cp1252 y dañaría las tildes.
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        main()
    except Exception as e:  # nunca bloquear el inicio de la sesión
        print(f"Skill Tower no pudo arrancar sola: {e}")
