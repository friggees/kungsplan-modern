# SEO-jämförelse – Kungsplan Trafikskola

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

### /

- Original / demo efter: **Kungsplan Trafikskola Karlskrona, ta körkort på vår körskola**
- Demo före: Din trafikskola i Karlskrona | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): På Kungsplan Trafikskola tar vi hänsyn till varje elevs unika behov. ✔️Ta ditt körkort på vår körskola i Karlskrona på 1-2 veckor med vår intensivkurs.
- Canonical: https://kungsplantrafikskola.se/
- Originalets H1: Välkommen till Kungsplans trafikskola
- Demosidans H1: Vi utbildarframtidens förare.

### /alkohol-drogpolicy/

- Original / demo efter: **Alkohol- & drogpolicy | Kungsplan Trafikskola**
- Demo före: Alkohol- & drogpolicy | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Inom förarutbildningen utgör nykterhet och drogfrihet grundläggande pelare. Vårt åtagande på trafikskolan sträcker sig bortom att endast försäkra
- Canonical: https://kungsplantrafikskola.se/alkohol-drogpolicy/
- Originalets H1: (saknas)
- Demosidans H1: Trygghet börjar med ansvar.

### /be-b96-bilslap/

- Original / demo efter: **BE/B96-bil+släp/handledarkurs körkort | Kungsplan Trafikskola**
- Demo före: Bil + släp · BE / B96 | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Introduktionsutbildningen är en grundläggande kurs som handlar om att förbereda eleven & handledaren inför privat övningskörning. ✔️ 450 kr →
- Canonical: https://kungsplantrafikskola.se/be-b96-bilslap/
- Originalets H1: BE/B96-bil+släp Behörighet
- Demosidans H1: Ta med dig lite mer.

### /halkbanan/

- Original / demo efter: **Boka riskutbildning 2 Karlskrona på Kungsplan Trafikskola**
- Demo före: Halkbanan · Riskutbildning del 2 | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Den här kursen fokuserar på att ge elever praktisk erfarenhet av olika riskfyllda situationer som kan uppstå när du kör bil. ✔️ Boka idag →
- Canonical: https://kungsplantrafikskola.se/halkbanan/
- Originalets H1: (saknas)
- Demosidans H1: Lär känna bilens gränser.

### /intensivkurs-korkort/

- Original / demo efter: **Intensivkurs körkort Karlskrona | Kungsplan Trafikskola**
- Demo före: Intensivkurs i Karlskrona | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): För dig som behöver ta körkortet snabbt är vår intensivkurs ett bra alternativ. Ta ditt körkort på vår trafikskola i Karlskrona på bara 1-2 veckor!
- Canonical: https://kungsplantrafikskola.se/intensivkurs-korkort/
- Originalets H1: Intensivkurs körkort Karlskrona
- Demosidans H1: Mer fokus. Närmare körkortet.

### /introduktionsutbildning/

- Original / demo efter: **Introduktionsutbildning/handledarkurs körkort | Kungsplan Trafikskola**
- Demo före: Introduktionsutbildning · Handledarkurs | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Introduktionsutbildningen är en grundläggande kurs som handlar om att förbereda eleven & handledaren inför privat övningskörning. ✔️ 450 kr →
- Canonical: https://kungsplantrafikskola.se/introduktionsutbildning/
- Originalets H1: Introduktionsutbildning
- Demosidans H1: En trygg start. Tillsammans.

### /kontakta-oss/

- Original / demo efter: **Kontakta oss | Kungsplan Trafikskola**
- Demo före: Kontakta oss | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): KONTAKTA OSS
- Canonical: https://kungsplantrafikskola.se/kontakta-oss/
- Originalets H1: (saknas)
- Demosidans H1: Vi finns här för dig.

### /korkortsgaranti/

