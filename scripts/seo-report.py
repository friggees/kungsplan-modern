import csv, html, json, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
source = json.loads((root/'reference/seo-original.json').read_text(encoding='utf-8'))
before = {r['path']: r for r in json.loads((root/'reference/seo-demo-before.json').read_text(encoding='utf-8'))}
entries = json.loads((root/'src/seo-pages.json').read_text(encoding='utf-8'))
original = {r['path']: r for r in source}
intro = '''# SEO-jämförelse – Kungsplan Trafikskola

Granskad 23 september 2026. Källa: https://kungsplantrafikskola.se/ och dess sitemap samt interna länkar. Demo: https://kungsplan-modern.vercel.app/

15 sidor har matchats sida för sida. Två äldre adresser, /hem/ och /kontakt/, leder till / respektive /kontakta-oss/ med permanent omdirigering (originalet använder 301, demon 308). Inventeringen omfattar alla sidor i publicerad sitemap samt HTML-sidor hittade via interna länkar, inte eventuella olistade eller privata sidor.

## Genomfört

- Exakt samma SEO-titlar och metabeskrivningar som originalet, inklusive originalets formuleringar och eventuella fel.
- Canonical samt befintlig Open Graph- och Twitter-metadata har kopierats. Canonical och delningsadresser pekar på kundens riktiga domän.
- Varje sida får sin egen metadata direkt i HTML-svaret och vid navigering i React. Tidigare fick alla samma beskrivning med trasiga svenska tecken.
- Demosidan har noindex i både HTML och HTTP-header. Detta är avsiktligt annorlunda än originalets index-inställning.
- Saknade adresser ger HTTP 404 i stället för att returnera startsidans HTML med 200.

## Originaltexter som SEO-byrån bör granska

- BE/B96: titeln innehåller ”handledarkurs”, och beskrivningen handlar om introduktionsutbildning för 450 kr. Det verkar inte beskriva sidans BE/B96-innehåll.
- Introduktionsutbildning: beskrivningen anger 450 kr. Priset behöver bekräftas mot aktuellt erbjudande.
- Studenterbjudande: titeln lovar 20 % rabatt, medan beskrivningen är samma som på körkortsgarantin. Bekräfta rabattens omfattning och villkor.
- Moped: beskrivningen säger ”Kör från 14 år och 9 månader” och att prov ingår. Kunden bör bekräfta formuleringen och vad som faktiskt ingår. Titeln har också teckenkombinationen ”–|”.
- Kontakt har endast ”KONTAKTA OSS” som beskrivning. Prislistans beskrivning är mycket kort; Om oss och drogpolicyn har avbrutna meningar.
- /startsida/ och / visar samma startsida i demon men har originalets olika titlar och canonical-adresser. Byrån bör besluta om /startsida/ ska omdirigeras vid lansering.

## Återstår inför byte av den riktiga webbplatsen

De synliga H1-rubrikerna och brödtexterna är fortfarande demosidans moderniserade texter. SEO-titel och H1 är olika saker; fullständig jämförelse finns nedan. Originalet saknar H1 på flera sidor och har tre H1 på teorisidan, vilket inte har kopierats som struktur.

Originalets Rank Math JSON-LD har inventerats och sparats i reference/seo-original.json. Det innehåller bland annat LocalBusiness/Organization, WebSite, WebPage, Article, Person och VideoObject. Dessa objekt har inte kopierats blint eftersom de bland annat beskriver originalets författare, publiceringsdatum och videoinnehåll. Relevant företags- och siddata behöver anpassas till den slutliga webbplatsen.

Sidinnehållet renderas fortfarande av React; den här ändringen gör metadata statisk, inte hela sidinnehållet. Bedöm förrendering/serverrendering inför skarp lansering. Delningsbildernas adresser pekar fortfarande på originalets /wp-content/uploads/ och måste bevaras eller flyttas vid plattformsbyte.

Vid skarp lansering: ta bort demo-noindex både i vercel.json, index.html, src/seo.ts och scripts/build-seo.mjs; lägg till en sitemap med de slutliga canonical-adresserna och dess hänvisning i robots.txt; granska rubriker/innehåll, strukturerade data och eventuella ytterligare gamla adresser med SEO-byrån. Search Console, Analytics, backlinks och sökordsplaceringar har inte granskats eftersom detta är en offentlig sidinventering.

## Sida för sida
'''
parts = [intro]
for e in entries:
    old, src = before[e['path']], original[e['path']]
    parts.append(f"### {e['path']}\n\n- Original / demo efter: **{e['title']}**\n- Demo före: {old['title']}\n- Metabeskrivning (original / demo efter): {e['description']}\n- Canonical: {e['canonical']}\n- Originalets H1: {' / '.join(src['h1']) or '(saknas)'}\n- Demosidans H1: {' / '.join(old['h1'])}\n")
text = '\n'.join(parts)
(root/'SEO-jamforelse.md').write_text(text, encoding='utf-8')
sections=[]
for block in text.split('\n\n'):
    if block.startswith('### '): sections.append('<h3>'+html.escape(block[4:])+'</h3>')
    elif block.startswith('## '): sections.append('<h2>'+html.escape(block[3:])+'</h2>')
    elif block.startswith('# '): sections.append('<h1>'+html.escape(block[2:])+'</h1>')
    elif block.startswith('- '): sections.append('<ul>'+''.join('<li>'+html.escape(line[2:]).replace('**','')+'</li>' for line in block.splitlines() if line.startswith('- '))+'</ul>')
    else: sections.append('<p>'+html.escape(block)+'</p>')
document='<!doctype html><html lang="sv"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>SEO-jämförelse – Kungsplan</title><style>body{font:16px/1.65 system-ui;color:#183548;max-width:960px;margin:40px auto;padding:0 24px}h1,h2,h3{line-height:1.25}h2{border-top:1px solid #ccdbe1;padding-top:28px;margin-top:38px}h3{color:#087b93}li{margin:8px 0;overflow-wrap:anywhere}@media print{h3{break-after:avoid}}</style>'+''.join(sections)+'</html>'
(root/'SEO-jamforelse.html').write_text(document,encoding='utf-8')
with (root/'SEO-jamforelse.csv').open('w', encoding='utf-8-sig', newline='') as f:
    writer=csv.writer(f,delimiter=';')
    writer.writerow(['Sida','Originaltitel = demo efter','Demo före','Originalbeskrivning = demo efter','Canonical','Original H1','Demo H1'])
    for e in entries:
        writer.writerow([e['path'],e['title'],before[e['path']]['title'],e['description'],e['canonical'],' / '.join(original[e['path']]['h1']),' / '.join(before[e['path']]['h1'])])
print('Created SEO-jamforelse.md, .html and .csv for 15 pages.')
