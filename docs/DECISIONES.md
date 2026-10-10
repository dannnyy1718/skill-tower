# Decisiones — Skill Tower

1. **Skill de usuario (`~/.claude/skills`), no de proyecto.** Así el panel funciona en cualquier carpeta y ve todas las sesiones.
2. **Python estándar, sin librerías.** No hay nada que instalar, lo que evita fallas de descarga con antivirus que inspeccionan HTTPS.
3. **Servidor local en vez de un HTML fijo.** Un archivo HTML suelto no puede leer los registros en vivo; el servidor sí, y la página se refresca cada 5 s.
4. **Seguridad del servidor:** escucha solo en 127.0.0.1, revisa Host/Origin y pide un token aleatorio para cambiar reglas. Así ninguna página web externa puede tocar el semáforo.
5. **Las descripciones se muestran con `textContent`.** Vienen de skills de terceros y no deben poder inyectar código en el panel.
6. **Semáforo de 3 estados (auto/pedir/apagada).** Por defecto: Claude Code y Anthropic en `auto`; plugins y terceros en `pedir`. Así Claude no usa skills por su cuenta: el usuario decide.
7. **El semáforo es una regla para Claude, no un bloqueo técnico.** Claude lo lee antes de usar una skill (regla en el CLAUDE.md global). Para apagar un plugin de verdad se usa `/plugin` en Claude Code.
8. **Tokens de skills ≈ caracteres / 4.** Es una estimación; los tokens de la sesión sí son exactos porque vienen de la API.
