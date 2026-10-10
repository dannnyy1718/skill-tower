"""Skill Tower: servidor local que muestra skills, agentes y tokens de Claude Code.

Por qué existe: ver en una sola pantalla qué skills tiene, cuáles se usan
en la sesión, cuántos tokens se van gastando, y poner orden (semáforo auto/pedir/apagada).

Cómo funciona:
1. Lee el inventario desde las carpetas de skills/plugins de ~/.claude.
2. Lee la sesión desde los registros .jsonl que Claude Code guarda en ~/.claude/projects.
3. Sirve una página en http://127.0.0.1:8765 que se refresca sola cada 5 segundos.

Solo usa la librería estándar de Python (nada que instalar).
Seguridad: escucha únicamente en 127.0.0.1, revisa el encabezado Host/Origin y exige un
token aleatorio para cambiar reglas, así una página web externa no puede modificarlas.
"""

import json
import re
import secrets
import socket
import sys
import threading
import time
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

CLAUDE = Path.home() / ".claude"
AQUI = Path(__file__).resolve().parent
REGLAS = AQUI / "reglas.json"
PUERTO = 8765
MODOS = ("auto", "pedir", "apagada")
TOKEN = secrets.token_urlsafe(24)

# Palabras con las que una skill "se invita sola". Se marcan como alerta porque
# empujan a Claude a usarlas sin que el usuario las pida (lección de agent-reach).
AGRESIVAS = re.compile(r"MUST USE|ALWAYS use|use proactively|proactively", re.I)

# Las que vienen dentro del programa Claude Code no tienen archivo que medir.
INTEGRADAS = {
    "code-review": "Revisa los cambios del código buscando errores.",
    "security-review": "Revisión de seguridad de los cambios pendientes.",
    "simplify": "Limpia y simplifica el código cambiado.",
    "init": "Crea el CLAUDE.md de un proyecto.",
    "run": "Arranca la app del proyecto para verla funcionando.",
    "loop": "Repite una tarea cada cierto tiempo.",
    "schedule": "Programa agentes en la nube con horario.",
    "update-config": "Cambia la configuración de Claude Code (permisos, hooks).",
    "keybindings-help": "Personaliza atajos de teclado.",
    "fewer-permission-prompts": "Reduce las preguntas de permiso repetidas.",
    "plugin-authoring": "Crea mods para la interfaz de Claude.",
    "claude-api": "Referencia de la API de Claude (modelos, precios).",
    "claude-in-chrome": "Maneja tu Chrome (clics, formularios, capturas).",
    "dataviz": "Guía para hacer gráficas y tableros.",
    "artifact-design": "Guía de diseño para páginas publicadas (Artifacts).",
    "artifact-diagramming": "Diagramas dentro de Artifacts.",
    "artifact-capabilities": "Funciones extra de los Artifacts (datos, archivos).",
}
AGENTES_INTEGRADOS = {
    "Explore": "Busca en muchos archivos y trae solo la conclusión.",
    "Plan": "Arquitecto: diseña planes de implementación.",
    "general-purpose": "Agente general para tareas de varios pasos.",
    "claude": "Agente comodín por defecto.",
    "claude-code-guide": "Responde dudas sobre Claude Code y la API.",
    "statusline-setup": "Configura la línea de estado de Claude Code.",
}
TEXTO = {".md", ".txt", ".py", ".js", ".mjs", ".ts", ".tsx", ".json", ".yaml", ".yml"}


def tokens(caracteres):
    """Aproximación usada en todo el panel: 1 token ≈ 4 caracteres."""
    return round(caracteres / 4)


