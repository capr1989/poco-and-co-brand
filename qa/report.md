# Control de calidad — revisión 01

Fecha: 2 de noviembre de 2026. Este informe distingue verificaciones mecánicas, inspección visual y limitaciones.

## Alcance

Tres rutas de identidad con firmas principales, horizontales, compactas, monocromáticas, claras y oscuras, inicial para favicon, guías, tokens y siete aplicaciones por ruta. Se producen SVG de curvas reales y PNG; los estudios con texto vivo están identificados por separado.

## Verificaciones mecánicas

Los resultados y dimensiones exactas se conservan en [validation.json](validation.json), generado por `tools/document_and_check.py`.

- Parseo XML de todos los SVG del proyecto; viewBox presente, sin imágenes rasterizadas incrustadas ni referencias externas de imagen.
- Identificadores SVG únicos dentro de cada archivo, incluso en logos anidados en las aplicaciones.
- Decodificación de los PNG exportados y registro de sus dimensiones.
- Existencia de las variantes y las siete aplicaciones por ruta.
- Comprobación de enlaces estáticos locales de la presentación y presencia de licencias de fuentes.
- Cálculo de contraste sRGB de tinta/papel y combinaciones de apoyo. Usar tinta sobre papel y sobre secundario para texto funcional.

El inventario actual incluye **59 SVG en concepts y 71 PNG**, más la lámina comparativa fuera de esa carpeta. Las tres parejas tinta/papel superan 10:1; el ajuste del oliva B y del óxido C elevó las combinaciones funcionales comprobadas por encima de 4.5:1. Los valores exactos están en el JSON.

Refinamiento A: el favicon pasa de cobalto a azul tinta #192C46, manteniendo la geometría original. Se entregan variantes tinta/blanco y niebla/tinta a 16, 32, 48 y 512 px. Ver `concepts/concept-a/favicon-refinement.md` y `favicon-a-refinement.png` para comparación de reducción. Contraste blanco/tinta: 14.09:1; tinta/niebla: 12.73:1.

Estas comprobaciones no prueban por sí solas calidad estética o registrabilidad. La existencia de un enlace externo tampoco garantiza que siga accesible.

## Inspección visual

Se revisan las hojas [variantes](logo-variants.png), [tamaños pequeños](small-sizes.png) y aplicaciones [A](applications-a.png), [B](applications-b.png), [C](applications-c.png), junto a vistas grandes de tienda y empaque.

La revisión busca recortes, proporciones, lectura del nombre, separación de elementos, fondos y coherencia de las tres rutas. Los mínimos se aumentaron en A y B para proteger & Co. La inicial P se reserva para 16/32/48 px; no se fuerza el nombre completo a ese tamaño.

La caja de empaque es una simulación en perspectiva. La transformación del logo en ese mockup representa el plano de la caja y no cambia el archivo maestro.

## Presentación local

Comprobar en navegador: las tres rutas lado a lado en escritorio; selección de propuesta; versiones de logo; claro/oscuro; ampliación y cierre con Escape; siete aplicaciones; enlaces de SVG/PNG; grilla móvil; matriz y sección de investigación. Las fuentes y gráficos se cargan de carpetas locales, sin CDN. La presentación puede abrirse con `file://` sin servidor porque usa scripts clásicos y no solicitudes fetch.

Se verificó en Chrome mediante HTTP local en 127.0.0.1: navegación de propuesta, B compacta en oscuro con su descarga correspondiente, ampliación, cierre por Escape y cambio a aplicación móvil C. La revisión responsive a 390 × 844 no mostró elementos fuera del ancho disponible; la tabla comparativa tiene desplazamiento contenido. No se encontraron imágenes cargadas rotas en la vista inspeccionada. Se revisaron también la grilla y las variantes en PNG.

La automatización del navegador no permite navegar a protocolos `file://`; por ello **no se verificó automáticamente la apertura directa con doble clic**. El HTML usa scripts clásicos y rutas relativas, sin fetch ni CDN, para permitir esa apertura en un navegador local normal. Se proporciona también la alternativa de servidor loopback en el README, sin publicación.

Los enlaces a Markdown se abren como archivos de texto o se descargan según el navegador. Las paletas también se ven directamente en la presentación. La copia de HEX usa el portapapeles cuando está permitido y ofrece un mensaje con el código cuando el navegador restringe esa función.

## Limitaciones que permanecen

- Nombre provisional, con antecedentes relevantes. Ninguna revisión legal ni certificado de registro.
- Referencias de redes sociales limitadas por acceso público; no se afirmó disponibilidad de usuarios.
- WHOIS .pa no encontró registros, pero no se completó un flujo de contratación para probar disponibilidad comercial.
- Ilustraciones vectoriales de productos y precios ficticios; no son fotografía, catálogo aprobado, especificación técnica o disponibilidad de inventario.
- Aplicaciones de Shopify como visualización; no se implementó Shopify, carrito ni checkout.
- No hay prueba de impresión, CMYK/Pantone, troquel, perfil ICC, sangrado ni pruebas con usuarios. Los HEX son especificaciones sRGB; ajustar producción física con el proveedor cuando exista autorización.
- Las puntuaciones son juicio de diseño orientativo. La elección corresponde a los fundadores.
- Las fuentes originales requieren instalación para editar el estudio de texto vivo; los SVG finales de curvas no la requieren.

No se publicó ninguna página. El servidor usado para comprobar la presentación escucha solo en 127.0.0.1.
