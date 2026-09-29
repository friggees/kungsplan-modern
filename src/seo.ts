import entries from './seo-pages.json';

export function updateSeo(pathname: string) {
  const path = '/' + pathname.replace(/^\/+|\/+$/g, '') + '/';
  const seo = entries.find(entry => entry.path === (path === '//' ? '/' : path));
  document.querySelectorAll('[data-page-seo]').forEach(node => node.remove());
  const meta = (key: string, content: string) => {
    const node = document.createElement('meta');
    node.setAttribute(key.startsWith('og:') ? 'property' : 'name', key);
    node.content = content;
    node.dataset.pageSeo = '';
    document.head.append(node);
  };
  document.title = seo?.title ?? 'Sidan finns inte | Kungsplan Trafikskola';
  // Demo only. Remove noindex as part of the real-domain launch.
  meta('robots', 'noindex, follow');
  if (!seo) return;
  meta('description', seo.description);
  const canonical = document.createElement('link');
  canonical.rel = 'canonical';
  canonical.href = seo.canonical;
  canonical.dataset.pageSeo = '';
  document.head.append(canonical);
  Object.entries(seo.social).forEach(([key, value]) => { if (value) meta(key, value); });
}
