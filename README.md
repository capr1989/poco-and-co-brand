# Poco & Co. — Identidad de marca

Proyecto de branding e identidad visual para una tienda online multidepartamento, inicialmente orientada a Panamá.

**Estado:** tres propuestas visuales construidas para revisión de los fundadores. El nombre sigue siendo provisional y requiere revisión por los antecedentes encontrados. No hay identidad seleccionada ni aprobación jurídica.

## Abrir la presentación

Hacer doble clic en **`ABRIR-PRESENTACION.html`** o abrir **`presentation/index.html`** en Chrome o Edge. Funciona desde la carpeta local, sin instalar dependencias, sin conexión para ver los diseños y sin una suscripción de diseño. Mantener juntas las carpetas; el HTML usa recursos relativos.

La presentación permite comparar las tres propuestas, ampliar logos y aplicaciones, alternar fondos, consultar colores y fuentes, y descargar SVG/PNG. En móvil las rutas se apilan; en escritorio se ven lado a lado. Los informes Markdown se abren como texto o se descargan según el navegador.

La comprobación automatizada se hizo por HTTP local. Si el navegador restringe archivos locales, se puede servir la carpeta solo en el equipo con `python -m http.server 4173 --bind 127.0.0.1` y abrir `http://127.0.0.1:4173/presentation/index.html`; cerrar el proceso al terminar. Esto no publica la presentación en Internet.

| Propuesta | Dirección | Idea |
|---|---|---|
| A · En buena compañía | Geométrica y contemporánea | Lettering propio con dos oes del mismo módulo |
| B · Cada día, un poco | Cálida y editorial | Fraunces con una firma secundaria espaciada |
| C · Un mundo en Poco | Compacta y comercial | Nombre en dos líneas con un mismo ancho |

Vista general: [propuestas](comparison/proposals.png). Hay 57 SVG de conceptos, diagramas y estudios tipográficos, y 63 PNG exportados. Además se incluyen la lámina comparativa, fuentes y licencias, guías, tokens, investigación y evidencia de QA.

## Documentación

- [Brief original completo](brief/BRIEF-ORIGINAL.md)
- [Plan y entregables](PLAN.md)
- [Registro de decisiones](DECISIONS.md)
- [Investigación del nombre](research/brand-availability.md)
- [Matriz y justificaciones](comparison/evaluation.md)
- [Control de calidad y límites](qa/report.md)

## Organización

- `brief/`: requisitos originales del proyecto.
- `research/`: disponibilidad preliminar del nombre, referencias y fuentes fechadas.
- `concepts/concept-a/`, `concept-b/`, `concept-c/`: tres rutas distintas, SVG editables, guías, aplicaciones y PNG en `exports/`.
- `presentation/`: presentación local HTML/CSS/JavaScript.
- `design-tokens/`: paletas, tipografía y medidas por concepto.
- `comparison/`: matriz de evaluación ponderada.
- `qa/`: verificaciones y limitaciones documentadas.
- `assets/`: fuentes con sus licencias y referencias con atribución.

## Cómo trabajar

GitHub sirve para conservar documentos y archivos de diseño, aunque no sea un proyecto de software. Guardar cambios localmente no los sube automáticamente: hay que crear un commit y sincronizarlo con el repositorio remoto.

Mantener los originales editables junto a sus exportaciones. Usar nombres descriptivos y registrar decisiones de los fundadores. No incluir contraseñas, credenciales ni archivos privados ajenos al proyecto. GitHub no sustituye una copia de seguridad independiente.

Los SVG finales tienen contornos editables y no necesitan fuentes instaladas para verse. Los archivos `typography-editable.svg` conservan texto vivo y sí requieren las fuentes incluidas. Las aplicaciones comerciales son simulaciones vectoriales con productos y precios ilustrativos, no una implementación de Shopify.

## Volver a generar los archivos

Esto es opcional; no hace falta para revisar el trabajo. Requiere Python, Node.js y dependencias gratuitas. Desde la raíz del proyecto:

```powershell
python -m venv work/venv
./work/venv/Scripts/python.exe -m pip install -r tools/requirements.txt
npm install --prefix work @resvg/resvg-js@2.6.2
./work/venv/Scripts/python.exe tools/build_brand.py
node tools/export_png.cjs
./work/venv/Scripts/python.exe tools/document_and_check.py
```

`work/` se excluye de Git. Los archivos de fuente originales y sus licencias ya están en `assets/fonts/`. Para ediciones visuales directas se puede abrir cualquier SVG en un editor vectorial compatible. No es necesario ejecutar los generadores.

## Hallazgos del nombre

El dominio .com está registrado según RDAP. DIGERPI mostró POCO de Xiaomi como “Vigente”, con clases que incluyen 9 y 35. WHOIS de NIC Panamá no encontró registros para los dos dominios .pa consultados; no se completó un flujo de contratación. Redes sociales y otros usos están documentados con sus límites. **Ninguna de estas propuestas aprueba el nombre para lanzamiento.**

## Límites

No implementar Shopify ni publicar páginas, comprar dominios, registrar marcas, abrir cuentas comerciales, contactar terceros o contratar servicios. Usar herramientas gratuitas y locales. La revisión del nombre será preliminar y no equivale a aprobación legal.

El brief original es la referencia completa para el trabajo de diseño posterior.
