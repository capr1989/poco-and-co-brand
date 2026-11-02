# B — Cada día, un poco

**Ruta:** Editorial · cálida · sofisticada. **Estado:** propuesta para revisión; nombre provisional.

## Concepto

Una serif de curvas generosas y un ampersand explícito hablan de compañía sin recurrir a corazones. La composición editorial convierte la selección de objetos cotidianos en un gesto de cuidado.

**Ventaja:** Transmite cercanía y atención al detalle en empaque, hogar y comunicación de producto.

**Límite:** La serif demanda más tamaño en interfaces pequeñas; sin variedad de categorías podría percibirse como una tienda de hogar.

## Construcción y archivos

Composición de Fraunces 600, óptica 72, SOFT 40 y WONK 1 para Poco; Manrope 500 con espaciado para & CO. La horizontal usa Fraunces también en & Co.

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
| Tinta / fondo oscuro | `#532C30` |
| Papel / fondo claro | `#F5EDDF` |
| Acento de acción | `#94543C` |
| Secundario de superficie | `#ADB18A` |
| Blanco de apoyo | `#FFFDF8` |

Par de identidad recomendado: tinta sobre papel o papel sobre tinta. Contraste sRGB calculado: **10.20:1**. El color secundario funciona como superficie, no como texto pequeño sobre blanco. Usar tinta para texto informativo; revisar contraste cuando se creen combinaciones nuevas. Los logos no se evalúan como texto de interfaz, pero se privilegia su legibilidad.

## Tipografía

**Marca / titulares:** Fraunces 600 · óptica 72 · suavidad 40.

**Interfaz y textos:** Manrope 500 regular, 750 para énfasis y acciones. Titulares orientativos 32–76 px en escritorio, 28–38 px en móvil; cuerpo 16–18 px, interlineado 1.5. La presentación editorial usa tamaños propios por su función de catálogo de diseño.

En B, Fraunces se reserva para titulares y marca; Manrope sostiene navegación, categorías, precios y texto funcional.

Las familias originales y sus licencias SIL Open Font License están en `assets/fonts/`. No se adquirieron licencias ni se atribuye autoría del alfabeto al proyecto. Los archivos de fuente originales no se modificaron; se instanciaron sus ejes en memoria para dibujar contornos.

## Proporciones, espaciado y mínimos

- Grilla de interfaz: 8 px; espacios de 8, 16, 24, 32 y 48 px.
- Área libre: ½ de la altura de la o de Poco en todo el perímetro visible. Los márgenes del archivo pueden no completar esa reserva: añadir espacio al colocarlo. El diagrama es una referencia de aplicación.
- Mantener la relación de aspecto del archivo final y la separación de sus elementos. No reescribir el logo usando una fuente parecida.
- Ancho mínimo digital orientativo: principal **180 px**, horizontal **164 px**, compacta **112 px**. Por debajo, usar la inicial P del favicon.
- Favicon: 16 / 32 / 48 px; para perfiles grandes usar el nombre completo, para recortes menores de 48 px preferir P.
- Impresión: horizontal desde 36 mm de ancho; firma principal desde 36 mm. Son recomendaciones iniciales: realizar prueba física según papel, tinta y proceso.
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
