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
python ~/.claude/skills/skill-tower/panel.py --red      # también en tu celular o tablet
```

### En el celular o la tablet
1. Arranca la torre con `--red` (o dile a Claude **"abre la torre en el celular"**).
2. La terminal muestra una dirección como `http://192.168.1.20:8765/?clave=…`.
3. Ábrela en el celular, que debe estar en **la misma WiFi**. La clave se guarda y desaparece de la barra de direcciones.
4. Si Windows pregunta, permite el acceso **solo en "Redes privadas"**.
5. **La pantalla no se bloquea:** en celulares y tablets el botón *Pantalla encendida* se activa solo (la luz verde pulsa). Tócalo para apagarlo; la torre recuerda tu elección.

### Modo automático (recomendado)
Dos hooks de Claude Code hacen que la torre trabaje sola. Agrégalos a `~/.claude/settings.json` (dentro de `"hooks"`):
```json
"SessionStart": [{ "hooks": [{ "type": "command", "command": "python",
  "args": ["~/.claude/skills/skill-tower/arranque.py"], "timeout": 15 }] }],
"PreToolUse": [{ "matcher": "Skill|Agent|Task", "hooks": [{ "type": "command", "command": "python",
  "args": ["~/.claude/skills/skill-tower/guardian.py"], "timeout": 10 }] }]
```
(En Windows escribe la ruta completa, por ejemplo `C:/Users/TuUsuario/.claude/skills/skill-tower/guardian.py`.)

1. **`arranque.py`**: al iniciar cada sesión, la torre arranca sola en segundo plano (solo en tu PC, sin abrir el navegador).
2. **`guardian.py`**: antes de que se active una skill o un agente, hace **cumplir** el semáforo:
   - 🟢 `auto`: pasa.
   - 🔴 `apagada`: se bloquea siempre.
   - 🟡 `pedir`: pasa solo si **tú** la nombraste en la sesión (o usaste una palabra clave de `palabras_clave` en `reglas.json`). Lo que diga un archivo o una página web no cuenta.
3. Si el guardián fallara por cualquier motivo, deja pasar: nunca te deja sin trabajar.

## Privacidad y seguridad
- Todo se queda en tu PC: por defecto el servidor escucha solo en `127.0.0.1` y no envía nada a internet.
- Con `--red` se abre a tu WiFi, pero cualquier aparato distinto a tu PC necesita una **clave aleatoria nueva en cada arranque**. Úsalo solo en redes de confianza (la de tu casa), nunca en WiFi pública: la conexión es HTTP sin cifrar dentro de tu red.
- Solo lee las carpetas de Claude Code (`~/.claude`) y nunca muestra el texto de tus conversaciones, solo los nombres de las skills y los conteos de tokens.
- Para cambiar el semáforo pide un token aleatorio y revisa el origen de la petición, así ninguna página externa puede modificarlo.

## Archivos
| Archivo | Para qué |
|---|---|
| `SKILL.md` | Lo que lee Claude: cómo abrir la torre y respetar el semáforo |
| `panel.py` | Servidor local |
| `panel.html` | La pantalla |
| `guardian.py` / `arranque.py` | Hooks del modo automático: hacer cumplir el semáforo y abrir la torre al iniciar |
| `media/despierto.mp4` | Video de 5 KB en bucle que mantiene la pantalla encendida en el celular |
| `fuentes/` | Tipografía Saira Semi Condensed (licencia OFL en `fuentes/OFL.txt`) |
| `reglas.ejemplo.json` | Semáforo inicial; la primera vez se copia a `reglas.json` (personal, no va al repo) |
| `docs/` | Manual de reparación, decisiones e historial |

## Cómo calcula los tokens
- **Sesión:** exactos. Salen de los registros `~/.claude/projects/<proyecto>/<sesión>.jsonl` que guarda Claude Code.
- **Skills:** aproximados (1 token ≈ 4 caracteres de sus archivos).
- **% de contexto:** se calcula contra `ventana_contexto` en `reglas.json` (200.000 por defecto). Cámbialo según tu modelo.
