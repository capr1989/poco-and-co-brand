// Run after build_brand.py. Install @resvg/resvg-js under work/, never globally.
const fs = require('fs');
const path = require('path');
const { Resvg } = require('../work/node_modules/@resvg/resvg-js');
const root = path.resolve(__dirname, '..');
let count = 0;
for (const id of ['a', 'b', 'c']) {
  const base = path.join(root, 'concepts', `concept-${id}`);
  const exportsDir = path.join(base, 'exports');
  fs.mkdirSync(exportsDir, { recursive: true });
  for (const name of fs.readdirSync(base).filter(n => n.endsWith('.svg') && !n.startsWith('typography'))) {
    const input = fs.readFileSync(path.join(base, name));
    const opts = { fitTo: { mode: 'width', value: name === 'favicon.svg' ? 512 : 3000 } };
    fs.writeFileSync(path.join(exportsDir, name.replace('.svg', '.png')), new Resvg(input, opts).render().asPng());
    count++;
    if (name === 'favicon.svg') for (const size of [16, 32, 48]) {
      fs.writeFileSync(path.join(exportsDir, `favicon-${size}.png`), new Resvg(input, {fitTo:{mode:'width',value:size}}).render().asPng());
      count++;
    }
  }
  for (const name of fs.readdirSync(path.join(base, 'applications')).filter(n => n.endsWith('.svg'))) {
    fs.writeFileSync(path.join(exportsDir, name.replace('.svg', '.png')), new Resvg(fs.readFileSync(path.join(base, 'applications', name)), {fitTo:{mode:'width',value:name==='shopify-mobile.svg'?1170:2160}}).render().asPng());
    count++;
  }
}
console.log(`Exported ${count} PNGs with resvg.`);
fs.writeFileSync(path.join(root,'comparison','proposals.png'),new Resvg(fs.readFileSync(path.join(root,'comparison','proposals.svg')),{fitTo:{mode:'width',value:2400}}).render().asPng());
