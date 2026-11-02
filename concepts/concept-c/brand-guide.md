# C — Un mundo en Poco

**Ruta:** Compacta · directa · comercial. **Estado:** propuesta para revisión; nombre provisional.

## Concepto

Dos líneas con un mismo ancho convierten el nombre completo en una firma compacta. La palabra compañía tiene presencia real: & CO. sostiene el bloque, en vez de ser una nota al margen.

**Ventaja:** Alta presencia en etiquetas, publicaciones y señalización con una firma fácil de reproducir a una tinta.

**Límite:** La masa tipográfica es más enérgica; necesita márgenes amplios y moderación en promociones para no sugerir descuento permanente.

## Construcción y archivos

Composición de Archivo Black. En la firma principal las dos líneas se ajustan horizontalmente al mismo ancho, como parte del diseño original; no reescalar las líneas por separado al reproducir el archivo final.

- `logo-primary.svg`: firma principal con fondo transparente.
- `logo-horizontal.svg`: composición para cabeceras; en A coincide con la principal porque ya es horizontal.
- `logo-compact.svg`: abreviación tipográfica para soportes pequeños. No es un símbolo independiente ni reemplaza siempre al nombre completo.
- `logo-monochrome.svg`: firma en negro, sin fondo.
- `logo-light.svg` y `logo-dark.svg`: tintas para fondos claros y oscuros; fondo transparente, debe elegirse el fondo correspondiente.
- `logo-horizontal-dark.svg`, `logo-compact-dark.svg`, `logo-monochrome-dark.svg`: inversiones exportables, también transparentes.
- `favicon.svg`: inicial P sobre campo de marca, desde 16 px. No se intenta comprimir el nombre entero en un favicon.
- `logo-clear-space.svg`: diagrama de área libre, **el marco no forma parte del logo**.
- `typography-editable.svg`: estudio con texto vivo. Requiere instalar las fuentes incluidas; no es el arte final del logotipo. El lettering A se edita como curvas en los archivos finales.
- `exports/`: PNG con contornos idénticos a los SVG, logos a 3000 px de ancho; favicon a 512, 48, 32 y 16 px; aplicaciones a 2160 px, salvo móvil a 1170 px.

Los SVG finales contienen formas vectoriales y trazados de tipografía; no imágenes rasterizadas ni dependencias de fuentes para reproducirse. En un editor SVG pueden modificarse color, geometría y composición. Para cambiar palabras y volver a generar contornos, editar `tools/build_brand.py`.

## Paleta

| Función | HEX |
|---|---|
| Tinta / fondo oscuro | `#153E35` |
| Papel / fondo claro | `#F1F0E7` |
| Acento de acción | `#BA4429` |
| Secundario de superficie | `#CFDC96` |
| Blanco de apoyo | `#FFFFFF` |

Par de identidad recomendado: tinta sobre papel o papel sobre tinta. Contraste sRGB calculado: **10.36:1**. El color secundario funciona como superficie, no como texto pequeño sobre blanco. Usar tinta para texto informativo; revisar contraste cuando se creen combinaciones nuevas. Los logos no se evalúan como texto de interfaz, pero se privilegia su legibilidad.

## Tipografía

**Marca / titulares:** Archivo Black · composición de bloque.

**Interfaz y textos:** Manrope 500 regular, 750 para énfasis y acciones. Titulares orientativos 32–76 px en escritorio, 28–38 px en móvil; cuerpo 16–18 px, interlineado 1.5. La presentación editorial usa tamaños propios por su función de catálogo de diseño.

En C, Archivo Black se reserva para titulares cortos y marca; no usarla en párrafos ni todo el catálogo.

Las familias originales y sus licencias SIL Open Font License están en `assets/fonts/`. No se adquirieron licencias ni se atribuye autoría del alfabeto al proyecto. Los archivos de fuente originales no se modificaron; se instanciaron sus ejes en memoria para dibujar contornos.

## Proporciones, espaciado y mínimos

- Grilla de interfaz: 8 px; espacios de 8, 16, 24, 32 y 48 px.
- Área libre: ¼ de la altura completa del bloque en todo el perímetro visible. Los márgenes del archivo pueden no completar esa reserva: añadir espacio al colocarlo. El diagrama es una referencia de aplicación.
- Mantener la relación de aspecto del archivo final y la separación de sus elementos. No reescribir el logo usando una fuente parecida.
- Ancho mínimo digital orientativo: principal **96 px**, horizontal **150 px**, compacta **64 px**. Por debajo, usar la inicial P del favicon.
- Favicon: 16 / 32 / 48 px; para perfiles grandes usar el nombre completo, para recortes menores de 48 px preferir P.
- Impresión: horizontal desde 32 mm de ancho; firma principal desde 24 mm. Son recomendaciones iniciales: realizar prueba física según papel, tinta y proceso.
- No añadir un eslogan al archivo del logotipo. Los lemas de las aplicaciones son contenido demostrativo, no marcas investigadas.

## Usos correctos

1. Firma íntegra sobre una superficie limpia y con contraste.
2. Variante clara u oscura según el fondo. Una tinta en empaque sencillo.
3. Inicial P para favicon o reducción extrema; nombre completo en primeras impresiones.
4. Colocar productos de distintas categorías dentro del mismo sistema de grilla y jerarquía.

## Usos incorrectos

1. Estirar, comprimir o rotar la firma; alterar solo una línea del bloque C después de su composición final.
2. Usar el secundario como tinta pequeña sobre papel sin comprobar contraste.
3. Poner la firma sobre una fotografía ocupada sin una zona despejada.
4. Añadir sombras, degradados, corazones, carritos, destellos o contornos decorativos al logo.
5. Reducir la firma completa hasta que & Co. deje de leerse.
6. Presentar esta propuesta como una marca legalmente aprobada.

## Aplicaciones

En `applications/`: cabecera conceptual Shopify en escritorio y móvil; pestaña con favicon; perfil Instagram; publicación 1080 × 1350; tarjeta de soporte para automóvil; caja kraft con etiqueta.

Las aplicaciones muestran tecnología, hogar y automóvil. Productos, precios, lemas y contenidos son ilustrativos. Son simulaciones vectoriales originales, sin tienda, pedidos o inventario implementados. La caja es una visualización de uso, no un troquel listo para imprenta. Su perspectiva es un mockup: no copiar esa deformación como archivo maestro.

## Revisión

Ver `qa/report.md` y `comparison/evaluation.md`. La preferencia visual corresponde a los fundadores. La evaluación del nombre tiene límites separados en `research/brand-availability.md`.
