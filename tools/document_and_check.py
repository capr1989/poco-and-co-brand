"""Generate guides and mechanical QA evidence; contact sheets must also be inspected visually."""
from pathlib import Path
import csv, json, re, sys, xml.etree.ElementTree as ET
from html.parser import HTMLParser
from PIL import Image, ImageDraw, ImageOps, ImageFont
from build_brand import DATA, ROOT, write

def luminance(h):
    channels=[int(h[n:n+2],16)/255 for n in [1,3,5]]
    channels=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in channels]
    return sum(v*w for v,w in zip(channels,[.2126,.7152,.0722]))

def contrast(a,b):
    l1,l2=sorted([luminance(a),luminance(b)]);return (l2+.05)/(l1+.05)

def documentation():
    for d in DATA:
        k=d['id']; token=json.loads((ROOT/f'design-tokens/concept-{k}.json').read_text())
        palette=['Tinta / fondo oscuro','Papel / fondo claro','Acento de acción','Secundario de superficie']
        colortable='\n'.join(f'| {label} | `{d[key]}` |' for label,key in zip(palette,['ink','paper','accent','secondary']))
        guide=f'''# {k.upper()} — {d['name']}

**Ruta:** {d['route']}. **Estado:** propuesta para revisión; nombre provisional.

## Concepto

{d['idea']}

**Ventaja:** {d['strength']}

**Límite:** {d['limit']}

## Construcción y archivos

{'Lettering original construido en curvas Bézier, con módulo compartido para las oes, apertura propia de la c y asta de la p. & co. usa Manrope 750.' if k=='a' else 'Composición de Fraunces 600, óptica 72, SOFT 40 y WONK 1 para Poco; Manrope 500 con espaciado para & CO. La horizontal usa Fraunces también en & Co.' if k=='b' else 'Composición de Archivo Black. En la firma principal las dos líneas se ajustan horizontalmente al mismo ancho, como parte del diseño original; no reescalar las líneas por separado al reproducir el archivo final.'}

- `logo-primary.svg`: firma principal con fondo transparente.
- `logo-horizontal.svg`: composición para cabeceras; en A coincide con la principal porque ya es horizontal.
- `logo-compact.svg`: abreviación tipográfica para soportes pequeños. No es un símbolo independiente ni reemplaza siempre al nombre completo.
- `logo-monochrome.svg`: firma en negro, sin fondo.
- `logo-light.svg` y `logo-dark.svg`: tintas para fondos claros y oscuros; fondo transparente, debe elegirse el fondo correspondiente.
- `logo-horizontal-dark.svg`, `logo-compact-dark.svg`, `logo-monochrome-dark.svg`: inversiones exportables, también transparentes.
- `favicon.svg`: inicial P sobre campo de marca, desde 16 px. No se intenta comprimir el nombre entero en un favicon.
{('- En A, el favicon usa fondo azul tinta #192C46 y p blanca; `favicon-dark.svg` es la misma firma y `favicon-light.svg` invierte a niebla con p tinta. Ver `favicon-refinement.md`.'+chr(10) if k=='a' else '')}- `logo-clear-space.svg`: diagrama de área libre, **el marco no forma parte del logo**.
- `typography-editable.svg`: estudio con texto vivo. Requiere instalar las fuentes incluidas; no es el arte final del logotipo. El lettering A se edita como curvas en los archivos finales.
- `exports/`: PNG con contornos idénticos a los SVG, logos a 3000 px de ancho; favicon a 512, 48, 32 y 16 px; aplicaciones a 2160 px, salvo móvil a 1170 px.

Los SVG finales contienen formas vectoriales y trazados de tipografía; no imágenes rasterizadas ni dependencias de fuentes para reproducirse. En un editor SVG pueden modificarse color, geometría y composición. Para cambiar palabras y volver a generar contornos, editar `tools/build_brand.py`.

## Paleta

| Función | HEX |
|---|---|
{colortable}
| Blanco de apoyo | `{d['light']}` |

Par de identidad recomendado: tinta sobre papel o papel sobre tinta. Contraste sRGB calculado: **{contrast(d['ink'],d['paper']):.2f}:1**. El color secundario funciona como superficie, no como texto pequeño sobre blanco. Usar tinta para texto informativo; revisar contraste cuando se creen combinaciones nuevas. Los logos no se evalúan como texto de interfaz, pero se privilegia su legibilidad.

## Tipografía

**Marca / titulares:** {d['display']}.

**Interfaz y textos:** Manrope 500 regular, 750 para énfasis y acciones. Titulares orientativos 32–76 px en escritorio, 28–38 px en móvil; cuerpo 16–18 px, interlineado 1.5. La presentación editorial usa tamaños propios por su función de catálogo de diseño.

{'En B, Fraunces se reserva para titulares y marca; Manrope sostiene navegación, categorías, precios y texto funcional.' if k=='b' else 'En C, Archivo Black se reserva para titulares cortos y marca; no usarla en párrafos ni todo el catálogo.' if k=='c' else 'El lettering del logotipo no es un alfabeto de texto. Usar Manrope en el resto del sistema.'}

Las familias originales y sus licencias SIL Open Font License están en `assets/fonts/`. No se adquirieron licencias ni se atribuye autoría del alfabeto al proyecto. Los archivos de fuente originales no se modificaron; se instanciaron sus ejes en memoria para dibujar contornos.

## Proporciones, espaciado y mínimos

- Grilla de interfaz: 8 px; espacios de 8, 16, 24, 32 y 48 px.
- Área libre: {'¼ de la altura completa del bloque' if k=='c' else '½ de la altura de la o de Poco'} en todo el perímetro visible. Los márgenes del archivo pueden no completar esa reserva: añadir espacio al colocarlo. El diagrama es una referencia de aplicación.
- Mantener la relación de aspecto del archivo final y la separación de sus elementos. No reescribir el logo usando una fuente parecida.
- Ancho mínimo digital orientativo: principal **{token['minimumPrimaryPx']} px**, horizontal **{token['minimumHorizontalPx']} px**, compacta **{token['minimumCompactPx']} px**. Por debajo, usar la inicial P del favicon.
- Favicon: 16 / 32 / 48 px; para perfiles grandes usar el nombre completo, para recortes menores de 48 px preferir P.
- Impresión: horizontal desde {'42' if k=='a' else '36' if k=='b' else '32'} mm de ancho; firma principal desde {'42' if k=='a' else '36' if k=='b' else '24'} mm. Son recomendaciones iniciales: realizar prueba física según papel, tinta y proceso.
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
'''
        write(Path('concepts')/f'concept-{k}'/'brand-guide.md',guide)
    evaltext='''# Evaluación comparativa

Fecha: 2 de noviembre de 2026. Escala 1–10. Juicio de diseño del estudio, no una encuesta, prueba comercial ni dictamen legal. Una puntuación más alta no elige automáticamente una ganadora.

| Criterio | Peso | A | B | C |
|---|---:|---:|---:|---:|
'''
    criteria=['Originalidad y diferenciación','Versatilidad multidepartamento','Legibilidad y reconocimiento','Atractivo para público general','Calidad profesional de ejecución','Aplicabilidad digital y comercial']
    weights=[20,20,20,15,15,10]
    for n,c in enumerate(criteria):evaltext+=f'| {c} | {weights[n]} % | '+ ' | '.join(str(d['weights'][n]) for d in DATA)+' |\n'
    evaltext+='| **Resultado ponderado** | **100 %** | '+' | '.join(f"**{sum(v*w/100 for v,w in zip(d['weights'],weights)):.2f}**" for d in DATA)+' |\n'
    evaltext+='''
Fórmula: suma de cada puntaje multiplicado por su peso / 100. El total es sobre 10. No incluye disponibilidad jurídica, porque no hay dictamen ni un resultado comparable para cada diseño: todos comparten el mismo nombre provisional.

## A — En buena compañía

- **Originalidad 8:** lettering dibujado con geometría propia y repetición consistente de las oes. Las formas geométricas son un lenguaje común; no se afirma exclusividad formal o jurídica.
- **Versatilidad 9:** el nombre no incorpora objetos de una categoría y conserva el mismo orden con audio, bandejas y soporte de automóvil.
- **Legibilidad 9:** masa y aperturas amplias en Poco. & co. exige respetar el mínimo de 200 px; por eso no recibe 10.
- **Atractivo 8:** neutral y sencillo; puede percibirse más técnico que afectivo sin una voz cálida.
- **Ejecución 9:** módulo de curvas consistente, alineaciones controladas y contornos independientes de fuentes. La compacta requiere aprendizaje de la abreviación p/c.
- **Aplicación 9:** la horizontal encaja bien en cabeceras y las dos tintas se reproducen con facilidad. El favicon usa una inicial que necesita construirse con reconocimiento de marca.

## B — Cada día, un poco

- **Originalidad 8:** proporción marcada de la P y composición editorial propia. Fraunces es una familia existente con licencia, por lo que la diferenciación no depende de inventar sus letras.
- **Versatilidad 8:** funciona en las tres categorías ilustradas; la combinación de serif y papel cálido tiene mayor afinidad percibida con hogar y selección de objetos.
- **Legibilidad 8:** buena lectura a escala normal; el contraste de trazos y la segunda línea exigen más ancho. La horizontal y la inicial resuelven espacios reducidos.
- **Atractivo 9:** formas abiertas y un sistema cálido sin recurrir a códigos románticos o infantiles. Esta hipótesis debe validarse con los fundadores y compradores.
- **Ejecución 9:** jerarquía clara, control de pesos y contraste entre marca editorial y texto funcional. Las aplicaciones conservan aire y consistencia.
- **Aplicación 8:** fuerte en etiqueta y publicación; la firma apilada no se adapta tan directamente a una cabecera estrecha como la A.

## C — Un mundo en Poco

- **Originalidad 8:** composición de dos líneas a un mismo ancho que da protagonismo a & CO. El lenguaje de bloque comercial y Archivo Black es compartido con otras identidades.
- **Versatilidad 9:** firma de categoría amplia; tecnología, hogar y automóvil conservan un mismo nivel de presencia.
- **Legibilidad 9:** contornos gruesos y alto contraste en tamaño pequeño; no alcanza 10 por el ampersand denso y porque la compacta no escribe el nombre de corrido.
- **Atractivo 8:** comunica energía y confianza comercial; puede resultar más intenso que el tono cálido de la historia de los fundadores.
- **Ejecución 8:** bloque reproducible con buena presencia, pero menos matiz y personalidad de letra que el lettering A o el contraste editorial B.
- **Aplicación 9:** compacto en empaque y publicaciones, con alternativa horizontal para tienda. Requiere márgenes generosos para evitar saturación visual.

## Conversación de fundadores

Valorar primero cuál representa a ambos y después qué ajustes merece. Revisar cada ruta sin color, en móvil y junto a productos de categorías diferentes. No sumar preferencias personales a la matriz como si fueran mediciones objetivas. Resolver el nombre antes del lanzamiento.
'''
    write(Path('comparison/evaluation.md'),evaltext)

