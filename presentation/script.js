'use strict';
const data=window.BRAND_DATA;
const $=id=>document.getElementById(id);
const base=id=>`../concepts/concept-${id}/`;
const weights=[.20,.20,.20,.15,.15,.10];
const criteria=['Originalidad y diferenciación','Versatilidad multidepartamento','Legibilidad y reconocimiento','Atractivo para público general','Calidad profesional de ejecución','Aplicabilidad digital y comercial'];
const apps=[
 ['shopify-desktop','Tienda · escritorio','Cabecera conceptual compatible con una estructura de tienda Shopify. Incluye tecnología, hogar y automóvil. No se implementó una tienda.'],
 ['shopify-mobile','Tienda · móvil','La misma marca en 390 px de ancho. El logo horizontal conserva su espacio y la búsqueda tiene una fila propia.'],
 ['browser-favicon','Navegador','La inicial P identifica la pestaña a 16–32 px. La dirección .example es ficticia; no representa un dominio disponible.'],
 ['instagram-profile','Perfil de Instagram','El nombre completo queda dentro de la zona central del recorte circular. Para avatares menores de 48 px, usar la inicial del favicon.'],
 ['promotional-post','Publicación promocional','Formato 1080 × 1350. Tecnología como categoría protagonista. Producto y precio ilustrativos.'],
 ['product-card','Tarjeta de producto','Un accesorio para automóvil prueba la versatilidad comercial de la identidad. Producto y precio ilustrativos.'],
 ['packaging-label','Empaque y etiqueta','Simulación vectorial de caja kraft y etiqueta a una tinta. Los colores requieren prueba física antes de producción.']
];
let current='a',dark=false,app='shopify-desktop',toastTimer;
const cards=$('concept-cards');
for(const d of data){
 const article=document.createElement('article');article.className='concept-card';
 article.innerHTML=`<button class="concept-card-art" aria-label="Ampliar propuesta ${d.id.toUpperCase()}: ${d.name}" style="background:${d.paper}"><img src="${base(d.id)}logo-primary.svg" alt="Logotipo ${d.id.toUpperCase()} de Poco & Co."><span class="expand-label">Ampliar ↗</span></button><div class="concept-card-copy"><span class="card-letter">${d.id.toUpperCase()} /</span><div><h3>${d.name}</h3><p>${d.route}</p></div></div><div class="card-actions"><button class="explore-button">Explorar propuesta ${d.id.toUpperCase()} ↗</button><button class="card-mode" aria-pressed="false">Ver oscuro ◐</button></div>`;
 let cardDark=false;
 article.querySelector('.concept-card-art').addEventListener('click',()=>openImage(base(d.id)+(cardDark?'logo-dark.svg':'logo-primary.svg'),`Propuesta ${d.id.toUpperCase()} · ${d.name}`,cardDark?d.ink:d.paper));
 article.querySelector('.explore-button').addEventListener('click',()=>{setRoute(d.id);$('explorar').scrollIntoView({behavior:'smooth'});});
 article.querySelector('.card-mode').addEventListener('click',e=>{cardDark=!cardDark;const art=article.querySelector('.concept-card-art');art.style.background=cardDark?d.ink:d.paper;art.style.color=cardDark?d.paper:d.ink;art.querySelector('img').src=base(d.id)+(cardDark?'logo-dark.svg':'logo-primary.svg');e.currentTarget.textContent=cardDark?'Ver claro ◐':'Ver oscuro ◐';e.currentTarget.setAttribute('aria-pressed',String(cardDark));});
 cards.appendChild(article);
}

