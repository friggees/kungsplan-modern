# Kungsplan Trafikskola

Moderniserad React-webbplats med Vite, TypeScript, Tailwind och shadcn/ui (Radix). Originalets logotyp, blå/turkosa identitet och bilder används. Bildfilerna ligger lokalt i `public/images`.

## Utveckling

`npm install`, därefter `npm run dev`. Produktionsbygge: `npm run build`. Lint: `npm run lint`.

## Innehåll och sidstruktur

Samtliga 15 adresser från originalets page-sitemap.xml den 21 september 2026 finns representerade. `/startsida/` visar samma moderniserade startsida som `/`. `/hem/` fungerar också som kompatibilitetsadress. Utbildningstexter finns i `src/data.ts`, sidkomponenter i `src/Site.tsx`, styling i `src/site.css`.

Bokning, elevanmälan och e-handel länkar till skolans befintliga Trafikskola Online. Kontakt sker via telefon, e-post och kartlänk. Ingen ny betalningshantering eller formulärbackend finns. Webbplatsen sätter inga egna analys- eller marknadsföringscookies.

## Källmaterial

Hämtat från https://kungsplantrafikskola.se/ med undersidor. Sidinventering och originaltexter finns i `reference/pages.json`. Originalets gamla kampanjer från 2023/2024 har inte lyfts fram. Prislistan från 17 september 2026 används för gemensamma priser där originalets undersidor har olika uppgifter. Studentpaket kommer från den separata studentsidan. Intensivkursens administrationsavgift på 600 kr finns beskriven. Körkortsgarantins originaltext innehåller motstridiga inkluderingsvillkor; den moderniserade sidan hänvisar därför till personligt prisförslag och aktuellt avtal.

## Verifiering

`python verify.py [bas-url]` kräver Python Playwright och Chromium. Kontrollerar alla 15 adresser, huvudrubriker, bildfel, mobilöverflöde, mobilmeny, desktopmeny, prisvillkorens accordion och bokningslänk. Manuella skärmbilder har också granskats i agent-browser.

## Publicering

Vercel-projekt: `kungsplan-modern`, team `albin-bergvalls-projects`. Kör `npx vercel deploy --prod --yes` från projektkatalogen. Vercel bygger med `npm run build`. Routing definieras i `vercel.json`.

## SEO-matchning 23 september 2026

Originalets titlar, metabeskrivningar, canonical och sociala metadata finns i `src/seo-pages.json`. Bygget genererar 15 separata HTML-dokument med dessa värden via `scripts/build-seo.mjs`. `src/seo.ts` håller samma metadata uppdaterad vid klientnavigering. `/hem/` och `/kontakt/` omdirigeras permanent till `/` respektive `/kontakta-oss/`. Okända adresser ger HTTP 404.

Detta är fortfarande en demo med `noindex` i både HTML och HTTP-header. Läs lanseringspunkterna i `SEO-jamforelse.md` innan projektet kopplas till kundens riktiga domän. H1 och brödtexter är demosidans texter; originalets JSON-LD är inventerad men inte migrerad.

`python verify_seo.py https://kungsplan-modern.vercel.app` kontrollerar samtliga sidors HTML- och webbläsarmetadata, klientnavigering, omdirigeringar, 404 och noindex-header. Inventering: `python audit_seo.py`. Rapport: `python scripts/seo-report.py` (HTML, Markdown och CSV).
