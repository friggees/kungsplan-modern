import json,sys
from playwright.sync_api import sync_playwright
base=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:5174'
pages=json.load(open('reference/pages.json',encoding='utf-8'))
with sync_playwright() as p:
 browser=p.chromium.launch()
 page=browser.new_page(viewport={'width':390,'height':844})
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 results=[]
 for item in pages:
  path='/' if item['slug']=='home' else '/'+item['slug']+'/'
  response=page.goto(base+path,wait_until='networkidle')
  page.locator('h1').wait_for()
  broken=page.evaluate('Array.from(document.images).filter(i=>i.complete && !i.naturalWidth).map(i=>i.src)')
  overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth')
  assert response.status==200,(path,response.status)
  assert not broken,(path,broken)
  assert not overflow,(path,'overflow')
  results.append({'path':path,'status':response.status,'heading':page.locator('h1').inner_text(),'mobileOverflow':overflow,'brokenImages':broken})
 page.goto(base,wait_until='networkidle')
 page.get_by_role('button',name='Öppna meny').click()
 page.get_by_role('navigation',name='Mobilmeny').get_by_role('link',name='Prislista',exact=True).click()
 assert page.url.endswith('/prislista/')
 page.get_by_role('dialog').wait_for(state='hidden')
 page.get_by_role('button',name='Betalning och delbetalning',exact=True).click()
 assert page.get_by_text('Du kan betala med kort, Swish',exact=False).is_visible()
 page.set_viewport_size({'width':1440,'height':1000})
 page.goto(base,wait_until='networkidle')
 page.get_by_role('button',name='Utbildningar',exact=True).click()
 page.get_by_role('menuitem',name='Moped & mopedbil',exact=True).click()
 assert page.url.endswith('/mopedkorkort/')
 assert page.get_by_role('link',name='Se kurser & boka').get_attribute('href')=='https://www.trafikskolaonline.se/sv/skola/kungsplan/kurser'
 assert not errors,errors
 print(json.dumps({'base':base,'routes':results,'mobileMenu':'pass','desktopDropdown':'pass','accordion':'pass','bookingDestination':'pass','browserErrors':errors},ensure_ascii=False,indent=2))
 browser.close()
