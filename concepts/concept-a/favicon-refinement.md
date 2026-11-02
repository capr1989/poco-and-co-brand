# Refinamiento del favicon A

La propuesta A fue indicada como favorita por los fundadores. Este ajuste afecta al favicon y su demostración en el navegador.

- Antes: fondo cobalto `#2855D9`.
- Ahora: fondo azul tinta **`#192C46`**, idéntico al fondo oscuro del sistema de marca y del perfil social A.
- Se conserva la p geométrica blanca `#FFFFFF`, su curva, posición, escala y el contenedor redondeado original.
- El cobalto sigue siendo un acento de la paleta; deja de usarse como fondo del favicon.

## Archivos

- `favicon.svg`: versión recomendada, fondo azul tinta y p blanca; funciona en pestañas claras y oscuras.
- `favicon-dark.svg`: la misma versión con nombre explícito.
- `favicon-light.svg`: variante invertida, fondo niebla `#F1F4F2` y p azul tinta `#192C46`, para composiciones con superficie clara. Si se usa sobre una interfaz muy clara, preferir la versión azul para definir mejor el contenedor.
- `exports/favicon*.png`: cada versión en **16, 32, 48 y 512 px**.

El logotipo principal tiene fondo transparente; el azul tinta es tanto su tinta en la versión clara como el fondo de su aplicación oscura. Por eso se toma ese color como referencia, en lugar de introducir otro azul.

## Comprobación

SVG válidos, sin imágenes incrustadas; PNG decodificados en los cuatro tamaños. La geometría de la versión recomendada se conserva exactamente: solo cambia el color del fondo. Se inspeccionó la reducción a 16, 32 y 48 px; la contraforma de la p sigue abierta y el asta mantiene su lectura.

Contraste sRGB p blanca / fondo tinta: **14.09:1** aproximadamente. Variante clara tinta / niebla: **12.73:1**. El cambio aumenta el contraste respecto del favicon cobalto anterior.

Este refinamiento no implica aprobación legal del nombre. La selección de A como favorita no modifica las otras propuestas.
