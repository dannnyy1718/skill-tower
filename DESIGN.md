---
name: Skill Tower
description: Torre de control local de skills y agentes de Claude Code, en el mundo NEXUS (azul profundo, cian y verde brillantes, material 3D).
colors:
  campo: "#061230"
  campo-hondo: "#030a1e"
  placa: "#0d2150"
  placa-baja: "#0a1a40"
  control-alto: "#13306b"
  control-bajo: "#0c2152"
  linea: "rgba(126, 196, 255, 0.18)"
  linea-fuerte: "rgba(126, 196, 255, 0.34)"
  blanco-titular: "#ffffff"
  texto: "#eaf3ff"
  suave: "#a6bfe3"
  tenue: "#8aa6d0"
  cian: "#2ee6ff"
  verde: "#3ef0a1"
  ambar: "#ffc542"
  rojo: "#ff7070"
  barra-alta: "#0e2456"
  barra-baja: "#081638"
  cabecera-alta: "#15336f"
  cabecera-baja: "#0f2759"
  aviso-alto: "#17407e"
  aviso-bajo: "#0f2a5c"
  carcasa-alta: "#050d24"
  carcasa-baja: "#0b1838"
  tinta-envuelo: "#031a22"
  icono-skill-alto: "#1fb8d6"
  icono-skill-bajo: "#0a5f86"
  icono-agente-alto: "#e6a91d"
  icono-agente-bajo: "#8a5a06"
  icono-comando-alto: "#22c784"
  icono-comando-bajo: "#0b6a45"
  icono-vacio-alto: "#23406f"
  icono-vacio-bajo: "#142a52"
  tubo-verde-brillo: "#8dffd0"
  tubo-verde-fondo: "#18a86b"
  tubo-ambar-brillo: "#ffe39b"
  tubo-ambar-fondo: "#c58a06"
  tubo-rojo-brillo: "#ffb3b3"
  tubo-rojo-fondo: "#b52a2a"
  lampara-verde-apagada: "#14412f"
  lampara-ambar-apagada: "#47380f"
  lampara-roja-apagada: "#4a1d1d"
  sombra-lampara: "rgba(0, 0, 0, 0.5)"
  texto-error: "#ffe1e1"
  borde-barrido: "#8ff6ff"
typography:
  marca:
    fontFamily: "\"Saira Semi Condensed\", \"Segoe UI Variable Display\", \"Segoe UI\", system-ui, -apple-system, sans-serif"
    fontSize: "26px"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "0.12em"
  display:
    fontFamily: "\"Saira Semi Condensed\", \"Segoe UI Variable Display\", \"Segoe UI\", system-ui, -apple-system, sans-serif"
    fontSize: "clamp(30px, 3vw, 40px)"
    fontWeight: 800
    lineHeight: 1
    fontFeature: "tnum"
  headline:
    fontFamily: "\"Saira Semi Condensed\", \"Segoe UI Variable Display\", \"Segoe UI\", system-ui, -apple-system, sans-serif"
    fontSize: "clamp(24px, 2.4vw, 32px)"
    fontWeight: 700
    lineHeight: 1.15
  title:
    fontFamily: "\"Saira Semi Condensed\", \"Segoe UI Variable Display\", \"Segoe UI\", system-ui, -apple-system, sans-serif"
    fontSize: "21px"
    fontWeight: 700
    lineHeight: 1.2
  lectura:
    fontFamily: "\"Saira Semi Condensed\", \"Segoe UI Variable Display\", \"Segoe UI\", system-ui, -apple-system, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.2
    fontFeature: "tnum"
  divisor:
    fontFamily: "\"Saira Semi Condensed\", \"Segoe UI Variable Display\", \"Segoe UI\", system-ui, -apple-system, sans-serif"
    fontSize: "17px"
    fontWeight: 600
    lineHeight: 1
    fontFeature: "tnum"
  body:
    fontFamily: "\"Segoe UI Variable Text\", \"Segoe UI\", system-ui, -apple-system, \"Helvetica Neue\", sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  body-celular:
    fontFamily: "\"Segoe UI Variable Text\", \"Segoe UI\", system-ui, -apple-system, \"Helvetica Neue\", sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.5
    fontFeature: "tnum"
  detalle:
    fontFamily: "\"Segoe UI Variable Text\", \"Segoe UI\", system-ui, -apple-system, \"Helvetica Neue\", sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
  body-ayuda:
    fontFamily: "\"Segoe UI Variable Text\", \"Segoe UI\", system-ui, -apple-system, \"Helvetica Neue\", sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "\"Segoe UI Variable Text\", \"Segoe UI\", system-ui, -apple-system, \"Helvetica Neue\", sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.5
  escala:
    fontFamily: "\"Segoe UI Variable Text\", \"Segoe UI\", system-ui, -apple-system, \"Helvetica Neue\", sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  orden: "6px"
  enfoque: "8px"
  control: "12px"
  bandeja: "14px"
  icono: "16px"
  placa: "18px"
  pastilla: "99px"
