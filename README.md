# Tour Globe

A destinations-first map of TripADeal's current tour deals. Country dots at world level, headline cities as you zoom in, and a full route with transport modes, day-by-day itinerary and photo gallery when you open a tour.

**Live page:** enable GitHub Pages (Settings → Pages → *Deploy from a branch* → `main`, `/ (root)`) and it serves `index.html`.

## Layout

| Path | What it is |
|---|---|
| `index.html` | The built site. Self-contained: world outlines and tour data are embedded, so it works from a double-click. |
| `scripts/template.html` | Page source with `/*WORLD_JSON*/`, `/*TOURS_JSON*/`, `/*COUNTRY_JSON*/` placeholders. |
| `scripts/build_data.py` | Curated deal data (prices, dates, sale flags, destinations) + city gazetteer → `data/tours.json`. |
| `scripts/details_extra.py` | Day-by-day itineraries, galleries and exact stop lists written from each deal page. |
| `scripts/scrape_tripadeal.py` | Scraper that parses deal pages into the same JSON shape (routes, modes, day text, meals, hotels, galleries). |
| `scripts/build.py` | Assembles `index.html` from the template and `data/`. |
| `scripts/smoke.js` | Headless jsdom smoke test of the page logic. |
| `data/` | `tours.json`, `countries_pts.json` (country centroids), `world.json` (simplified Natural Earth 50m outlines, antimeridian-safe). |

## Rebuild

```bash
python3 scripts/build_data.py   # regenerates data/tours.json from the curated Python
python3 scripts/build.py        # writes index.html
```

The GitHub Action does the same on every push that touches `scripts/` or `data/`.

## Refresh from TripADeal

```bash
pip install -r requirements.txt
python3 scripts/scrape_tripadeal.py --listing     # every tour on the listing page → data/tours.json
python3 scripts/build.py
```

The scraper rate-limits itself to one request a second and caches pages in `.cache/`. Check TripADeal's terms before running it at scale; the affiliate feed is the proper long-term source. The `detail` text it captures is TripADeal's own copy and should be rewritten before publishing.

## Test

```bash
npm install jsdom && node scripts/smoke.js
```

## Notes

- Photos load from TripADeal's image CDN; the gallery hides itself when offline.
- The home city is detected from IP (ipwho.is, then ipapi.co) and snapped to the nearest TripADeal departure city; the dropdown overrides it.
- Cruise legs are bent through water using the embedded outlines; the Alaska fjords are the one place the simplified coastline can't resolve.
