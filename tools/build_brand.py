"""Build the editable vector identity study. No raster assets or remote runtime resources."""
from pathlib import Path
from html import escape
import json, math, re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'assets/fonts'

def font(family, pattern, axes=None):
    f = TTFont(next((FONTS / family).glob(pattern)))
    if axes: f = instantiateVariableFont(f, axes, inplace=False)
    return f

SANS = font('manrope', '*.ttf', {'wght':500})
BOLD = font('manrope', '*.ttf', {'wght':750})
SERIF = font('fraunces', 'Fraunces[[]SOFT*', {'wght':600,'opsz':72,'SOFT':40,'WONK':1})
BLACK = font('archivoblack', '*.ttf')

def text(s, x, y, size, color, f=SANS, spacing=0, align='left'):
    """Outline each glyph; y is baseline. Geometry stays font independent and editable."""
    gs=f.getGlyphSet(); cmap=f.getBestCmap(); scale=size/f['head'].unitsPerEm
    advance=sum(f['hmtx'][cmap.get(ord(c),'space')][0]*scale+spacing for c in s)-spacing
    if align=='center': x-=advance/2
    if align=='right': x-=advance
    paths=[]
    for c in s:
        name=cmap.get(ord(c),'space'); pen=SVGPathPen(gs); gs[name].draw(pen)
        if pen.getCommands(): paths.append(f'<path d="{pen.getCommands()}" transform="translate({x:.3f} {y}) scale({scale:.7f} {-scale:.7f})"/>')
        x+=f['hmtx'][name][0]*scale+spacing
    return f'<g fill="{color}" aria-label="{escape(s,quote=True)}">'+''.join(paths)+'</g>'

def width(s,size,f=SANS,spacing=0):
    cm=f.getBestCmap(); return sum(f['hmtx'][cm.get(ord(c),'space')][0]*size/f['head'].unitsPerEm+spacing for c in s)-spacing

