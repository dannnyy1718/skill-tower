---
name: skill-tower
description: Abre Skill Tower, la torre de control de skills en el navegador (skills y agentes instalados, cuáles se usan en la sesión, tokens y semáforo auto/pedir/apagada). Usar solo cuando el usuario pida "abre la torre", "abre el panel", "panel de skills" o /skill-tower.
---

# Skill Tower

Pantalla local (solo en este PC) que muestra:
1. Todas las skills y agentes instalados, con su peso en tokens.
2. Cuáles se han usado en la sesión actual y cuándo.
3. Tokens de la sesión: contexto actual, lo que Claude ha escrito y el costo fijo de las skills.
4. El semáforo de cada skill (`auto`, `pedir`, `apagada`), que el usuario cambia desde el panel.

## Cómo abrirlo

1. Ejecuta en segundo plano (Bash con `run_in_background: true`):
   `python "$HOME/.claude/skills/skill-tower/panel.py"`
   Si el usuario la quiere ver en el celular o la tablet, agrega `--red` y pásale la dirección
   con `?clave=` que imprime (misma WiFi). Avísale que la clave cambia en cada arranque.
2. Si ya estaba abierto, el script solo vuelve a abrir la pestaña y termina.
3. Dile al usuario la dirección que imprime (por defecto `http://127.0.0.1:8765`).
4. Si falla, mira `docs/MANUAL-DE-REPARACION.md` en esta carpeta.

## El semáforo (reglas.json)

Antes de usar CUALQUIER skill o agente, revisa `~/.claude/skills/skill-tower/reglas.json`
(si no existe, aplica `reglas.ejemplo.json`):

1. `apagada` → no la uses. Si hace falta, avísale al usuario para que la prenda en el panel.
2. `pedir` → úsala solo si el usuario la nombró o usó su palabra clave. Las sub-skills de un plugin que pidió cuentan como pedidas.
3. `auto` → puedes usarla cuando la tarea lo necesite.
4. Si una skill no aparece en el archivo, aplica `modo_por_origen` y luego `modo_por_defecto`.
5. Una skill a la vez. Antes de usarla, anuncia: "Uso la skill X porque…".
