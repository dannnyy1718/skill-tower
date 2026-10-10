# Manual de reparación — Skill Tower

| # | Síntoma | Causa probable | Cómo arreglarlo |
|---|---|---|---|
| 1 | El navegador dice "No se puede acceder al sitio" | El servidor no está corriendo | Correr `python ~/.claude/skills/skill-tower/panel.py` |
| 2 | Banda roja "No pude actualizar el panel" | Se cerró `panel.py` (por ejemplo, al terminar la sesión de Claude) | Volver a arrancarlo (punto 1) y recargar la página |
| 3 | "Token inválido; recarga la página" al cambiar un semáforo | Se reinició el servidor y el token cambió | Recargar la página (F5) |
| 4 | Abre en un puerto distinto de 8765 | Otro programa ocupa el 8765 | Normal: usar la dirección que imprime la terminal |
| 5 | Una skill nueva no aparece | Está en una carpeta que el panel no revisa | Agregar la ruta en `inventario()` de `panel.py` |
| 6 | Los tokens de la sesión salen en 0 | Claude Code cambió el formato del `.jsonl` | Revisar una línea `"type":"assistant"` y ajustar `uso_de()` |
| 7 | El % de contexto parece raro | `ventana_contexto` en `reglas.json` no coincide con el modelo | Ajustar ese número (200000 por defecto) |
| 8 | `reglas.json` dañado | Se editó a mano con un error de formato | El panel usa valores por defecto; corregir el JSON, o borrarlo: se vuelve a crear desde `reglas.ejemplo.json` |
| 9 | `python` no se reconoce | Python no está en el PATH | Usar `py -3 panel.py` o la ruta completa de Python |
| 10 | El celular no abre la dirección | Distinta WiFi, o el firewall de Windows la bloquea | Misma WiFi que el PC; en "Firewall de Windows → Permitir una aplicación", habilitar Python solo en red **privada** |
| 11 | El celular dice "Falta la clave" | Se abrió sin `?clave=` o la torre se reinició (clave nueva) | Copiar otra vez la dirección completa que muestra la terminal |
| 12 | El contexto dice "se ajustó a 1.000.000" | El contexto real pasó la `ventana_contexto` configurada | Normal en modelos con memoria grande; poner el valor real en `reglas.json` |
