"""Guardián del semáforo: hook PreToolUse de Claude Code para las herramientas Skill y Agent.

Por qué existe: el semáforo de reglas.json era solo una regla que Claude "respetaba".
Con este hook se cumple de verdad, antes de que la skill o el agente arranque:
  - auto     → pasa.
  - apagada  → se bloquea siempre.
  - pedir    → pasa solo si el usuario la nombró (o usó una palabra clave) en esta sesión.

Recibe por stdin el JSON del hook (tool_name, tool_input, transcript_path).
Si algo falla, deja pasar (fail-open): un error del guardián nunca debe dejar a Claude sin trabajar.
"""

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import panel  # noqa: E402  (reutiliza reglas, listas de integradas y lectura del registro)


def origen_de(id_):
    """Mismo criterio de origen que usa el panel, sin recorrer todo el inventario."""
    if id_ in panel.INTEGRADAS or id_ in panel.AGENTES_INTEGRADOS:
        return "Claude Code"
    if id_.startswith("anthropic-skills:"):
        return "Anthropic"
    if ":" in id_:
        return "Plugin " + id_.split(":", 1)[0]
    if (panel.CLAUDE / "skills" / id_ / "SKILL.md").is_file() or (panel.CLAUDE / "agents" / f"{id_}.md").is_file():
        return "Tuyas"
    return ""


def mensajes_del_usuario(transcript):
    """Solo lo que el usuario escribió: sin resultados de herramientas ni recordatorios del sistema."""
    textos = []
    if not transcript or not Path(transcript).is_file():
        return textos
    for d in panel.leer_jsonl(Path(transcript)):
        if d.get("type") != "user" or d.get("isMeta"):
            continue
        contenido = (d.get("message") or {}).get("content")
        if isinstance(contenido, list):
            if any(isinstance(c, dict) and c.get("type") == "tool_result" for c in contenido):
                continue
            contenido = " ".join(c.get("text", "") for c in contenido if isinstance(c, dict) and c.get("type") == "text")
        if isinstance(contenido, str) and contenido.strip():
            textos.append(re.sub(r"<system-reminder>.*?</system-reminder>", " ", contenido, flags=re.S).lower())
    return textos


def fue_pedida(id_, reglas, textos):
    corto = id_.split(":")[-1]
    plugin = id_.split(":", 1)[0] if ":" in id_ else ""
    claves = [id_, corto] + ([plugin] if plugin and plugin != "anthropic-skills" else [])
    claves += reglas.get("palabras_clave", {}).get(id_, [])
    claves = [c.lower() for c in claves if c and len(c) >= 3]
    return any(c in t for t in textos for c in claves)


def responder(decision, motivo):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": decision, "permissionDecisionReason": motivo}},
        ensure_ascii=False))


def main():
    try:
        datos = json.loads(sys.stdin.read() or "{}")
    except json.JSONDecodeError:
        return
    entrada = datos.get("tool_input") or {}
    if datos.get("tool_name") == "Skill":
        id_, que = entrada.get("skill") or "", "la skill"
    elif datos.get("tool_name") in ("Agent", "Task"):
        id_, que = entrada.get("subagent_type") or "general-purpose", "el agente"
    else:
        return
    if not id_:
        return

    reglas = panel.cargar_reglas()
    modo = reglas["skills"].get(id_) or reglas["modo_por_origen"].get(origen_de(id_)) or reglas["modo_por_defecto"]

    if modo == "apagada":
        return responder("deny", f"Skill Tower: {que} '{id_}' está APAGADA en el semáforo. "
                                 "No la uses. Si de verdad hace falta, explícale al usuario por qué "
                                 "y que la prenda en la torre (http://127.0.0.1:8765).")
    if modo == "pedir" and not fue_pedida(id_, reglas, mensajes_del_usuario(datos.get("transcript_path"))):
        return responder("deny", f"Skill Tower: {que} '{id_}' está en PEDIR y el usuario no la ha nombrado "
                                 "en esta sesión. Pregúntale si quiere usarla (di cuál y para qué); "
                                 "si dice que sí, podrás usarla.")
    # auto, o pedir ya autorizada: no se dice nada y la herramienta sigue normal.


if __name__ == "__main__":
    # Claude Code lee la salida en UTF-8; en Windows Python escribiría en cp1252 y dañaría las tildes.
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        main()
    except Exception:  # fail-open: el guardián nunca tumba la sesión
        pass
