# Skill Tower 🗼

**La torre de control de tus skills de Claude Code.** Ve en tu navegador todas las skills y agentes que tienes, cuáles está usando Claude en este momento, cuántos tokens llevas gastados, y decide cuáles pueden "despegar" con un semáforo.

Gratis y de código abierto (licencia MIT). Hecho por **NEXUS**.

## Qué muestra
1. **Tokens de la sesión:** contexto actual (con barra de llenado), lo escrito por Claude, lo leído en total, el costo fijo de las skills por mensaje y lo gastado por agentes.
2. **Usadas en la sesión:** skills, agentes y comandos, con su línea de tiempo. Se actualiza cada 5 segundos.
3. **Semáforo:** cada skill en `auto`, `pedir` o `apagada`, para que no se activen todas a la vez ni por su cuenta.
4. **Inventario:** todas las skills y agentes (tuyas, de plugins, de Anthropic, del proyecto y de terceros), con su peso en tokens y alertas:
   - **se invita sola**: su descripción le pide a Claude usarla sin que tú la pidas.
   - **terceros sin revisar**: instalada con `npx skills` desde un repo ajeno.

## Requisitos
- [Claude Code](https://claude.com/claude-code)
- Python 3.8 o superior. No necesita librerías extra.

## Instalación
```bash
git clone https://github.com/dannnyy1718/skill-tower ~/.claude/skills/skill-tower
```
Después, en Claude Code escribe **"abre la torre"** o `/skill-tower`.

También lo puedes abrir a mano:
```bash
python ~/.claude/skills/skill-tower/panel.py            # abre el navegador
python ~/.claude/skills/skill-tower/panel.py --no-abrir # solo el servidor
```

### Para que Claude respete el semáforo siempre
Agrega esto a tu `~/.claude/CLAUDE.md`:
```markdown
## Orden de skills (Skill Tower)
Antes de usar una skill o agente, revisa ~/.claude/skills/skill-tower/reglas.json:
apagada = no usar; pedir = solo si yo la nombro; auto = libre. Una skill a la vez y anuncia cuál usas y por qué.
```

## Privacidad y seguridad
- Todo se queda en tu PC: el servidor escucha solo en `127.0.0.1` y no envía nada a internet.
- Solo lee las carpetas de Claude Code (`~/.claude`) y nunca muestra el texto de tus conversaciones, solo los nombres de las skills y los conteos de tokens.
- Para cambiar el semáforo pide un token aleatorio y revisa el origen de la petición, así ninguna página externa puede modificarlo.

## Archivos
| Archivo | Para qué |
|---|---|
| `SKILL.md` | Lo que lee Claude: cómo abrir la torre y respetar el semáforo |
| `panel.py` | Servidor local |
| `panel.html` | La pantalla |
| `reglas.ejemplo.json` | Semáforo inicial; la primera vez se copia a `reglas.json` (personal, no va al repo) |
| `docs/` | Manual de reparación, decisiones e historial |

## Cómo calcula los tokens
- **Sesión:** exactos. Salen de los registros `~/.claude/projects/<proyecto>/<sesión>.jsonl` que guarda Claude Code.
- **Skills:** aproximados (1 token ≈ 4 caracteres de sus archivos).
- **% de contexto:** se calcula contra `ventana_contexto` en `reglas.json` (200.000 por defecto). Cámbialo según tu modelo.
