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

## 2026-10-28
- Nueva sección **Oficina** (pedido de Danny, inspirada en un TikTok de @ioao7): plano isométrico en SVG con 3 salas (dirección, estudio de skills y sala de agentes), escritorios con pantalla, plantas, carteles y gráfica animada en la pared.
- El jefe es quien usa la torre (`"nombre_jefe"` en `reglas.json`; para Danny, "Danny · jefe") y Claude Code está a su lado como el muñequito naranja de bloques (de la foto que mandó Danny).
- Estado real desde los registros: agentes que siguen corriendo (ficha `.meta.json` de cada agente), skills usadas hace menos de 5 min y Claude Code mientras la sesión se mueve. "Modo vitrina" (encendido de entrada) pone a todos a trabajar para videos.
- El nombre de cada uno va encima de su cabeza; los puntitos verdes de "trabajando" van en la misma placa.
- Cuando Claude llama una skill o un agente, su muñequito corre (con rebote, bamboleo, polvito y sudor) hasta la oficina del jefe, lo saluda con la mano y vuelve a su puesto.
- En celular el plano se desliza de lado dentro de su marco y arranca centrado en la dirección. Probado en PC (1440 px) y celular (390 px), sin errores en la consola.