def qa():
    errors=[]; svgfiles=sorted((ROOT/'concepts').rglob('*.svg')); pngfiles=sorted((ROOT/'concepts').rglob('*.png'))
    for p in svgfiles:
        try:
            doc=ET.fromstring(p.read_text(encoding='utf-8')); ids=[]
            assert doc.tag.endswith('svg') and len(doc.attrib['viewBox'].split())==4
            for node in doc.iter():
                if node.tag.endswith('image'):errors.append(f'Raster image in {p.relative_to(ROOT)}')
                if node.get('id'):ids.append(node.get('id'))
                for key,value in node.attrib.items():
                    if key.endswith('href') and not value.startswith('#'):errors.append(f'External SVG dependency: {p.relative_to(ROOT)}')
            if len(ids)!=len(set(ids)):errors.append(f'Duplicate SVG id: {p.relative_to(ROOT)}')
        except Exception as exc:errors.append(f'{p.relative_to(ROOT)}: {exc}')
    dimensions={}
    for p in pngfiles:
        try:
            with Image.open(p) as im:im.verify()
            with Image.open(p) as im:dimensions[str(p.relative_to(ROOT))]=list(im.size)
        except Exception as exc:errors.append(f'{p.relative_to(ROOT)}: {exc}')
    class Links(HTMLParser):
        def handle_starttag(self,tag,attrs):
            for key,v in attrs:
                if key in ['src','href'] and v and not v.startswith(('http:','https:','#','data:')):
                    if not (ROOT/'presentation'/v).resolve().exists():errors.append(f'Missing HTML link: {v}')
    Links().feed((ROOT/'presentation/index.html').read_text(encoding='utf-8'))
    for k in 'abc':
        for name in ['logo-primary','logo-horizontal','logo-compact','logo-monochrome','logo-light','logo-dark','logo-horizontal-dark','logo-compact-dark','logo-monochrome-dark','favicon']:
            for ext,sub in [('svg',''),('png','exports/')]:
                if not (ROOT/f'concepts/concept-{k}/{sub}{name}.{ext}').is_file():errors.append(f'Missing {k}/{sub}{name}.{ext}')
        for name in ['shopify-desktop','shopify-mobile','browser-favicon','instagram-profile','promotional-post','product-card','packaging-label']:
            if not (ROOT/f'concepts/concept-{k}/applications/{name}.svg').is_file():errors.append(f'Missing application: {k}/{name}')
    for family in ['manrope','fraunces','archivoblack']:
        if not (ROOT/f'assets/fonts/{family}/OFL.txt').is_file():errors.append('Font license missing: '+family)
    ratios={d['id']:{'ink_on_paper':round(contrast(d['ink'],d['paper']),2),'paper_on_ink':round(contrast(d['paper'],d['ink']),2),'accent_on_paper':round(contrast(d['accent'],d['paper']),2),'ink_on_secondary':round(contrast(d['ink'],d['secondary']),2)} for d in DATA}
    # Contact sheets complement, rather than replace, browser visual review.
    ui_font=ImageFont.truetype(str(next((ROOT/'assets/fonts/manrope').glob('*.ttf'))),18)
    for k in 'abc':
        names=['shopify-desktop','shopify-mobile','browser-favicon','instagram-profile','promotional-post','product-card','packaging-label']
        sheet=Image.new('RGB',(1600,1200),'#e7e8e0');draw=ImageDraw.Draw(sheet)
        for n,name in enumerate(names):
            x=(n%4)*400+15;y=(n//4)*570+45
            im=Image.open(ROOT/f'concepts/concept-{k}/exports/{name}.png').convert('RGBA');im=ImageOps.contain(im,(370,490));sheet.paste(im,(x+(370-im.width)//2,y),im)
            draw.text((x,y-28),f'{k.upper()} / {name}',font=ui_font,fill='#20312b')
        sheet.save(ROOT/f'qa/applications-{k}.png')
    sheet=Image.new('RGB',(1560,1290),'#e7e8e0');draw=ImageDraw.Draw(sheet)
    for col,k in enumerate('abc'):
        for row,v in enumerate(['primary','horizontal','compact','monochrome','light','dark']):
            x=col*520;y=row*190+30;bg=DATA[col]['ink'] if v=='dark' else DATA[col]['paper'];draw.rectangle((x+8,y,x+510,y+160),fill=bg)
            im=Image.open(ROOT/f'concepts/concept-{k}/exports/logo-{v}.png').convert('RGBA');im=ImageOps.contain(im,(440,145));sheet.paste(im,(x+40+(440-im.width)//2,y+7),im);draw.text((x+14,y+163),f'{k.upper()} / {v}',fill='#20312b',font=ui_font)
    sheet.save(ROOT/'qa/logo-variants.png')
    small=Image.new('RGB',(1440,540),'#f6f5ef');draw=ImageDraw.Draw(small)
    for n,k in enumerate('abc'):
        d=DATA[n];x=n*480+30;token=json.loads((ROOT/f'design-tokens/concept-{k}.json').read_text());draw.text((x,20),f'{k.upper()} / mínimos a tamaño real',fill=d['ink'],font=ui_font)
        for row,(name,w) in enumerate([('logo-primary',token['minimumPrimaryPx']),('logo-horizontal',token['minimumHorizontalPx']),('logo-compact',token['minimumCompactPx'])]):
            im=Image.open(ROOT/f'concepts/concept-{k}/exports/{name}.png').convert('RGBA');im=ImageOps.contain(im,(w,120));small.paste(im,(x,65+row*135),im);draw.text((x+230,76+row*135),f'{name[5:]} · {w} px',font=ui_font,fill=d['ink'])
        for j,size in enumerate([16,32,48]):
            im=Image.open(ROOT/f'concepts/concept-{k}/exports/favicon-{size}.png').convert('RGBA');small.paste(im,(x+j*90,475),im)
    small.save(ROOT/'qa/small-sizes.png')
    report={'date':'2026-11-02','svg_count':len(svgfiles),'png_count':len(pngfiles),'errors':errors,'contrast':ratios,'dimensions':dimensions}
    write(Path('qa/validation.json'),json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:report[k] for k in ['svg_count','png_count','errors','contrast']},indent=2))
    if errors:sys.exit(1)

if __name__=='__main__':documentation();qa()
