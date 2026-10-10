---
version: 1
slug: "panel-html"
primary_target: "panel.html"
related_targets: []
---

## Scope
panel.html — única pantalla de Skill Tower. Modo: Operate. Seed key: 1eaf8292 (sorteo superado por brief fijado: marca NEXUS + torre de control, pedido explícito del usuario).

## Task
Ver de reojo qué skill/agente está activo ahora y cuánto contexto va; luego ordenar el semáforo. Datos reales, refresco 5 s.

## Direction contract
THESIS: Una torre de control, no un listado: lo que despegó en la sesión aparece en un radar vivo. Rechaza la grilla de tarjetas de métricas iguales.
OWN-WORLD: Azul NEXUS profundo como campo propio (no gris), cian = skills, verde = autorizado/ok, ámbar = agentes/pedir, rojo = apagada/crítico. Material brillante 3D: biseles, brillo superior, sombras suaves con desplazamiento, cúpula de vidrio solo en radar, medidor y lámparas.
STORY: Abro la torre, veo qué está "en el aire", cuánto combustible (contexto) queda, y autorizo o apago skills desde el hangar.
FIRST VIEWPORT: Barra superior (marca, sesión, en vivo). Izquierda: radar grande con barrido; blips = skills/agentes usados, distancia al centro = tiempo desde su uso. Derecha: "En el aire" (último evento) + medidor de contexto grande + fila de lecturas (escritos, leídos, costo fijo, agentes, turnos).
SIGNATURE: El radar de actividad: barrido que ilumina cada blip al pasar; un uso nuevo emite un pulso.
DEPTH: Tablero de despegues (línea de tiempo con estado En vuelo/Aterrizó) y Hangar (inventario con semáforo de 3 lámparas como grupo de radio, filtros, orden).
