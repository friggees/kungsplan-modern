import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

const entries = JSON.parse(await readFile('src/seo-pages.json', 'utf8'));
const template = await readFile('dist/index.html', 'utf8');
const escape = value => value.replaceAll('&', '&amp;').replaceAll('"', '&quot;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');
const base = template.replace(/<title>[\s\S]*?<\/title>/, '').replace(/<meta\b[^>]*data-page-seo[^>]*>/g, '');
for (const entry of entries) {
  const tags = [
    `<title>${escape(entry.title)}</title>`,
    `<meta data-page-seo name="description" content="${escape(entry.description)}">`,
    '<meta data-page-seo name="robots" content="noindex, follow">',
    `<link data-page-seo rel="canonical" href="${escape(entry.canonical)}">`,
    ...Object.entries(entry.social).map(([key, value]) => `<meta data-page-seo ${key.startsWith('og:') ? 'property' : 'name'}="${escape(key)}" content="${escape(value)}">`),
  ];
  const dir = path.join('dist', entry.path);
  await mkdir(dir, { recursive: true });
  await writeFile(path.join(dir, 'index.html'), base.replace('</head>', tags.join('\n') + '\n</head>'));
}
await writeFile('dist/404.html', base.replace('</head>', '<title>Sidan finns inte | Kungsplan Trafikskola</title><meta data-page-seo name="robots" content="noindex, follow"></head>'));
console.log(`Generated static SEO metadata for ${entries.length} pages and a 404 document.`);