spacing:
  celda: "11px 14px"
  control: "9px 14px"
  hueco: "22px"
  placa: "22px clamp(16px, 2vw, 28px)"
  margen-pagina: "clamp(16px, 3vw, 36px)"
  pie: "40px"
components:
  placa:
    backgroundColor: "{colors.placa}"
    textColor: "{colors.texto}"
    rounded: "{rounded.placa}"
    padding: "{spacing.placa}"
  campo-control:
    backgroundColor: "{colors.control-alto}"
    textColor: "{colors.texto}"
    rounded: "{rounded.control}"
    padding: "{spacing.control}"
  tabla-bandeja:
    backgroundColor: "{colors.campo-hondo}"
    textColor: "{colors.texto}"
    rounded: "{rounded.bandeja}"
    padding: "{spacing.celda}"
  tabla-cabecera:
    backgroundColor: "{colors.cabecera-alta}"
    textColor: "{colors.cian}"
    typography: "{typography.label}"
    padding: "{spacing.celda}"
  estado-envuelo:
    backgroundColor: "{colors.cian}"
    textColor: "{colors.campo-hondo}"
    typography: "{typography.label}"
    rounded: "{rounded.pastilla}"
    padding: "2px 10px"
  estado-aterrizo:
    backgroundColor: "{colors.placa-baja}"
    textColor: "{colors.suave}"
    typography: "{typography.label}"
    rounded: "{rounded.pastilla}"
    padding: "2px 10px"
  semaforo:
    backgroundColor: "{colors.campo-hondo}"
    rounded: "{rounded.pastilla}"
    padding: "5px 7px"
  lampara:
    rounded: "{rounded.pastilla}"
    size: "22px"
  icono-vuelo:
    textColor: "{colors.blanco-titular}"
    rounded: "{rounded.icono}"
    size: "58px"
  boton-despierto:
    backgroundColor: "{colors.control-alto}"
    textColor: "{colors.texto}"
    typography: "{typography.detalle}"
    rounded: "{rounded.pastilla}"
    padding: "6px 14px 6px 8px"
  luz-despierto:
    backgroundColor: "{colors.lampara-verde-apagada}"
    rounded: "{rounded.pastilla}"
    size: "20px"
  boton-orden:
    textColor: "{colors.cian}"
    typography: "{typography.label}"
    rounded: "{rounded.orden}"
---

# Design System: Skill Tower

## Overview

**Creative North Star: "La Torre de Control NEXUS"**

Skill Tower es un tablero de torre de control dibujado en el azul profundo de NEXUS. El fondo no es gris: es un campo azul casi negro con dos resplandores suaves (cian arriba a la izquierda, verde arriba a la derecha) que dan la sensación de una sala de radar de noche. Sobre ese campo flotan placas de instrumentos con bisel y sombra blanda; lo que está vivo (blips, lámparas, el combustible del contexto, la luz "En vivo") emite luz propia en cian, verde, ámbar o rojo.

La densidad es de instrumento, no de documento: letra grande (18 px de base), números tabulares, lecturas separadas por filetes finos y no por cajas. El material es brillante y tridimensional porque la marca lo pide (el autor rechaza lo plano), pero el vidrio y el brillo especular se reservan para los instrumentos: radar, medidor, lámparas e icono de vuelo. Las placas solo llevan bisel.

