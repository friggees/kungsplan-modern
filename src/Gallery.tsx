import { useRef, useState } from 'react';
import { Dialog } from 'radix-ui';
import { ArrowLeft, ArrowRight, ArrowUpRight, Camera, Plus, X } from 'lucide-react';

// Same eight posts and order as the original site's gallery, retrieved 2026-09-22.
const photos = [
  { id: 1, name: 'Adrian', title: 'Körkortet är klart!' },
  { id: 2, name: 'Simon', title: 'Friheten börjar här.' },
  { id: 3, name: 'Alaa', title: 'Ett välförtjänt körkort.' },
  { id: 4, name: 'Mopedbil', title: 'Fler vägar till frihet.' },
  { id: 5, name: 'Agnes', title: 'Redo för nya vägar.' },
  { id: 6, name: 'Neo', title: 'Vi ses på vägarna.' },
  { id: 7, name: 'Anna', title: 'Njut av friheten.' },
  { id: 8, name: 'Ardrin', title: 'I mål med körkortet.' },
];

export default function Gallery() {
  const [selected, setSelected] = useState(0);
  const openedFrom = useRef<HTMLButtonElement | null>(null);
  const photo = photos[selected];
  const step = (direction: number) => setSelected(current => (current + direction + photos.length) % photos.length);

  return (
    <section className="section gallery" id="galleri" aria-labelledby="gallery-title">
      <div className="wrap">
        <div className="section-heading">
          <div>
            <span className="eyebrow">SMÅ ÖGONBLICK. STOR FRIHET.</span>
            <h2 id="gallery-title">Några av våra nöjda<br className="desktop-break"/> körkortsinnehavare.</h2>
          </div>
          <p>Glädjen när allt faller på plats.<br/>Här börjar nästa kapitel.</p>
        </div>
        <Dialog.Root>
          <div className="gallery-grid">
            {photos.map((item, index) => (
              <Dialog.Trigger asChild key={item.id}>
                <button className="gallery-card" onClick={event => { openedFrom.current = event.currentTarget; setSelected(index); }} aria-label={`Förstora bild: ${item.name}`}>
                  <span className="gallery-photo">
                    <img src={`/images/gallery/${item.id}.jpg`} alt={item.id === 4 ? 'Kungsplan Trafikskolas mopedbil' : `${item.name} firar sitt körkort hos Kungsplan Trafikskola`} width="1440" height="1440" loading="lazy" decoding="async"/>
                    <span className="gallery-zoom" aria-hidden="true"><Plus size={18}/></span>
                  </span>
                  <span className="gallery-caption"><strong>{item.name}</strong><span>{item.title}</span></span>
                </button>
              </Dialog.Trigger>
            ))}
          </div>
          <Dialog.Portal>
            <Dialog.Overlay className="gallery-overlay"/>
            <Dialog.Content className="gallery-dialog" onCloseAutoFocus={event => { event.preventDefault(); openedFrom.current?.focus(); }} onKeyDown={event => {
              if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
                event.preventDefault();
                step(event.key === 'ArrowLeft' ? -1 : 1);
              }
            }}>
              <Dialog.Close className="gallery-close" aria-label="Stäng bild"><X size={22}/></Dialog.Close>
              <img className="gallery-full-image" src={`/images/gallery/${photo.id}.jpg`} alt={photo.id === 4 ? 'Kungsplan Trafikskolas mopedbil' : `${photo.name} firar sitt körkort hos Kungsplan Trafikskola`}/>
              <div className="gallery-dialog-footer">
                <div aria-live="polite" aria-atomic="true">
                  <Dialog.Title>{photo.name}</Dialog.Title>
                  <Dialog.Description>{photo.title} · Bild {selected + 1} av {photos.length}</Dialog.Description>
                </div>
                <div className="gallery-controls">
                  <button onClick={() => step(-1)} aria-label="Föregående bild"><ArrowLeft size={20}/></button>
                  <button onClick={() => step(1)} aria-label="Nästa bild"><ArrowRight size={20}/></button>
                </div>
              </div>
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>
        <div className="gallery-bottom">
          <span>Fler körkort. Fler leenden.</span>
          <a className="text-link" href="https://www.instagram.com/kungsplantrafikskola/" target="_blank" rel="noopener noreferrer"><Camera size={17}/> Följ vår vardag på Instagram <ArrowUpRight size={16}/></a>
        </div>
      </div>
    </section>
  );
}

