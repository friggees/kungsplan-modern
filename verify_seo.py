"""Verify raw HTML and browser metadata against the original snapshot."""
import json, pathlib, sys
import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, expect

root = pathlib.Path(__file__).parent
base = sys.argv[1].rstrip('/') if len(sys.argv) > 1 else 'http://127.0.0.1:4187'
entries = json.loads((root/'src/seo-pages.json').read_text(encoding='utf-8'))
results = []
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    for entry in entries:
        url = base + entry['path']
        response = requests.get(url, timeout=30)
        assert response.status_code == 200, (url, response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        assert len(soup.select('title')) == 1 and soup.title.string == entry['title'], url
        assert soup.select_one('link[rel="canonical"]')['href'] == entry['canonical'], url
        expected = {'description': entry['description'], 'robots': 'noindex, follow', **entry['social']}
        for key, value in expected.items():
            nodes = soup.find_all('meta', attrs={'property' if key.startswith('og:') else 'name': key})
            assert len(nodes) == 1 and nodes[0]['content'] == value, (url, key)
        page.goto(url, wait_until='domcontentloaded')
        page.locator('h1').wait_for()
        expect(page).to_have_title(entry['title'])
        assert page.locator('meta[name="description"]').get_attribute('content') == entry['description'], url
        assert page.locator('link[rel="canonical"]').get_attribute('href') == entry['canonical'], url
        # Returning via a React Router link must replace metadata without leftovers.
        page.locator('header a[href="/"]').click()
        page.wait_for_url(base + '/')
        expect(page).to_have_title(entries[0]['title'])
        assert page.locator('meta[name="description"]').count() == 1
        assert page.locator('meta[name="description"]').get_attribute('content') == entries[0]['description']
        assert page.locator('meta[property="og:image"]').count() == (1 if 'og:image' in entries[0]['social'] else 0)
        results.append({'path': entry['path'], 'rawHtml': 'PASS', 'browser': 'PASS', 'navigation': 'PASS'})
    assert not errors, errors
    browser.close()
if 'vercel.app' in base:
    for source, target in [('/hem/', '/'), ('/kontakt/', '/kontakta-oss/')]:
        response = requests.get(base + source, timeout=30, allow_redirects=False)
        assert response.status_code in [301, 308], (source, response.status_code)
        assert response.headers['Location'] in [target, base + target]
    assert requests.get(base + '/seo-test-missing-page/', timeout=30).status_code == 404
    assert 'noindex' in requests.get(base + '/', timeout=30).headers.get('X-Robots-Tag', '')
(root/'reference/seo-verification.json').write_text(json.dumps({'base': base, 'pages': results, 'consoleErrors': errors}, indent=2), encoding='utf-8')
print(f'PASS: {len(results)} pages, exact HTML/browser metadata, navigation cleanup, no browser errors.')