- Original / demo efter: **Körkortsgaranti | Ta ditt körkort med fastpris i Karlskrona**
- Demo före: Personbil · B-körkort | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Du som elev kan välja körkortsgaranti hos oss, var kostnadsmedveten och ta ditt körkort med ett fast pris. ✔️ Enkelt, bekvämt och prisvärt! →
- Canonical: https://kungsplantrafikskola.se/korkortsgaranti/
- Originalets H1: Utbildning för personbil
- Demosidans H1: Ditt körkort. I din takt.

### /mopedkorkort/

- Original / demo efter: **Mopedkörkort Karlskrona –| Kungsplan Trafikskola**
- Demo före: Moped & mopedbil · AM | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Få ditt mopedkörkort i Karlskrona för EU-moped klass 1. Kör från 14 år och 9 månader. Teori, praktik, synundersökning och prov ingår. Boka idag!
- Canonical: https://kungsplantrafikskola.se/mopedkorkort/
- Originalets H1: Mopedkörkort Karlskrona
- Demosidans H1: Din första smak av frihet.

### /om-oss/

- Original / demo efter: **Om oss | Kungsplan Trafikskola**
- Demo före: Om Kungsplan Trafikskola | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Vi är en grupp dedikerade och erfarna körskollärare som är angelägna om att hjälpa våra elever att bli säkra och självsäkra förare. Med års erfarenhet av
- Canonical: https://kungsplantrafikskola.se/om-oss/
- Originalets H1: (saknas)
- Demosidans H1: Människorna bakom din körglädje.

### /prislista/

- Original / demo efter: **Prislista | Kungsplan Trafikskola**
- Demo före: Priser & paket | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Just nu: Kampanjpris på våra körkortspaket & körlektioner - 
- Canonical: https://kungsplantrafikskola.se/prislista/
- Originalets H1: (saknas)
- Demosidans H1: Din investering i frihet.

### /riskettan/

- Original / demo efter: **Riskettan Karlskrona | Boka med Kungsplan Trafikskola**
- Demo före: Riskutbildning · Del 1 | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Riskutbildning 1 - kvalitetsutbildning med Kungsplan Trafikskola. Erfarna lärare, praktiska insikter och kvalitet i fokus ✔️ Boka riskettan nu →
- Canonical: https://kungsplantrafikskola.se/riskettan/
- Originalets H1: (saknas)
- Demosidans H1: Förstå riskerna. Kör tryggare.

### /startsida/

- Original / demo efter: **Startsida | Kungsplan Trafikskola**
- Demo före: Din trafikskola i Karlskrona | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Kungsplan Trafikskola är en körskola som erbjuder gedigna utbildningar i Karlskrona – självklart till ett bra pris.
- Canonical: https://kungsplantrafikskola.se/startsida/
- Originalets H1: Välkommen till Kungsplans trafikskola
- Demosidans H1: Vi utbildarframtidens förare.

### /studenterbjudande-mecenat/

- Original / demo efter: **Studenterbjudande | Ta ditt körkort med 20% rabatt för studenter**
- Demo före: Studenterbjudande | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Du som elev kan välja körkortsgaranti hos oss, var kostnadsmedveten och ta ditt körkort med ett fast pris. ✔️ Enkelt, bekvämt och prisvärt! →
- Canonical: https://kungsplantrafikskola.se/studenterbjudande-mecenat/
- Originalets H1: Ta körkortet billigare som student
- Demosidans H1: Mer körkort. Mindre studentbudget.

### /teorihjalp/

- Original / demo efter: **Teorihjälp körkort Karlskrona - Kungsplan Trafikskola**
- Demo före: Teorihjälp | Kungsplan Trafikskola
- Metabeskrivning (original / demo efter): Ta körkortet i Karlskrona med Kungsplan Trafikskola. Få effektiv teorihjälp och praktiska körlektioner med bil som tar dig i mål. ✔️ Boka idag →
- Canonical: https://kungsplantrafikskola.se/teorihjalp/
- Originalets H1: Kungsplan Trafikskola – Din bästa vän på vägen till körkortet / Teorihjälp körkort Karlskrona / Teoriundervisning med lärare
- Demosidans H1: Teori som blir begriplig.