El movimiento cuenta el estado: el barrido del radar gira cada 4 s y enciende cada blip al pasar; un uso nuevo emite un pulso; el medidor se llena con desaceleración larga. Todo se detiene con `prefers-reduced-motion`.

**Key Characteristics:**
- Campo azul NEXUS propio (#061230 a #030a1e), nunca gris neutro.
- Código de color de vuelo: cian = skill, ámbar = agente/pedir, verde = comando/auto/ok, rojo = apagada/crítico.
- Placas con bisel (luz arriba, sombra abajo) y sombra blanda desplazada hacia abajo.
- Vidrio y brillo especular solo en instrumentos (radar, medidor, lámparas, icono de vuelo).
- Letra grande, números tabulares, alto contraste sobre azul.

## Colors

Un campo azul de medianoche con cuatro luces de señal saturadas; las luces significan algo, nunca decoran.

### Primary
- **Cian Radar** (cian): voz principal. Skills, iconos de sección, cabeceras de tabla, anillos y barrido del radar, anillo de foco, borde del aviso, la palabra "NEXUS" del pie y la pastilla "En vuelo".

### Secondary
- **Verde Autorizado** (verde): comandos, modo "auto", medidor de contexto en zona sana, luz "En vivo", centro del radar y el lema bajo la marca.

### Tertiary
- **Ámbar Agente** (ambar): agentes, modo "pedir", medidor en alerta y la etiqueta "agresiva".
- **Rojo Apagada** (rojo): modo "apagada", medidor crítico, panel de error y la etiqueta "terceros" (texto en #ff9c9c para contraste).

### Neutral
- **Campo NEXUS** (campo) y **Campo Hondo** (campo-hondo): fondo de página en degradado vertical; el hondo también es pista de la barra de desplazamiento y fondo de bandejas y semáforo.
- **Placa** (placa) a **Placa Baja** (placa-baja): degradado vertical de cada panel.
- **Control Alto / Control Bajo** (control-alto, control-bajo): degradado de selects y buscador, un escalón más claro que la placa para que se lean como piezas que se tocan.
- **Línea** y **Línea Fuerte** (linea, linea-fuerte): filetes azul hielo translúcidos; la fuerte bordea controles, tubo y semáforo.
- **Blanco Titular** (blanco-titular): marca, títulos de sección, nombre del vuelo.
- **Texto** (texto): texto corrido.
- **Suave** (suave): ayudas, detalles, etiquetas de lectura.
- **Tenue** (tenue): escala del medidor, anillos del radar, placeholder, pie.

### Paradas por componente y estado
Colores que solo viven dentro de un componente, casi siempre como par de degradado (alto arriba o a la izquierda, bajo abajo o a la derecha). No son paleta libre: cada uno pertenece a su pieza y a su estado.
- **Barra superior** (barra-alta a barra-baja): degradado vertical de la barra.
- **Cabecera de tabla** (cabecera-alta a cabecera-baja): degradado de la cabecera pegajosa.
- **Aviso flotante** (aviso-alto a aviso-bajo): degradado del aviso, con borde cian.
- **Carcasa del semáforo** (carcasa-alta a carcasa-baja): hueco donde se hunden las lámparas.
- **Icono de vuelo** (a 160°): skill de icono-skill-alto a icono-skill-bajo; agente de icono-agente-alto a icono-agente-bajo; comando de icono-comando-alto a icono-comando-bajo; vacío de icono-vacio-alto a icono-vacio-bajo.
- **Relleno del medidor** (vertical, brillo 0 %, color de señal 45 %, fondo 100 %): sano con tubo-verde-brillo y tubo-verde-fondo; alerta con tubo-ambar-brillo y tubo-ambar-fondo; crítico con tubo-rojo-brillo y tubo-rojo-fondo.
- **Lámparas apagadas** (lampara-verde-apagada, lampara-ambar-apagada, lampara-roja-apagada): el color muerto de cada luz; el verde apagado también es el fondo del video de "Pantalla encendida" mientras carga.
- **Sombra de lámpara** (sombra-lampara): sombra interior inferior de la lámpara apagada.
- **Tinta En vuelo** (tinta-envuelo): texto y punto de la pastilla "En vuelo" sobre cian.
- **Texto de error** (texto-error): texto del panel de error sobre velo rojo.
- **Borde del barrido** (borde-barrido): línea brillante que encabeza el barrido del radar.

### Named Rules
**La Regla del Código de Vuelo.** Cian es skill, ámbar es agente o pedir, verde es comando o autorizado, rojo es apagada o crítico. Ningún color de señal se usa como adorno ni cambia de significado entre zonas.

**La Regla del Campo Propio.** Todo neutro es azul. Fondo, bandejas, cabeceras de tabla, barra de desplazamiento y hasta la tinta del contorno de las etiquetas del radar (#041030) salen del azul NEXUS; el gris no existe en este mundo.

## Typography

**Display Font:** Saira Semi Condensed 600/700/800 (OFL, alojada en `fuentes/` y servida por panel.py), con respaldo "Segoe UI Variable Display", "Segoe UI", system-ui
**Body Font:** "Segoe UI Variable Text" (con "Segoe UI", system-ui, -apple-system, "Helvetica Neue", sans-serif)

**Character:** Una semicondensada de corte técnico como voz de instrumento (marca, títulos, el vuelo actual y todas las cifras grandes) sobre una sans humanista del sistema, legible de reojo a 15–18 px. Cifras tabulares en toda la página para que los números no bailen al refrescar cada 5 s.

**Fuente display.** Saira Semi Condensed 600/700/800 (OFL) se sirve desde `/fuentes/saira-{600,700,800}.woff2` del propio panel.py (no CDN), con `font-display: swap`, así la CSP sigue siendo `'self'`. Si no carga, cae a "Segoe UI Variable Display", "Segoe UI", system-ui.

### Hierarchy
- **Marca** (800, 26 px, interlineado 1, tracking 0.12em, mayúsculas; 22 px en celular): solo el logotipo "SKILL TOWER".
- **Display** (800, clamp(30px, 3vw, 40px), 1): la cifra del contexto usado.
- **Divisor** (600, 17 px, display): el "/ 1.000.000 · 31 %" junto a la cifra, en suave.
- **Headline** (700, clamp(24px, 2.4vw, 32px), 1.15): el nombre de lo que está "En el aire".
- **Title** (700, 21 px, 1.2): títulos de panel, siempre con icono de trazo en cian a la izquierda.
- **Lectura** (700, 22 px, 1.2): valores de la fila de lecturas.
- **Body** (400, 18 px, 1.5): texto corrido y celdas.
- **Body celular** (400, 17 px, 1.5): la base en ≤820 px.
- **Detalle** (400, 16 px): controles de la barra, detalle del vuelo, rótulo del medidor.
- **Body ayuda** (400, 15 px, 1.5, máx. 70ch): ayudas bajo títulos, nota del medidor, reglas, descripciones (62ch), pie.
- **Label** (700, 14 px): cabeceras de tabla en cian, pastillas de estado, etiquetas de lectura y leyenda (400).
- **Escala** (400, 13 px): escala del medidor, texto del modo bajo el semáforo, etiqueta de cada número en las fichas; las etiquetas del hangar usan el mismo tamaño a 700.

### Named Rules
**La Regla del Número Quieto.** Toda la página usa `font-variant-numeric: tabular-nums`; una cifra que se refresca no puede cambiar de ancho.

**La Regla de Letra Grande.** El texto que se lee va a 15 px o más; 13–14 px queda para escalas, pastillas y cabeceras.

## Layout

Columna centrada de hasta 1440 px con márgenes laterales fluidos (margen-pagina) y 72 px al final. La primera vista es una rejilla de dos columnas (1.05fr / 1fr, hueco de 22 px): el radar a la izquierda (cuadrado, máx. 500 px) y "En el aire" a la derecha, con el vuelo actual, el medidor y la fila de lecturas apilados con 22 px. Debajo, una sola columna con el tablero de despegues (alto máx. 330 px con desplazamiento) y el hangar (máx. 70vh).

La barra superior es pegajosa en escritorio y se envuelve con huecos 12/28 px. La fila de lecturas es un flujo flexible (base 150 px) separado por filetes, no una rejilla de tarjetas.

Responsivo:
- ≤1180 px: el hangar oculta Origen y Máximo y recorta la descripción a 2 líneas.
- ≤980 px: la primera vista pasa a una columna; radar máx. 420 px.
- ≤820 px: base 17 px; la barra deja de ser pegajosa; "En el aire" sube antes que el radar (lo activo va primero); las etiquetas del radar crecen (15/17 px); cada fila de tabla se convierte en ficha en rejilla, sin desplazamiento horizontal, con la etiqueta de cada número encima.

## Elevation & Depth

Sistema en capas con material 3D. Cada placa lleva un bisel (luz de 1 px arriba, sombra de 1 px abajo) más una sombra blanda que cae hacia abajo; los huecos (tubo del medidor, semáforo) se hunden con sombra interior; las fuentes de luz (lámparas encendidas, blips, luz "En vivo", relleno del medidor, icono de vuelo) brillan con halo de su propio color. El radar es la pieza de más profundidad: aro biselado, pantalla con degradado radial y cúpula de vidrio encima.

### Shadow Vocabulary
- **Bisel** (`box-shadow: inset 0 1px 0 rgba(255,255,255,0.10), inset 0 -1px 0 rgba(0,0,0,0.35)`): toda placa y control.
- **Sombra de placa** (`box-shadow: 0 18px 40px -18px rgba(0,0,0,0.85), 0 3px 8px rgba(0,0,0,0.35)`): placas y aviso flotante.
- **Hundido** (`box-shadow: inset 0 3px 8px rgba(0,0,0,0.7)`): tubo del medidor; el semáforo usa `inset 0 2px 6px rgba(0,0,0,0.7)`.
- **Halo de luz** (`box-shadow: 0 0 14px <color>, 0 0 3px <color>`): lámpara encendida; blips con desenfoque SVG equivalente.
- **Halo del icono** (`0 8px 18px -6px <color de señal a 0.5–0.55>` + brillo interior blanco 0.35): icono de vuelo.

### Named Rules
**La Regla del Vidrio Reservado.** El reflejo especular (radial blanco arriba a la izquierda) es de los instrumentos: radar, lámparas, relleno del medidor e icono de vuelo. Las placas, tablas y controles solo llevan bisel.

**La Regla de la Luz Propia.** Solo lo que representa una señal viva brilla con halo de color. Un título, un borde o un texto nunca emiten luz.

## Shapes

Rectángulos de esquinas suaves anidados que se van cerrando hacia dentro: placa 18 px, icono de vuelo 16 px, bandeja de tabla, error y aviso 14 px, controles 12 px; el anillo de foco global se curva a 8 px y el del botón de orden de tabla a 6 px. Todo lo que es estado o luz es redondo: pastillas de 99 px (estados, etiquetas, tubo, semáforo, botón "Pantalla encendida") y círculos (lámparas, blips, luz "En vivo", luz de video). El radar es el único círculo grande; sus anillos y ejes son filetes cian translúcidos. Iconos de trazo de 2 px con remates redondos, dibujados en SVG.

## Components

### Placa
Instrumento empotrado: degradado vertical placa a placa-baja, filete fino, radio de placa, bisel más sombra de placa. Título con icono cian y una línea de ayuda debajo.

### Campos (select y buscador)
- **Estilo:** degradado control-alto a control-bajo, borde línea fuerte, radio 12 px, bisel.
- **Hover:** el borde pasa a cian a 0.55.
- **Foco:** anillo cian de 3 px separado 3 px (global para todo control).
- **Casillas:** color de acento nativo, verde para "En vivo", cian para filtros.

### Pastillas de estado y etiquetas
- **En vuelo:** cian sólido con texto azul hondo y punto que late 3 veces (1.2 s).
- **Aterrizó:** suave sobre suave a 0.14.
- **Etiquetas del hangar** (usada / agresiva / terceros): 13 px, 700, fondo del color de señal a 0.14–0.16 y texto del mismo color.

### Tablas (despegues y hangar)
- **Bandeja:** radio 14 px, filete, fondo campo-hondo a 0.45.
- **Cabecera:** pegajosa, degradado cabecera-alta a cabecera-baja, texto label en cian.
- **Botón de orden:** la cabecera entera es un botón sin estilo propio; la columna ordenada muestra un chevrón de 12 px dibujado con máscara SVG en el color del texto (nunca un glifo), que gira 180° en orden ascendente. Foco con anillo cian de 3 px y radio 6 px.
- **Filas:** celdas 11/14 px con filete inferior; hover con velo cian a 0.05; la fila ya usada en la sesión lleva un tinte de fondo cian a 0.06 (rgba(46, 230, 255, 0.06)), sin franja lateral.
- **Celular:** cada fila es una ficha en rejilla.

### Navegación (barra superior)
Barra pegajosa (estática en celular) con degradado barra-alta a barra-baja, filete inferior y línea interior cian a 0.25. Marca: torre en SVG con halo cian, logotipo en Saira y lema en verde. A la derecha, en tipo detalle: sesión, interruptor "En vivo" con luz verde (tenue en pausa), botón "Pantalla encendida" y hora de actualización en región viva.

### Botón "Pantalla encendida"
Pastilla con el mismo degradado y bisel que los campos (control-alto a control-bajo, borde línea fuerte; hover con borde cian a 0.55). Su luz es un `<video>` circular de 20 px, mudo y en bucle (media/despierto.mp4: un pulso verde de #17784f a #3ef0a1), con fondo lampara-verde-apagada mientras carga. Estado en `aria-pressed`: encendida, la luz se ve a color; apagada, pasa a escala de grises y brillo 0.5.

### Medidor de contexto
Tubo hundido de 26 px en pastilla con marcas cada 25 %. El relleno es una barra de vidrio verde (ámbar en alerta, rojo en crítico) con brillo interior y halo; crece en 0.8 s con `cubic-bezier(0.16, 1, 0.3, 1)`. Encima, la cifra display; debajo, la escala en tenue y una nota en lenguaje llano.

### Semáforo (firma del hangar)
Grupo de radio con tres lámparas de vidrio de 22 px en una carcasa hundida en pastilla. Apagadas, cada lámpara muestra su color muerto (verde #14412f, ámbar #47380f, rojo #4a1d1d) con reflejo tenue; la elegida se enciende con reflejo blanco fuerte y halo de su color. Hover aclara 1.35; foco con anillo cian. Una versión mini de 14 px sirve de leyenda y en el tablero.

### Radar (firma de la torre)
SVG de 400×400: aro biselado, pantalla en degradado radial, tres anillos de tiempo (3 min, 15 min, 1 hora o más), barrido cian con estela de diez cuñas que gira cada 4 s y cúpula de vidrio encima. Cada blip (cian, ámbar o verde; el más reciente más grande) se enciende cuando el barrido pasa por su ángulo; un uso nuevo emite una onda de 1.4 s. Etiquetas con contorno azul hondo para que se lean sobre la pantalla.

### Icono de vuelo
Baldosa de 58 px, radio 16 px, con degradado del color de señal (cian, ámbar o verde), reflejo especular y halo del mismo color; vacía, es azul apagado con bisel.

## Do's and Don'ts

### Do:
- **Do** usar el campo azul NEXUS (campo a campo-hondo) como fondo de toda superficie nueva, con los dos resplandores suaves cian y verde.
- **Do** asignar color solo por significado: cian skill, ámbar agente/pedir, verde comando/auto/ok, rojo apagada/crítico.
- **Do** montar cada bloque sobre una placa con bisel y sombra de placa, radio 18 px.
- **Do** dar el vidrio especular y el halo solo a instrumentos y señales vivas (radar, lámparas, medidor, icono de vuelo, luz "En vivo").
- **Do** mantener la base en 18 px (17 px en celular), números tabulares y anillo de foco cian de 3 px.
- **Do** separar lecturas con filetes finos dentro de una placa.
- **Do** apagar barrido, pulsos y transiciones con `prefers-reduced-motion`.

### Don't:
- **Don't** usar grises neutros; todo neutro sale del azul NEXUS.
- **Don't** hacer el material plano: el autor pide brillo y relieve.
- **Don't** meter cada lectura en su propia tarjeta ni armar una rejilla de tarjetas de métricas iguales.
- **Don't** poner halo o resplandor en títulos, bordes o texto.
- **Don't** usar un color de señal como decoración o con otro significado.
- **Don't** cargar la fuente display desde un CDN: Saira Semi Condensed se sirve desde el propio panel.py para no abrir la CSP.