function setRoute(id){
 current=id;const d=data.find(x=>x.id===id);const root=document.documentElement;
 for(const key of ['ink','paper','accent','secondary'])root.style.setProperty(`--route-${key}`,d[key]);
 document.querySelectorAll('[data-route]').forEach(b=>{const active=b.dataset.route===id;b.setAttribute('aria-selected',String(active));b.tabIndex=active?0:-1;});
 $('route-panel').setAttribute('aria-labelledby',`tab-${id}`);$('route-label').textContent=`PROPUESTA ${id.toUpperCase()} / ${d.route}`;
 $('detail-title').textContent=d.name;$('concept-idea').textContent=d.idea;$('concept-strength').textContent=d.strength;$('concept-limit').textContent=d.limit;
 $('type-preview').style.fontFamily=id==='a'?'Manrope':id==='b'?'Fraunces':'Archivo Black';$('type-preview').style.fontWeight=id==='c'?'400':'600';
 $('type-name').textContent=d.display;$('type-note').textContent=id==='a'?'Lettering propio para el nombre. Manrope 500 / 750 para interfaz y comunicación.':'Fuente principal incluida con licencia SIL OFL. Manrope 500 / 750 acompaña textos e interfaz.';
 $('tokens-link').href=`../design-tokens/concept-${id}.json`;$('brand-guide').href=base(id)+'brand-guide.md';
 $('color-note').textContent=id==='a'?'Tinta azul y superficies abiertas. Cobalto para acciones; salvia para acompañar producto.':id==='b'?'Borgoña y papel cálido. Arcilla para acentos; oliva como contrapunto cotidiano.':'Verde profundo y papel claro. Óxido para acciones; lima suave para categorías y fondos.';
 const names=id==='a'?['Tinta','Niebla','Cobalto','Salvia']:id==='b'?['Borgoña','Avena','Arcilla','Oliva']:['Bosque','Papel','Óxido','Lima'];
 $('swatches').replaceChildren();['ink','paper','accent','secondary'].forEach((key,n)=>{const b=document.createElement('button');b.className='swatch';b.setAttribute('aria-label',`Copiar ${names[n]} ${d[key]}`);b.innerHTML=`<span class="swatch-color" style="background:${d[key]}"></span><span class="swatch-name">${names[n]}</span><span class="swatch-code">${d[key]}</span>`;b.addEventListener('click',()=>copyColor(d[key]));$('swatches').appendChild(b);});
 $('space-note').textContent=id==='c'?'Reservar ¼ de la altura del bloque a cada lado. Grilla de 8 px para interfaces.':'Reservar ½ de la altura de la o a cada lado. Grilla de 8 px para interfaces.';
 $('size-note').textContent={a:'Horizontal ≥ 200 px · compacta ≥ 80 px · inicial desde 16 px.',b:'Horizontal ≥ 164 px · principal ≥ 180 px · compacta ≥ 112 px.',c:'Horizontal ≥ 150 px · bloque ≥ 96 px · compacta ≥ 64 px.'}[id];
 updateLogo();updateApp();
 $('all-apps').replaceChildren();for(const [file,label] of apps){const b=document.createElement('button');b.className='app-preview';b.innerHTML=`<div><img src="${base(id)}applications/${file}.svg" alt="${label}, propuesta ${id.toUpperCase()}" loading="lazy"></div><span>${label} ↗</span>`;b.addEventListener('click',()=>{app=file;updateApp();openImage(base(current)+`applications/${file}.svg`,`${label} · ${d.name}`,d.paper);});$('all-apps').appendChild(b);}
}
function updateLogo(){
 const d=data.find(x=>x.id===current),variant=$('logo-variant').value;
 const name=variant==='favicon'?'favicon':dark?(variant==='primary'?'logo-dark':`logo-${variant}-dark`):`logo-${variant}`;
 const src=base(current)+`${name}.svg`;
 $('detail-logo').src=src;
 $('detail-logo').alt=`Poco & Co. · propuesta ${current.toUpperCase()} · ${$('logo-variant').selectedOptions[0].textContent}`;
 $('logo-stage').classList.toggle('dark',dark);
 $('detail-logo').style.filter='';
 $('download-svg').href=src;
 $('download-png').href=base(current)+`exports/${name}.png`;
 $('theme-toggle').setAttribute('aria-pressed',String(dark));$('theme-toggle').textContent=dark?'Fondo claro ◑':'Fondo oscuro ◐';
}
function updateApp(){
 const entry=apps.find(x=>x[0]===app);$('application-image').src=base(current)+`applications/${app}.svg`;$('application-image').alt=`${entry[1]} de Poco & Co., propuesta ${current.toUpperCase()}`;$('application-caption').textContent=entry[2];
 $('app-svg').href=base(current)+`applications/${app}.svg`;$('app-png').href=base(current)+`exports/${app}.png`;
 document.querySelectorAll('[data-app]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.app===app)));
 const frame=document.querySelector('.application-frame');frame.classList.toggle('mobile',app==='shopify-mobile');frame.classList.toggle('social',app==='promotional-post'||app==='product-card');frame.classList.toggle('profile',app==='instagram-profile');
}
function openImage(src,title,background,filter=''){$('dialog-title').textContent=title;$('dialog-image').src=src;$('dialog-image').alt=title;$('dialog-image').style.filter=filter;$('dialog-stage').style.background=background;$('image-dialog').showModal();}
function toast(message){$('toast').textContent=message;$('toast').classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').classList.remove('visible'),2300);}
async function copyColor(value){try{if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(value);toast(`${value} copiado`);}else{toast(`Color: ${value} · selecciona el HEX para copiar`);}}catch{toast(`Color: ${value} · copia el HEX que aparece bajo la muestra`);}}
document.querySelectorAll('[data-route]').forEach(b=>{b.addEventListener('click',()=>setRoute(b.dataset.route));b.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;e.preventDefault();let n='abc'.indexOf(current);n=e.key==='Home'?0:e.key==='End'?2:(n+(e.key==='ArrowRight'?1:2))%3;setRoute('abc'[n]);$(`tab-${'abc'[n]}`).focus();});});
document.querySelectorAll('[data-app]').forEach(b=>b.addEventListener('click',()=>{app=b.dataset.app;updateApp();}));
$('logo-variant').addEventListener('change',updateLogo);$('theme-toggle').addEventListener('click',()=>{dark=!dark;updateLogo();});
$('logo-stage').addEventListener('click',()=>{const d=data.find(x=>x.id===current);openImage($('detail-logo').getAttribute('src'),$('detail-logo').alt,dark?d.ink:d.paper,$('detail-logo').style.filter);});
$('application-zoom').addEventListener('click',()=>openImage($('application-image').getAttribute('src'),$('application-image').alt,data.find(x=>x.id===current).paper));
$('dialog-close').addEventListener('click',()=>$('image-dialog').close());$('image-dialog').addEventListener('click',e=>{if(e.target===$('image-dialog'))$('image-dialog').close();});
const tbody=$('score-table');criteria.forEach((name,n)=>{const tr=document.createElement('tr');tr.innerHTML=`<td>${name}</td><td>${Math.round(weights[n]*100)} %</td>${data.map(d=>`<td>${d.weights[n]}<span class="small muted"> / 10</span></td>`).join('')}`;tbody.appendChild(tr);});
const total=document.createElement('tr');total.innerHTML='<td>Resultado ponderado</td><td>100 %</td>'+data.map(d=>`<td>${d.weights.reduce((s,v,n)=>s+v*weights[n],0).toFixed(2).replace('.',',')}<span class="small muted"> / 10</span></td>`).join('');tbody.appendChild(total);
setRoute('a');
