"""Snapshot public SEO metadata, sitemap URLs and linked internal pages."""
import concurrent.futures, json, pathlib, urllib.parse, xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).parent
BASE = 'https://kungsplantrafikskola.se'
def get(url):
    r = requests.get(url, timeout=40)
    r.raise_for_status()
    return r

def sitemap(url):
    doc = ET.fromstring(get(url).content)
    locs = [e.text for e in doc.findall('.//{*}loc')]
    return [u for loc in locs for u in sitemap(loc)] if doc.tag.endswith('sitemapindex') else locs

def fetch(url):
    r = get(url)
    s = BeautifulSoup(r.content, 'html.parser')
    def meta(key):
        el = s.find('meta', attrs={'name': key}) or s.find('meta', attrs={'property': key})
        return el.get('content', '') if el else ''
    canonical = s.find('link', rel='canonical')
    links = set()
    for a in s.select('a[href]'):
        u = urllib.parse.urlsplit(urllib.parse.urljoin(r.url, a['href']))
        if u.hostname == urllib.parse.urlsplit(BASE).hostname and not u.query and not pathlib.PurePosixPath(u.path).suffix and not u.path.startswith(('/wp-', '/feed')):
            links.add(BASE + (u.path.rstrip('/') + '/' if u.path else '/'))
    return {'url': url, 'path': urllib.parse.urlsplit(url).path or '/', 'status': r.status_code,
            'title': s.title.get_text() if s.title else '', 'description': meta('description'),
            'canonical': canonical.get('href', '') if canonical else '', 'robots': meta('robots'),
            'h1': [h.get_text(' ', strip=True) for h in s.select('h1')],
            'social': {k: meta(k) for k in ['og:title','og:description','og:url','og:type','og:image','og:locale','og:site_name','twitter:card','twitter:title','twitter:description','twitter:image'] if meta(k)},
            'jsonld': [json.loads(x.string) for x in s.select('script[type="application/ld+json"]') if x.string],
            'links': sorted(links)}

if __name__ == '__main__':
    urls = set(sitemap(BASE + '/sitemap_index.xml'))
    urls = {u for u in urls if not pathlib.PurePosixPath(urllib.parse.urlsplit(u).path).suffix}
    seen, pages = set(), []
    while urls - seen:
        batch = sorted(urls - seen)
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            results = list(pool.map(fetch, batch))
        pages.extend(results)
        seen.update(batch)
        urls.update(u for page in results for u in page['links'])
    pages.sort(key=lambda p:p['path'])
    (ROOT/'reference/seo-original.json').write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps([{k:p[k] for k in ['path','title','description','canonical','h1']} for p in pages], ensure_ascii=True, indent=2))
