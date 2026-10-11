# Historial — Skill Tower

## 2026-10-10
- Se pidió una pantalla para ver sus skills, cuáles se usan con Claude y cuántos tokens se gastan, y poner orden para que no trabajen todas a la vez.
- Se creó la skill `skill-tower`: servidor local `panel.py`, página `panel.html` y semáforo `reglas.json`.
- Primera versión creada por NEXUS (nombre original: panel-nexus, renombrado a Skill Tower para publicarlo). Se recomienda agregar al CLAUDE.md global la regla de respetar el semáforo y usar una skill a la vez.
- Publicada en GitHub (público, licencia MIT).
- Rediseño completo de la pantalla con la skill impeccable: radar de actividad, "En el aire", medidor de contexto brillante, tablero de despegues y hangar con semáforo de lámparas. Adaptada a celular.
- Nuevo modo `--red` para verla desde el celular o la tablet en la misma WiFi, con clave secreta.
- Tipografía Saira Semi Condensed (OFL) servida por la propia torre; la CSP no se abrió.
- Modo automático: la torre arranca sola en cada sesión (hook SessionStart) y un guardián (hook PreToolUse) hace cumplir el semáforo: bloquea skills apagadas y las de "pedir" que el usuario no nombró. Probado con 11 casos y en vivo.
- Botón *Pantalla encendida*: en el celular la torre ya no deja que la pantalla se bloquee (pedido de Danny).
- DESIGN.md puesto al día con el documentador de impeccable: fuente Saira, botón Pantalla encendida, colores de degradados y medidas (detector: de 26 alertas a 0).
- GIF del radar en el README (grabado de la torre real) y video promocional publicado en TikTok @nexus.tech.co.

## 2026-10-11
- Pedido de Danny: cada vez que diga "prende tower", Claude debe darle el link del celular.
- Nueva opción `"abrir_en_celular"` en `reglas.json` (en el ejemplo viene en `false`). Si está en `true`, la skill arranca la torre con `--red` y entrega los dos links: PC y celular con clave.
- La skill ahora también responde a "prende la torre" y "prende tower".
