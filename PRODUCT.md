# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users
Personas hispanohablantes que usan Claude Code (el autor, Danny de NEXUS, y cualquiera que clone el repo).
Abren la torre en una pestaña al lado de la terminal mientras trabajan con Claude, y la miran de reojo.

## Product Purpose
Mostrar en una pantalla local qué skills y agentes hay instalados, cuáles está usando Claude en este momento,
cuántos tokens lleva la sesión, y dejar que el usuario decida con un semáforo (auto / pedir / apagada)
cuáles pueden activarse. Éxito: de un vistazo se sabe qué está activo ahora y qué tan lleno va el contexto.

## Positioning
Torre de control: no solo lista skills, muestra en vivo cuáles "despegan" en la sesión real (lee los registros
.jsonl de Claude Code) y le da al usuario la autorización de despegue.

## Operating Context
Pestaña del navegador en 127.0.0.1, refresco cada 5 s, junto a la terminal de Claude Code. Sesiones largas.

## Capabilities and Constraints
- Python estándar + un único HTML con CSS/JS en línea; sin librerías ni fuentes externas (CSP 'self').
- Datos: sesión (contexto, tokens, eventos), inventario (~100 skills/agentes), reglas (semáforo).
- Interfaz en español.

## Brand Commitments
- Nombre "Skill Tower"; firmado "hecho por NEXUS".
- NEXUS: azul oscuro profundo, cian y verde brillantes; al autor le gusta lo brillante/3D, no lo plano (petición explícita).
- Metáfora de torre de control aérea (radar, despegue, semáforo).

## Evidence on Hand
Datos reales de la sesión del usuario. No inventar métricas ni testimonios.

## Product Principles
1. Lo activo ahora va primero.
2. Todo local y privado: nunca se muestra el texto de las conversaciones.
3. El usuario autoriza; las skills no despegan solas.
4. Legible de reojo: letra grande, alto contraste.

## Accessibility & Inclusion
WCAG 2.2 AA, navegación con teclado, letra grande (el autor lo pide), respeta prefers-reduced-motion.
