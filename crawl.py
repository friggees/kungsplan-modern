import requests,json,re,concurrent.futures, pathlib,xml.etree.ElementTree as E
from bs4 import BeautifulSoup
root=pathlib.Path(__file__).parent
(root/'reference').mkdir(exist_ok=True)
(root/'public/images').mkdir(parents=True,exist_ok=True)
urls=[x.text for x in E.parse(root.parent/'kungsplan-sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
def fetch(url):
 s=BeautifulSoup(requests.get(url,timeout=45).text,'html.parser'); slug=url.rstrip('/').split('/')[-1] if url.rstrip('/')!='https://kungsplantrafikskola.se' else 'home'
 for e in s.select('header,footer,script,style,nav'):e.decompose()
 body=s.select_one('[data-elementor-type="wp-page"]') or s
 text=body.get_text('\n',strip=True)
 (root/'reference'/f'{slug}.txt').write_text(text,encoding='utf-8')
 imgs=list(dict.fromkeys([i.get('src') for i in body.select('img[src]') if '/uploads/' in i.get('src','')]))
 return {'slug':slug,'url':url,'text':text,'images':imgs,'headings':[i.get_text(' ',strip=True) for i in body.select('h1,h2,h3')]}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: pages=list(ex.map(fetch,urls))
(root/'reference/pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
html=(root.parent/'kungsplan-original.html').read_text(encoding='utf-8')
assets=set(i for p in pages for i in p['images'])
assets.update(re.findall(r'https://kungsplantrafikskola.se/wp-content/uploads/[^\s"\)<>]+?\.(?:jpg|png|webp)',html))
def asset(url):
 name=url.split('/')[-1]; r=requests.get(url,timeout=40)
 if r.ok:(root/'public/images'/name).write_bytes(r.content)
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:list(ex.map(asset,assets))
print(json.dumps([{'slug':p['slug'],'headings':p['headings'],'images':p['images'][:2]} for p in pages],ensure_ascii=False,indent=2))