def rect(x,y,w,h,fill,rx=0,stroke=None,sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>'

def line(x1,y1,x2,y2,color,sw=1):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{color}" stroke-width="{sw}"/>' if y1==y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{sw}"/>'

def svg(w,h,body,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{body}</svg>'

def write(path, content):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding='utf-8')

DATA=[
 dict(id='a',name='En buena compañía',route='Geométrica · serena · contemporánea',ink='#192C46',paper='#F1F4F2',accent='#2855D9',secondary='#B8CEC7',light='#FFFFFF',font='Manrope',display='Lettering geométrico original',claim='Lo útil. Lo tuyo.',idea='Las dos oes comparten exactamente la misma construcción: dos presencias que avanzan al mismo ritmo. Un lettering de curvas tensas y remates planos pone el nombre por delante de cualquier categoría.',strength='Orden, lectura rápida y un sistema sobrio que deja respirar a productos muy diferentes.',limit='La geometría necesita una voz y una fotografía cálidas para evitar una percepción demasiado tecnológica.',weights=[8,9,9,8,9,9]),
 dict(id='b',name='Cada día, un poco',route='Editorial · cálida · sofisticada',ink='#532C30',paper='#F5EDDF',accent='#94543C',secondary='#ADB18A',light='#FFFDF8',font='Fraunces',display='Fraunces 600 · óptica 72 · suavidad 40',claim='Cosas que se quedan.',idea='Una serif de curvas generosas y un ampersand explícito hablan de compañía sin recurrir a corazones. La composición editorial convierte la selección de objetos cotidianos en un gesto de cuidado.',strength='Transmite cercanía y atención al detalle en empaque, hogar y comunicación de producto.',limit='La serif demanda más tamaño en interfaces pequeñas; sin variedad de categorías podría percibirse como una tienda de hogar.',weights=[8,8,8,9,9,8]),
 dict(id='c',name='Un mundo en Poco',route='Compacta · directa · comercial',ink='#153E35',paper='#F1F0E7',accent='#BA4429',secondary='#CFDC96',light='#FFFFFF',font='Archivo Black',display='Archivo Black · composición de bloque',claim='Tu día tiene de todo.',idea='Dos líneas con un mismo ancho convierten el nombre completo en una firma compacta. La palabra compañía tiene presencia real: & CO. sostiene el bloque, en vez de ser una nota al margen.',strength='Alta presencia en etiquetas, publicaciones y señalización con una firma fácil de reproducir a una tinta.',limit='La masa tipográfica es más enérgica; necesita márgenes amplios y moderación en promociones para no sugerir descuento permanente.',weights=[8,9,9,8,8,9])
]

def a_letter(char,x,y,sz=1,color='#192C46'):
    # All curves are cubic Beziers, one shared bowl module. The p has an extended stem.
    ring='M50 0C80 0 100 21 100 52C100 83 80 104 50 104C20 104 0 83 0 52C0 21 20 0 50 0ZM50 24C34 24 25 35 25 52C25 69 34 80 50 80C66 80 75 69 75 52C75 35 66 24 50 24Z'
    if char=='p': d=ring
    elif char=='c':
        d='M94 16L78 35C70 27 62 24 51 24C34 24 25 35 25 52C25 69 34 80 51 80C62 80 70 77 78 69L94 88C82 100 68 104 50 104C20 104 0 83 0 52C0 21 20 0 50 0C68 0 82 4 94 16Z'
    else: d=ring
    stem=rect(0,51,25,94,color) if char=='p' else ''
    return f'<g id="letter-{char}-{x}" transform="translate({x} {y}) scale({sz})">{stem}<path fill="{color}" fill-rule="evenodd" d="{d}"/></g>'

def logo(d,variant='primary',color=None):
    k=d['id']; co=color or d['ink']
    if variant=='favicon':
        if k=='a': body=a_letter('p',31,23,.68,d['light'])
        elif k=='b': body=text('P',64,103,116,d['light'],SERIF,align='center')
        else: body=text('P',64,99,95,d['light'],BLACK,align='center')
        return svg(128,128,rect(0,0,128,128,d['accent'] if k=='a' else d['ink'],24)+body,'Poco & Co. — inicial de uso reducido')
    if variant=='compact':
        if k=='a': body=a_letter('p',44,32,1.03,co)+a_letter('c',160,32,1.03,co)+text('&',143,216,38,co,BOLD,align='center')
        elif k=='b': body=text('P',148,185,200,co,SERIF,align='center')+text('& CO.',150,231,26,co,SANS,2,align='center')
        else: body=text('PO',150,125,107,co,BLACK,-3,align='center')+text('CO.',150,218,98,co,BLACK,-3,align='center')
        return svg(300,270,body,'Poco & Co. — firma compacta')
    if k=='a':
        body=''.join(a_letter(ch,x,48,1.12,co) for ch,x in zip('poco',[32,157,282,401]))
        body+=text('&',554,95,38,co,BOLD)+text('co.',552,154,38,co,BOLD)
        return svg(660,240,body,'Poco & Co. — lettering geométrico')
    if k=='b':
        if variant=='horizontal':
            return svg(760,230,text('Poco',38,169,205,co,SERIF,-4)+text('& Co.',529,166,63,co,SERIF,-1),'Poco & Co. — firma horizontal editorial')
        return svg(600,320,text('Poco',300,216,250,co,SERIF,-4,align='center')+text('& CO.',300,282,37,co,SANS,5,align='center'),'Poco & Co. — firma editorial')
    if variant=='horizontal':
        return svg(800,210,text('POCO',35,151,161,co,BLACK,-5)+text('& CO.',526,149,81,co,BLACK,-2),'Poco & Co. — firma horizontal comercial')
    # Optical horizontal scaling: two lines share the same visual block width.
    top=text('POCO',0,0,145,co,BLACK,-5); bot=text('& CO.',0,0,109,co,BLACK,-2)
    tw=width('POCO',145,BLACK,-5); bw=width('& CO.',109,BLACK,-2)
    return svg(600,340,f'<g transform="translate(65 154) scale({470/tw} 1)">{top}</g><g transform="translate(65 282) scale({470/bw} 1)">{bot}</g>','Poco & Co. — bloque comercial de dos líneas')

def embed_logo(d,x,y,w,h,variant='horizontal',color=None):
    raw=logo(d,variant,color)
    prefix=f'embed-{d["id"]}-{x}-{y}-'
    raw=re.sub(r'\bid="([^"]+)"',lambda m:f'id="{prefix}{m.group(1)}"',raw)
    raw=raw.replace('aria-labelledby="title"',f'aria-labelledby="{prefix}title"')
    return re.sub(r'<svg ',f'<svg x="{x}" y="{y}" ',raw,count=1).replace(re.search(r'width="[^"]+" height="[^"]+"',raw)[0],f'width="{w}" height="{h}"',1)

def obj(kind,x,y,scale=1):
    """Original product illustrations; concept placeholders, no third party photography."""
    dark='#29343B'; mid='#A3AFAF'; pale='#E6E9E4'
    if kind=='tech':
        b=f'<ellipse cx="150" cy="258" rx="115" ry="15" fill="#000" opacity=".09"/>'
        b+=rect(37,134,226,110,'#E7E9E6',45,mid)+rect(42,139,216,43,'#F8F9F5',23)
        b+=line(43,183,257,183,mid)+rect(140,208,20,5,dark,2)
        b+=f'<g transform="rotate(-13 86 86)">{rect(59,28,43,101,pale,20,mid)}{rect(54,24,59,47,"#F9FAF5",22,mid)}{rect(65,35,17,18,dark,8)}</g>'
        b+=f'<g transform="rotate(13 214 86)">{rect(192,28,43,101,pale,20,mid)}{rect(184,24,59,47,"#F9FAF5",22,mid)}{rect(214,35,17,18,dark,8)}</g>'
    elif kind=='home':
        b='<ellipse cx="150" cy="254" rx="135" ry="15" fill="#000" opacity=".09"/>'
        for yy,xx,ww in [(129,24,252),(102,41,219),(73,59,184)]:
            b+=rect(xx,yy,ww,117,'#B7A38A',18,'#7F715E',2)+rect(xx+7,yy+7,ww-14,71,'#D6C7B1',13,'#A28F73')
            b+=line(xx+24,yy+49,xx+ww-24,yy+49,'#BAA98F',2)
    else:
        b='<ellipse cx="150" cy="264" rx="107" ry="13" fill="#000" opacity=".1"/>'
        b+=rect(84,226,132,26,dark,13)+f'<path d="M145 231L167 165L129 126" fill="none" stroke="#65726F" stroke-width="22" stroke-linecap="round"/>'
        b+=f'<g transform="rotate(-12 148 100)">{rect(87,20,122,176,dark,25)}{rect(99,31,98,151,"#83938C",16)}{rect(124,37,47,7,dark,3)}{rect(74,91,25,44,"#142B28",9)}{rect(197,91,25,44,"#142B28",9)}</g>'
    return f'<g transform="translate({x} {y}) scale({scale})">{b}</g>'

def icon_search(x,y,c): return f'<g transform="translate({x} {y})" fill="none" stroke="{c}" stroke-width="2"><circle cx="9" cy="9" r="7"/><path d="M14 14L21 21"/></g>'
def icon_bag(x,y,c): return f'<g transform="translate({x} {y})" fill="none" stroke="{c}" stroke-width="2"><path d="M3 8H21V26H3ZM8 8V5C8 -1 16 -1 16 5V8"/></g>'

PRODUCTS=[('tech','TECNOLOGÍA','Audio sin cables','B/. 29.00'),('home','HOGAR','Bandejas que ordenan','B/. 18.00'),('auto','EN MOVIMIENTO','Soporte para tu ruta','B/. 16.00')]

def desktop(d):
    i,p,a,s=d['ink'],d['paper'],d['accent'],d['secondary']
    f=SERIF if d['id']=='b' else BLACK if d['id']=='c' else BOLD
    b=rect(0,0,1440,1080,d['light'])+rect(0,0,1440,32,i)+text('UNA SELECCIÓN PARA TU DÍA A DÍA',720,22,12,p,SANS,2,align='center')
    b+=embed_logo(d,49,49,227,72)+rect(485,64,580,43,p,7)+text('¿Qué estás buscando hoy?',506,92,16,i)+icon_search(1028,75,i)+text('Mi cuenta',1152,91,15,i)+icon_bag(1305,69,i)
    b+=line(0,138,1440,138,'#D6DAD4')
    for name,x in [('Todo',65),('Tecnología',196),('Hogar',389),('Automóvil',535),('Accesorios',724),('Mascotas',911),('Viajes',1092)]: b+=text(name,x,176,15,i)
    b+=rect(44,204,1352,440,p,12)+text('POCO & CO. / SELECCIÓN 01',88,253,13,i,SANS,2)
    if d['id']=='a': lines=['Lo útil.','Lo tuyo.']
    elif d['id']=='b': lines=['Cosas que','se quedan.']
    else: lines=['TU DÍA TIENE','DE TODO.']
    for n,ss in enumerate(lines): b+=text(ss,85,350+n*86,76,i,f,-2)
    b+=text('Para casa, para salir, para acompañarte.',89,506,18,i)
    b+=rect(88,549,202,49,i,5)+text('Explorar la selección',189,580,15,p,BOLD,align='center')
    b+=rect(834,248,510,347,s,6)+obj('tech',866,300,.78)+obj('home',1064,350,.78)+text('Pequeñas soluciones. Más posibilidades.',1090,619,14,i,SANS,align='center')
    b+=text('Tres formas de mejorar tu día',49,713,30,i,f,-.5)
    for n,(kind,cat,title,price) in enumerate(PRODUCTS):
        x=48+n*456; b+=rect(x,746,432,204,p,7)+obj(kind,x+107,737,.73)
        b+=text(cat,x,981,11,i,SANS,1.4)+text(title,x,1010,20,i,BOLD)+text(price,x,1042,18,i)
    return svg(1440,1080,b,'Aplicación conceptual de cabecera Shopify en escritorio — '+d['name'])

def mobile(d):
    i,p,a,s=d['ink'],d['paper'],d['accent'],d['secondary']; f=SERIF if d['id']=='b' else BOLD
    b=rect(0,0,390,844,d['light'])+rect(0,0,390,27,i)+text('PARA TU DÍA A DÍA',195,18,9,p,SANS,1.5,align='center')
    b+=line(20,59,40,59,i,2)+line(20,65,40,65,i,2)+line(20,71,40,71,i,2)+embed_logo(d,95,35,193,55)+icon_bag(343,53,i)
    b+=rect(18,103,354,39,p,5)+text('Buscar en Poco & Co.',32,128,13,i)+icon_search(337,112,i)
    b+=rect(18,160,354,413,p,9)+text('SELECCIÓN 01',38,192,10,i,SANS,1.5)
    words=['Lo útil. Lo tuyo.'] if d['id']=='a' else ['Cosas que','se quedan.'] if d['id']=='b' else ['Tu día tiene','de todo.']
    for n,ss in enumerate(words): b+=text(ss,36,239+n*44,35,i,f,-.9)
    b+=obj('tech',107,291 if len(words)==1 else 309,.75)
    b+=rect(37,508,316,44,i,5)+text('Explorar la selección',195,536,13,p,BOLD,align='center')
    b+=text('Un poco de todo',19,615,23,i,f)
    for n,(kind,cat,title,price) in enumerate(PRODUCTS[:2]):
        x=18+n*182; b+=rect(x,636,172,126,p,5)+obj(kind,x+20,639,.43)+text(cat,x,784,9,i,SANS,.8)+text(price,x,811,15,i,BOLD)
    return svg(390,844,b,'Aplicación conceptual de cabecera Shopify móvil — '+d['name'])

def profile(d):
    i,p=d['ink'],d['paper']; b=rect(0,0,1080,1080,i)+embed_logo(d,164,170,752,690,'primary',p)
    return svg(1080,1080,b,'Avatar Instagram — nombre completo dentro del recorte circular seguro')

def promo(d):
    i,p,a,s=d['ink'],d['paper'],d['accent'],d['secondary']; f=SERIF if d['id']=='b' else BLACK if d['id']=='c' else BOLD
    b=rect(0,0,1080,1350,p)+embed_logo(d,57,41,330,131,'horizontal')+text('SELECCIÓN / TECNOLOGÍA',1004,112,16,i,SANS,1,align='right')
    b+=text('Dale espacio',62,310,96,i,f,-3)+text('a lo que sigue.',62,419,96,i,f,-3)
    b+=rect(61,484,958,580,s,12)+obj('tech',237,502,2.0)
    b+=text('Audio sin cables',65,1140,42,i,BOLD)+text('B/. 29.00',1009,1140,38,i,BOLD,align='right')
    b+=line(64,1190,1016,1190,i)+text('Más libertad para tu rutina.',65,1245,25,i)+text('POCO & CO.',1014,1300,14,i,BOLD,1,align='right')
    return svg(1080,1350,b,'Publicación promocional — producto y precio ilustrativos')

def product_card(d):
    i,p=d['ink'],d['paper']; b=rect(0,0,800,1040,d['light'])+rect(32,32,736,650,p,12)+obj('auto',151,70,1.65)
    b+=embed_logo(d,61,55,200,75)+text('AUTOMÓVIL / ACCESORIOS',40,738,18,i,SANS,2)+text('Tu próxima ruta,',40,801,43,i,BOLD,-1)+text('con todo en su lugar.',40,853,43,i,BOLD,-1)
    b+=text('Soporte ajustable para teléfono',40,900,24,i)+text('B/. 16.00',40,977,39,i,BOLD)+rect(432,926,326,71,i,6)+text('Ver producto',595,972,24,p,BOLD,align='center')
    return svg(800,1040,b,'Tarjeta de producto — soporte para automóvil, precio ilustrativo')

def packaging(d):
    i,p,a=d['ink'],d['paper'],d['accent']; b=rect(0,0,1200,900,p)
    b+='<ellipse cx="555" cy="694" rx="414" ry="45" fill="#000" opacity=".08"/>'
    b+=f'<path d="M160 346L620 220L1015 350L552 492Z" fill="#CDB898"/><path d="M160 346L552 492V744L160 583Z" fill="#BDA786"/><path d="M552 492L1015 350V595L552 744Z" fill="#DCC9AB"/>'
    # Flat paper band on front; transform maps original artwork onto box face.
    b+=f'<g transform="matrix(1 -.306 0 .88 619 487)">{rect(0,0,315,215,d["light"])}{embed_logo(d,24,20,268,113,"horizontal")}{line(25,147,288,147,i)}{text("UN POCO PARA TU DÍA.",25,178,14,i,BOLD,1)}</g>'
    b+=f'<g transform="translate(73 53) rotate(-5 125 140)">{rect(0,0,272,316,i,3)}{embed_logo(d,27,28,216,156,"primary",p)}{line(30,217,242,217,p)}{text("HECHO PARA ACOMPAÑARTE",136,256,10,p,SANS,1,align="center")}{text("POCO & CO.",136,284,12,p,BOLD,1,align="center")}<circle cx="136" cy="14" r="5" fill="{p}"/></g>'
    b+=text('EMPAQUE / ETIQUETA',64,817,18,i,SANS,2)+text('Caja kraft · impresión a una tinta · etiqueta adhesiva',64,852,20,i)
    return svg(1200,900,b,'Aplicación de empaque y etiqueta comercial — simulación vectorial')

def browser(d):
    b=rect(0,0,1000,240,'#E0E4DF',14)+rect(19,18,334,53,d['light'],12)+embed_logo(d,37,30,28,28,'favicon')+text('Poco & Co. — Tienda online',79,51,16,d['ink'])+text('×',322,52,23,d['ink'])
    b+=rect(20,87,960,54,d['light'],25)+text('pocoandco.example / colección',63,122,18,d['ink'])+text('Dirección de demostración · no representa un dominio disponible',30,203,18,d['ink'])
    return svg(1000,240,b,'Favicon en una pestaña del navegador — dirección ficticia .example')

def main():
    app_functions={'shopify-desktop':desktop,'shopify-mobile':mobile,'instagram-profile':profile,'promotional-post':promo,'product-card':product_card,'packaging-label':packaging,'browser-favicon':browser}
    for d in DATA:
        base=Path('concepts')/('concept-'+d['id'])
        for v in ['primary','horizontal','compact','monochrome','light','dark']:
            color='#000000' if v=='monochrome' else d['paper'] if v=='dark' else d['ink']
            content=logo(d,'primary' if v in ['monochrome','light','dark'] else v,color)
            write(base/f'logo-{v}.svg',content)
        write(base/'favicon.svg',logo(d,'favicon'))
        for v in ['horizontal','compact','monochrome']:
            write(base/f'logo-{v}-dark.svg',logo(d,'primary' if v=='monochrome' else v,'#FFFFFF' if v=='monochrome' else d['paper']))
        for name,fn in app_functions.items(): write(base/'applications'/f'{name}.svg',fn(d))
        construction=rect(0,0,1000,620,d['paper'])+rect(92,88,816,370,'none',0,d['ink'])+embed_logo(d,175,120,650,295,'primary')+text('ÁREA DE SEGURIDAD',92,54,16,d['ink'],SANS,2)+text('Mantener libre el perímetro indicado; no agregar marcos al logotipo.',92,520,17,d['ink'])+text('A / B: ½ de la altura de la o. C: ¼ de la altura del bloque.',92,555,17,d['ink'])
        write(base/'logo-clear-space.svg',svg(1000,620,construction,'Área libre de referencia — el marco es una guía y no forma parte del logotipo'))
        # A live-text typography source accompanies portable outlines. A is custom paths.
        editable=svg(1200,440,rect(0,0,1200,440,d['paper'])+f'<text x="65" y="220" fill="{d["ink"]}" font-family="{d["font"]}" font-size="180" font-weight="600">Poco &amp; Co.</text><text x="65" y="340" fill="{d["ink"]}" font-family="Manrope" font-size="23">Estudio tipográfico editable; usar los SVG de logotipo para reproducción final.</text>','Fuente de composición tipográfica — requiere instalar la fuente incluida')
        write(base/'typography-editable.svg',editable)
        token={key:d[key] for key in ['id','name','ink','paper','accent','secondary','light','font','display']}
        token.update(spacingBase=8,clearSpace='0.5 × altura de la o / 0.25 × altura del bloque en C',minimumHorizontalPx={'a':200,'b':164,'c':150}[d['id']],minimumPrimaryPx={'a':200,'b':180,'c':96}[d['id']],minimumCompactPx={'a':80,'b':112,'c':64}[d['id']],faviconPx=[16,32,48])
        write(Path('design-tokens')/f'concept-{d["id"]}.json',json.dumps(token,ensure_ascii=False,indent=2))
    write(Path('presentation')/'data.js','window.BRAND_DATA = '+json.dumps(DATA,ensure_ascii=False,indent=2)+';\n')
    board=rect(0,0,1500,790,'#F6F5EF')+text('POCO & CO. / ESTUDIO DE IDENTIDAD 01',54,54,14,'#202D2E',BOLD,1.5)+text('Tres maneras de empezar.',50,143,65,'#202D2E',SANS,-2)
    for n,d in enumerate(DATA):
        x=50+n*475
        board+=rect(x,206,450,280,d['paper'])+embed_logo(d,x+25,231,400,230,'primary')
        board+=text(d['id'].upper()+' /',x,533,13,d['ink'],BOLD)+text(d['name'],x,577,27,d['ink'],BOLD,-.6)+text(d['route'],x,611,12,d['ink'])
        for j,key in enumerate(['ink','paper','accent','secondary']):board+=rect(x+j*47,642,38,13,d[key],2,'#00000015')
    board+=line(50,703,1450,703,'#CCD1C5')+text('NOMBRE PROVISIONAL · PROPUESTAS PARA REVISIÓN DE LOS FUNDADORES',50,743,12,'#5A655D',SANS,1)
    write(Path('comparison/proposals.svg'),svg(1500,790,board,'Tres propuestas de identidad para Poco & Co. — nombre provisional'))
    print('Built 30 logo SVGs, 21 applications, 3 clear-space diagrams, 3 editable typography studies and tokens.')

if __name__=='__main__': main()