def leer(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def frontmatter(texto):
    """Lee name/description del encabezado YAML sin depender de librerías externas."""
    datos = {}
    if not texto.startswith("---"):
        return datos
    fin = texto.find("\n---", 3)
    lineas = texto[3:fin].splitlines() if fin != -1 else []
    i = 0
    while i < len(lineas):
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", lineas[i])
        i += 1
        if not m:
            continue
        clave, valor = m.group(1), m.group(2).strip()
        if valor in (">", "|", ">-", "|-", ""):
            partes = []
            while i < len(lineas) and (lineas[i].startswith((" ", "\t")) or not lineas[i].strip()):
                partes.append(lineas[i].strip())
                i += 1
            valor = " ".join(p for p in partes if p)
        datos[clave] = valor.strip("\"'")
    return datos


def peso_carpeta(carpeta, limite=4000):
    """Tokens máximos si Claude leyera todos los textos de la carpeta (rara vez pasa)."""
    total, vistos = 0, 0
    for f in Path(carpeta).rglob("*"):
        if f.is_file() and f.suffix.lower() in TEXTO:
            try:
                total += f.stat().st_size
            except OSError:
                pass
            vistos += 1
            if vistos >= limite:
                break
    return tokens(total)


def item(id_, nombre, tipo, origen, desc, ruta=None, principal=None, maximo=None):
    return {
        "id": id_, "nombre": nombre, "tipo": tipo, "origen": origen, "desc": desc,
        "ruta": str(ruta) if ruta else "",
        "al_usar": principal, "maximo": maximo,
        # Costo fijo: la descripción viaja en cada mensaje aunque no se use la skill.
        "fijo": tokens(len(id_) + len(desc)) + 6,
        "agresiva": bool(AGRESIVAS.search(desc)),
    }


def skill_de_archivo(md, id_prefijo, origen, tipo="skill"):
    texto = leer(md)
    fm = frontmatter(texto)
    nombre = fm.get("name") or (md.parent.name if tipo == "skill" else md.stem)
    carpeta = md.parent if tipo == "skill" else None
    return item(
        f"{id_prefijo}{nombre}", nombre, tipo, origen, fm.get("description", ""), md,
        tokens(len(texto)), peso_carpeta(carpeta) if carpeta else tokens(len(texto)),
    )


def inventario(cwd=None):
    items = []
    usuario = CLAUDE / "skills"
    for md in sorted(usuario.glob("*/SKILL.md")):
        if md.parent.name != "synced":
            items.append(skill_de_archivo(md, "", "Tuyas"))

    for md in sorted((usuario / "synced").glob("*/*/SKILL.md")):
        items.append(skill_de_archivo(md, "anthropic-skills:", "Anthropic"))

    try:
        plugins = json.loads(leer(CLAUDE / "plugins" / "installed_plugins.json")).get("plugins", {})
    except json.JSONDecodeError:
        plugins = {}
    for clave, instalaciones in plugins.items():
        nombre_plugin = clave.split("@")[0]
        for inst in instalaciones[:1]:
            base = Path(inst.get("installPath", ""))
            for md in sorted(base.glob("skills/*/SKILL.md")):
                it = skill_de_archivo(md, f"{nombre_plugin}:", f"Plugin {nombre_plugin}")
                items.append(it)
            for md in sorted(base.glob("agents/*.md")):
                items.append(skill_de_archivo(md, f"{nombre_plugin}:", f"Plugin {nombre_plugin}", "agente"))

    # Skills y agentes del proyecto donde se está trabajando (y los instalados con `npx skills`).
    if cwd:
        p = Path(cwd)
        for md in sorted(p.glob(".claude/skills/*/SKILL.md")):
            items.append(skill_de_archivo(md, "", "Proyecto"))
        for md in sorted(p.glob(".agents/skills/*/SKILL.md")):
            items.append(skill_de_archivo(md, "", "Terceros (npx skills)"))
        for md in sorted(p.glob(".claude/agents/*.md")):
            items.append(skill_de_archivo(md, "", "Proyecto", "agente"))
    for md in sorted((CLAUDE / "agents").glob("*.md")):
        items.append(skill_de_archivo(md, "", "Tuyas", "agente"))

    for n, d in INTEGRADAS.items():
        items.append(item(n, n, "skill", "Claude Code", d))
    for n, d in AGENTES_INTEGRADOS.items():
        it = item(n, n, "agente", "Claude Code", d)
        it["fijo"] = 0  # los agentes integrados ya están en las instrucciones base
        items.append(it)

    vistos, unicos = set(), []
    for it in items:
        clave = (it["id"], it["tipo"])
        if clave not in vistos:
            vistos.add(clave)
            unicos.append(it)
    return unicos


def sesiones_recientes(n=8):
    archivos = [f for f in (CLAUDE / "projects").glob("*/*.jsonl") if f.is_file()]
    archivos.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    return archivos[:n]


def uso_de(msg):
    u = msg.get("usage") or {}
    return {
        "entrada": u.get("input_tokens", 0) or 0,
        "cache_leido": u.get("cache_read_input_tokens", 0) or 0,
        "cache_creado": u.get("cache_creation_input_tokens", 0) or 0,
        "salida": u.get("output_tokens", 0) or 0,
    }


def leer_jsonl(path):
    for linea in leer(path).splitlines():
        try:
            yield json.loads(linea)
        except json.JSONDecodeError:
            continue  # una línea a medio escribir mientras Claude trabaja; se ignora


def analizar_sesion(path):
    # Claude Code escribe una línea por bloque de respuesta con el mismo message.id;
    # se guarda solo la última de cada id para no contar tokens dos veces.
    por_id, eventos = {}, []
    titulo, cwd, modelo, turnos, ultimo_ctx = "", "", "", 0, 0
    for d in leer_jsonl(path):
        t = d.get("type")
        if t == "ai-title":
            titulo = d.get("aiTitle") or d.get("title") or titulo
        cwd = d.get("cwd") or cwd
        msg = d.get("message") or {}
        hora = d.get("timestamp", "")
        if t == "user":
            contenido = msg.get("content")
            texto = contenido if isinstance(contenido, str) else " ".join(
                c.get("text", "") for c in contenido or [] if isinstance(c, dict) and c.get("type") == "text")
            if texto and not d.get("isMeta"):
                es_resultado = isinstance(contenido, list) and any(
                    isinstance(c, dict) and c.get("type") == "tool_result" for c in contenido)
                if not es_resultado and "<system-reminder>" not in texto[:30]:
                    turnos += 1
            for cmd in re.findall(r"<command-name>/?([^<]+)</command-name>", texto or ""):
                eventos.append({"hora": hora, "tipo": "comando", "nombre": cmd.strip()})
        if t == "assistant":
            modelo = msg.get("model") or modelo
            if msg.get("id"):
                por_id[msg["id"]] = uso_de(msg)
                u = por_id[msg["id"]]
                ultimo_ctx = u["entrada"] + u["cache_leido"] + u["cache_creado"]
            for c in msg.get("content") or []:
                if not isinstance(c, dict) or c.get("type") != "tool_use":
                    continue
                entrada = c.get("input") or {}
                if c.get("name") == "Skill":
                    eventos.append({"hora": hora, "tipo": "skill", "nombre": entrada.get("skill", "?")})
                elif c.get("name") in ("Agent", "Task"):
                    eventos.append({"hora": hora, "tipo": "agente",
                                    "nombre": entrada.get("subagent_type") or "general-purpose",
                                    "detalle": entrada.get("description", "")})

    total = {k: sum(u[k] for u in por_id.values()) for k in ("entrada", "cache_leido", "cache_creado", "salida")}

    # Los agentes guardan su propio registro en una carpeta con el id de la sesión.
    agentes_salida, agentes_entrada = 0, 0
    sub = path.with_suffix("")
    if sub.is_dir():
        ids = {}
        for f in sub.rglob("*.jsonl"):
            for d in leer_jsonl(f):
                m = d.get("message") or {}
                if d.get("type") == "assistant" and m.get("id"):
                    ids[m["id"]] = uso_de(m)
        agentes_salida = sum(u["salida"] for u in ids.values())
        agentes_entrada = sum(u["entrada"] + u["cache_leido"] + u["cache_creado"] for u in ids.values())

    return {
        "id": path.stem, "titulo": titulo or path.stem[:8], "cwd": cwd, "modelo": modelo,
        "turnos": turnos, "respuestas": len(por_id), "contexto_actual": ultimo_ctx,
        "total": total, "agentes_salida": agentes_salida, "agentes_entrada": agentes_entrada,
        "eventos": eventos, "modificado": path.stat().st_mtime,
    }


def cargar_reglas():
    # reglas.json es de cada usuario (no va en el repo); la primera vez se copia del ejemplo.
    ejemplo = AQUI / "reglas.ejemplo.json"
    if not REGLAS.exists() and ejemplo.exists():
        REGLAS.write_text(leer(ejemplo), encoding="utf-8")
    try:
        r = json.loads(leer(REGLAS) or "{}")
    except json.JSONDecodeError:
        r = {}
    r.setdefault("ventana_contexto", 200000)
    r.setdefault("modo_por_defecto", "pedir")
    r.setdefault("modo_por_origen", {})
    r.setdefault("skills", {})
    return r


def modo_de(it, reglas):
    return reglas["skills"].get(it["id"]) or reglas["modo_por_origen"].get(it["origen"]) or reglas["modo_por_defecto"]


def datos(sesion_id=None):
    recientes = sesiones_recientes()
    elegida = next((f for f in recientes if f.stem == sesion_id), recientes[0] if recientes else None)
    sesion = analizar_sesion(elegida) if elegida else None
    reglas = cargar_reglas()
    items = inventario(sesion["cwd"] if sesion else None)
    usados = {}
    for e in (sesion or {}).get("eventos", []):
        if e["tipo"] in ("skill", "agente", "comando"):
            usados.setdefault(e["nombre"], []).append(e["hora"])
    for it in items:
        it["modo"] = modo_de(it, reglas)
        corto = it["id"].split(":")[-1]
        horas = usados.get(it["id"]) or usados.get(corto) or []
        it["usos"] = len(horas)
        it["ultimo_uso"] = max(horas) if horas else ""
    # Si el contexto real ya pasó la ventana configurada, el modelo tiene una ventana mayor
    # (por ejemplo 1 millón); se ajusta para no mostrar más de 100 %.
    ventana, ajustada = reglas["ventana_contexto"], False
    if sesion and sesion["contexto_actual"] > ventana:
        ventana, ajustada = max(1_000_000, sesion["contexto_actual"]), True
    return {
        "sesion": sesion,
        "sesiones": [{"id": f.stem, "proyecto": f.parent.name, "modificado": f.stat().st_mtime} for f in recientes],
        "items": items,
        "reglas": {"ventana_contexto": ventana, "ventana_ajustada": ajustada, "modo_por_defecto": reglas["modo_por_defecto"]},
        "ahora": time.time(),
    }


def guardar_regla(id_, modo):
    if modo not in MODOS or not isinstance(id_, str) or not (0 < len(id_) < 200):
        raise ValueError("Regla no válida")
    r = cargar_reglas()
    r["skills"][id_] = modo
    tmp = REGLAS.with_suffix(".tmp")
    tmp.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(REGLAS)  # escritura atómica: nunca queda un reglas.json a medias


# ---------- Modo red (celular / tablet) ----------
# Por defecto la torre solo escucha en 127.0.0.1. Con --red escucha en la WiFi de la casa,
# y todo aparato que no sea este PC debe presentar una clave aleatoria nueva en cada arranque.
MODO_RED = "--red" in sys.argv
CLAVE = secrets.token_urlsafe(12)
IP_RED = None
PAGINA_SIN_CLAVE = (
    "<!doctype html><html lang='es'><meta charset='utf-8'><meta name='viewport' content='width=device-width'>"
    "<title>Skill Tower</title><body style='font:20px system-ui;background:#061230;color:#eaf3ff;padding:32px'>"
    "Falta la clave. Abre la dirección completa que muestra la torre en tu PC "
    "(la que termina en <b>?clave=…</b>).</body></html>"
)


def ip_local():
    """IP de este PC en la red de la casa. Conectar un socket UDP no envía ningún paquete."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("10.255.255.255", 1))
            return s.getsockname()[0]
        except OSError:
            return "127.0.0.1"


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # sin ruido en la consola

    def _hosts(self):
        return {"127.0.0.1", "localhost"} | ({IP_RED} if MODO_RED and IP_RED else set())

    def _host_ok(self):
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0]
        return host in self._hosts()

    def _es_local(self):
        return self.client_address[0] in ("127.0.0.1", "::1")

    def _clave_ok(self, consulta=""):
        """Este PC entra sin clave; otro aparato necesita la cookie o ?clave= de la dirección."""
        if self._es_local():
            return True
        if secrets.compare_digest(self._cookie("st_clave"), CLAVE):
            return True
        return secrets.compare_digest(self._param(consulta, "clave"), CLAVE)

    def _cookie(self, nombre):
        for parte in (self.headers.get("Cookie") or "").split(";"):
            k, _, v = parte.strip().partition("=")
            if k == nombre:
                return v
        return ""

    @staticmethod
    def _param(consulta, nombre):
        return dict(p.split("=", 1) for p in consulta.split("&") if "=" in p).get(nombre, "")

    def _enviar(self, codigo, cuerpo, tipo="application/json; charset=utf-8", extra=None):
        datos_b = cuerpo.encode("utf-8") if isinstance(cuerpo, str) else cuerpo
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        if "Cache-Control" not in (extra or {}):
            self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy",
                         "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline'; "
                         "img-src 'self' data:; frame-ancestors 'none'")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(datos_b)

    def do_GET(self):
        if not self._host_ok():
            return self._enviar(403, '{"error":"Host no permitido"}')
        ruta, _, consulta = self.path.partition("?")
        if ruta == "/api/ping":
            return self._enviar(200, json.dumps({"ok": "skill-tower", "red": MODO_RED}))
        if not self._clave_ok(consulta):
            return self._enviar(401, PAGINA_SIN_CLAVE, "text/html; charset=utf-8")
        if ruta == "/" and self._param(consulta, "clave"):
            # Guarda la clave en una cookie y la quita de la barra de direcciones.
            return self._enviar(303, "", "text/plain", {
                "Location": "/", "Set-Cookie": f"st_clave={CLAVE}; Path=/; HttpOnly; SameSite=Strict"})
        if ruta == "/":
            html = leer(AQUI / "panel.html").replace("__TOKEN__", TOKEN)
            return self._enviar(200, html, "text/html; charset=utf-8")
        if ruta == "/media/despierto.mp4":
            return self._video(AQUI / "media" / "despierto.mp4")
        if ruta.startswith("/fuentes/"):
            # Solo se sirven los archivos de fuente conocidos: nada de rutas arbitrarias del disco.
            nombre = ruta[len("/fuentes/"):]
            if re.fullmatch(r"saira-(600|700|800)\.woff2", nombre) and (AQUI / "fuentes" / nombre).is_file():
                cuerpo = (AQUI / "fuentes" / nombre).read_bytes()
                return self._enviar(200, cuerpo, "font/woff2", {"Cache-Control": "max-age=604800"})
            return self._enviar(404, '{"error":"No existe"}')
        if ruta == "/api/datos":
            try:
                return self._enviar(200, json.dumps(datos(self._param(consulta, "sesion") or None), ensure_ascii=False))
            except Exception as e:  # el panel muestra el error en español en vez de quedarse en blanco
                return self._enviar(500, json.dumps({"error": f"No pude leer los datos: {e}"}, ensure_ascii=False))
        self._enviar(404, '{"error":"No existe"}')

    def _video(self, archivo):
        """Video que mantiene la pantalla encendida. Responde a peticiones por rangos (206),
        porque Safari en iPhone no reproduce videos de un servidor que no las soporta."""
        if not archivo.is_file():
            return self._enviar(404, '{"error":"No existe"}')
        cuerpo = archivo.read_bytes()
        total = len(cuerpo)
        m = re.fullmatch(r"bytes=(\d*)-(\d*)", self.headers.get("Range", "").strip())
        if m and (m.group(1) or m.group(2)):
            if m.group(1):
                ini, fin = int(m.group(1)), min(int(m.group(2) or total - 1), total - 1)
            else:  # "bytes=-N": los últimos N bytes
                ini, fin = max(0, total - int(m.group(2))), total - 1
            if ini > fin or ini >= total:
                return self._enviar(416, "", "text/plain", {"Content-Range": f"bytes */{total}"})
            return self._enviar(206, cuerpo[ini:fin + 1], "video/mp4", {
                "Content-Range": f"bytes {ini}-{fin}/{total}", "Accept-Ranges": "bytes", "Cache-Control": "max-age=604800"})
        return self._enviar(200, cuerpo, "video/mp4", {"Accept-Ranges": "bytes", "Cache-Control": "max-age=604800"})

    def do_POST(self):
        if self.path == "/api/apagar":
            # Solo un programa de este mismo PC (sin Origin, con la cabecera propia) puede apagar la torre;
            # un navegador no puede enviar esta cabecera a otro sitio sin permiso CORS, que aquí nunca se da.
            if self._es_local() and not self.headers.get("Origin") and self.headers.get("X-Skill-Tower") == "apagar":
                self._enviar(200, '{"ok":true}')
                threading.Thread(target=self.server.shutdown, daemon=True).start()
                return
            return self._enviar(403, '{"error":"No permitido"}')
        origen = self.headers.get("Origin", "")
        hosts = "|".join(re.escape(h) for h in self._hosts())
        if not self._host_ok() or (origen and not re.match(rf"^http://({hosts}):\d+$", origen)):
            return self._enviar(403, '{"error":"Origen no permitido"}')
        if not self._clave_ok():
            return self._enviar(401, '{"error":"Falta la clave; abre la dirección completa de la torre"}')
        if self.path != "/api/regla" or self.headers.get("X-Panel-Token") != TOKEN:
            return self._enviar(403, '{"error":"Token inválido; recarga la página"}')
        try:
            largo = min(int(self.headers.get("Content-Length", 0)), 2000)
            cuerpo = json.loads(self.rfile.read(largo) or b"{}")
            guardar_regla(cuerpo.get("id"), cuerpo.get("modo"))
            self._enviar(200, '{"ok":true}')
        except (ValueError, json.JSONDecodeError) as e:
            self._enviar(400, json.dumps({"error": str(e)}, ensure_ascii=False))


def ping(puerto):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{puerto}/api/ping", timeout=1) as r:
            d = json.loads(r.read() or b"{}")
            return d if d.get("ok") == "skill-tower" else None
    except (OSError, ValueError):
        return None


def puerto_libre(puerto):
    with socket.socket() as s:
        return s.connect_ex(("127.0.0.1", puerto)) != 0


def main():
    global IP_RED
    abrir = "--no-abrir" not in sys.argv
    activo = ping(PUERTO)
    if activo:
        if not (MODO_RED and not activo.get("red")):
            print(f"La torre ya estaba abierta: http://127.0.0.1:{PUERTO}")
        if MODO_RED and not activo.get("red"):
            print("Cambiando la torre automática a modo celular…", flush=True)
            # La torre automática corre en modo "solo este PC": se apaga y se relanza en modo red.
            pedido = urllib.request.Request(f"http://127.0.0.1:{PUERTO}/api/apagar", method="POST",
                                            headers={"X-Skill-Tower": "apagar"}, data=b"")
            urllib.request.urlopen(pedido, timeout=3).read()
            for _ in range(20):
                if puerto_libre(PUERTO):
                    break
                time.sleep(0.2)
        else:
            if abrir:
                webbrowser.open(f"http://127.0.0.1:{PUERTO}")
            return
    puerto = PUERTO if puerto_libre(PUERTO) else 0
    IP_RED = ip_local() if MODO_RED else None
    servidor = ThreadingHTTPServer(("0.0.0.0" if MODO_RED else "127.0.0.1", puerto), Manejador)
    p = servidor.server_address[1]
    url = f"http://127.0.0.1:{p}"
    print(f"Skill Tower abierto en {url}  (Ctrl+C para cerrarlo)", flush=True)
    if MODO_RED:
        print(f"Celular o tablet (misma WiFi): http://{IP_RED}:{p}/?clave={CLAVE}", flush=True)
        print("Si Windows pregunta, permite el acceso solo en 'Redes privadas'. Usa esto solo en la WiFi de tu casa.", flush=True)
    if abrir:
        webbrowser.open(url)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("Panel cerrado.")


if __name__ == "__main__":
    main()
