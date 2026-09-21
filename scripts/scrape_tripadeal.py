"""
scrape_tripadeal.py — turn TripADeal deal pages into tours.json for the globe.

Usage:
    pip install requests beautifulsoup4
    python scrape_tripadeal.py 5836 6363 6380            # specific deal IDs (full parse)
    python scrape_tripadeal.py --listing                 # every tour on the listing, full parse
    python scrape_tripadeal.py --listing --limit 30
    python scrape_tripadeal.py --prices                  # nightly: listing pages only, update price/dates/sale,
                                                         #          full-parse only deals that are new; write changelog
    python scrape_tripadeal.py --prices --full           # weekly: same, but re-parse every deal page

Output: data/tours.json (merged with existing), data/changelog.json (last 60 runs).
Exit codes: 0 ok · 2 safety guard tripped (listing shrank by >50%), nothing written · 3 network failure.

Each deal page has:
  * og:title            "13 Days Japan Discovery | Tour Package"
  * product:price       3999
  * breadcrumb          Tours > Asia > Japan
  * "Dates:" line       27 Nov 2026 - 22 Nov 2027
  * itinerary headers   "Day 4 Tokyo – Mt Fuji – Nagano"
  * overnight lines     "Overnight: Hotel Route Inn Suwa Inter or similar, Nagano Region"
Land days: the "Overnight: hotel, City" line gives the city. Cruise days: the overnight names
the ship, so the day header ("Juneau, Alaska, USA") is used instead; at-sea days keep the
previous port. Consecutive days in one city collapse into a stop with a night count.
Each stop carries the transport mode used to reach it (coach/rail/cruise/flight), detected
from keywords in that day's text.

Be a good citizen: random 2–5 s gaps between requests, retries with backoff, a plain UA.
Check TripADeal's terms before running this at scale; the affiliate feed is the
proper long-term source.
"""
import re, sys, json, time, pathlib, argparse, random, datetime
import requests
from bs4 import BeautifulSoup

BASE = "https://www.tripadeal.com.au"
CACHE = pathlib.Path(".cache"); CACHE.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
      "Accept-Language": "en-AU,en;q=0.9"}
DATA = pathlib.Path(__file__).resolve().parent.parent/"data"
MIN_GAP, MAX_GAP = 2.0, 5.0     # seconds between requests
NO_CACHE = False                 # --prices sets this so listing pages are always fresh
DEP = {"Sydney","Melbourne","Brisbane","Perth","Adelaide","Auckland","Australia","New Zealand","Australia (or New Zealand)"}

# --- gazetteer: extend freely; anything missing falls back to Nominatim ---------------
sys.path.insert(0, str(pathlib.Path(__file__).parent))
try:
    from build_data import G as GAZ
except Exception:
    GAZ = {}
ALIAS = {"Halong Bay":"Ha Long Bay","Ha Long":"Ha Long Bay","Nagano Region":"Nagano","Xi'An":"Xi'an","Xian":"Xi'an","Mount Fuji":"Mt Fuji","Ho Chi Minh":"Ho Chi Minh City","Saigon":"Ho Chi Minh City"}

def get(url, fresh=False):
    key = CACHE / (re.sub(r"[^a-z0-9]+","_",url.lower()) + ".html")
    if key.exists() and not fresh and not NO_CACHE: return key.read_text()
    last = None
    for attempt in range(3):
        try:
            r = requests.get(url, headers=UA, timeout=30)
            if r.status_code in (429, 503): raise requests.HTTPError(f"{r.status_code} for {url}")
            r.raise_for_status()
            key.write_text(r.text); time.sleep(random.uniform(MIN_GAP, MAX_GAP))
            return r.text
        except Exception as e:
            last = e; time.sleep(15 * (attempt + 1))
    raise last

_geo_cache_path = DATA / "places.json"
_geo = json.loads(_geo_cache_path.read_text()) if _geo_cache_path.exists() else {}
def geocode(city, country_hint=""):
    city = ALIAS.get(city, city)
    if city in GAZ: return GAZ[city]
    if city in _geo: return tuple(_geo[city])
    GEO_UA = {"User-Agent": "tour-globe/1.0 (github.com/WesleyDotExe/tour-globe; nightly geocoder)"}
    r = []
    for q in ([f"{city}, {country_hint}"] if country_hint else []) + [city]:
        try:
            resp = requests.get("https://nominatim.openstreetmap.org/search", params={"q":q,"format":"json","limit":1}, headers=GEO_UA, timeout=30)
            r = resp.json() if resp.ok else []
        except Exception: r = []
        time.sleep(1.1)  # Nominatim usage policy: max 1 req/s
        if r: break
    if not r: return None
    ll = (round(float(r[0]["lon"]),2), round(float(r[0]["lat"]),2))
    _geo[city] = ll; _geo_cache_path.write_text(json.dumps(_geo, indent=1))
    return ll

# --- parsing --------------------------------------------------------------------------
def text_of(soup):  # itinerary is plain text with bold overnight lines; flatten
    for br in soup.find_all("br"): br.replace_with("\n")
    return soup.get_text("\n")


GENERIC = re.compile(r"(sightseeing|free day|at leisure|day at|cruising|scenic|tour\b|experience|embark|disembark|in-transit|in transit|arrive|depart|optional|museum|warriors|great wall|grottoes|terracotta|bullet train|&|\bbegin\b|\d+-night|\bfly\b|flight|crossing|transit|equator|canal|airport|cruise port|\band\b|glacier|at sea|day \d)", re.I)
HOTELISH = re.compile(r"(hotel|resort|inn\b|lodge|suites?|plaza|boutique|spa\b|retreat|camp\b|villa|ryokan|guesthouse|apartments?|palace hotel|or similar|by wyndham|by hilton|by marriott|hilton|marriott|sheraton|novotel|ibis|ramada|mercure|hyatt|radisson|holiday inn|best western|crowne|doubletree|courtyard|wyndham)", re.I)
SHIP = re.compile(r"(cruises?'|'s |princess|koningsdam|seas|celebrity|msc|carnival|hurtigruten|ship|onboard|aboard)", re.I)
MODE_RE = [("rail", re.compile(r"(bullet train|high-speed train|rocky mountaineer|rail journey|by train|train to|train ride|railway|shinkansen)", re.I)),
           ("river", re.compile(r"(nile|river cruise|danube|rhine|mekong|yangtze|felucca|riverboat)", re.I)),
           ("cruise", re.compile(r"(cruise|sail |sailing|embark|onboard|aboard|at sea|dock|port of)", re.I)),
           ("flight", re.compile(r"(domestic flight|fly to|flight to|fly from|internal flight|by air)", re.I))]
def mode_of(text):
    for m, rx in MODE_RE:
        if rx.search(text): return m
    return "coach"

HOME = re.compile(r"^(australia|new zealand|australia \(or new zealand\)|home)\b", re.I)

def clean_place(p):
    p = re.sub(r"\s*\(.*?\)", "", p).strip(" .*")
    p = re.sub(r"\s+(Region|Area|National Park|Free Day|Free Morning|Sightseeing|Overnight Cruise|Overnight|Cruise|Day Trip|City Tour|Tour|Stay)$", "", p, flags=re.I).strip()
    p = re.sub(r"\s+(Region|Area|National Park|Overnight Cruise|Overnight|Cruise|Hotel|Airport|Port|Island)$", "", p, flags=re.I).strip()
    return p

def place_from_header(header):
    """'Calgary - Lake Louise - Banff - Canmore' -> Canmore ; 'Juneau, Alaska, USA' -> Juneau ; 'Great Wall of China' -> None"""
    header = header.split(",")[0]
    parts = [clean_place(x) for x in re.split(r"\s[–—-]\s|\s(?:OR|or)\s", header)]
    parts = [x for x in parts if x and not HOME.match(x) and not GENERIC.search(x) and len(x) <= 30]
    return parts[-1] if parts else None

def parse_days(it, country=""):
    """Return (days_detail, stops). days_detail: [{d,title,city,text}], stops: [[city, nights], ...]"""
    blocks = re.split(r"\n\s*(?=Day \d+\s)", "\n" + it)
    days, last_city = [], None
    for b in blocks:
        m = re.match(r"Day (\d+)\s+([^\n]+)\n?(.*)", b.strip(), re.S)
        if not m: continue
        d, header, rest = int(m.group(1)), m.group(2).strip(), m.group(3)
        over = re.search(r"Overnight:\s*([^\n]+)", rest)
        city = None
        if over:
            o = over.group(1).strip(" *")
            if not SHIP.search(o):
                last = clean_place(o.split(",")[-1])
                if last and not HOTELISH.search(last) and len(last) <= 30: city = last
        if not city:
            city = place_from_header(header)
        if not city and over and SHIP.search(over.group(1)):
            city = last_city                        # day at sea: keep the previous port
        body_txt = re.split(r"\n\s*(?:Please note|\*\*Overnight|\*\*Meals|Overnight:|Meals included)", rest.strip(), maxsplit=1)[0]
        body_txt = re.sub(r"\s+", " ", body_txt).strip()
        # first sentence as the one-liner; the full day copy as `detail` (your own site should rewrite this before publishing)
        text = re.split(r"(?<=[.!?])\s", body_txt, maxsplit=1)[0][:220]
        detail = body_txt[:1200]
        meals = (re.search(r"Meals included:\s*([^\n*]+)", rest) or [None, ""])[1].strip()
        hotel = (over.group(1).strip(" *") if over else "")
        optional = "; ".join(m.strip(" *") for m in re.findall(r"\n\s*\*?\*?Optional[^\n]*?:\s*([^\n]+)", rest))[:300]
        mode = mode_of(header + " " + rest[:600])
        days.append(dict(d=d, title=header, city=city, text=text, detail=detail, meals=meals, hotel=hotel, optional=optional, mode=mode))
        if city: last_city = city
    # collapse consecutive days in the same city into stops with night counts
    stops = []
    for x in days:
        if not x["city"]: continue
        if stops and stops[-1][0] == x["city"]: stops[-1][1] += 1
        else: stops.append([x["city"], 1, x["mode"]])
    if stops: stops[-1][1] = max(0, stops[-1][1] - 1)   # last day is a departure, not a night
    return days, stops

def parse_deal(deal_id):
    url = f"{BASE}/deals/{deal_id}"
    html = get(url); soup = BeautifulSoup(html, "html.parser")
    meta = lambda p: (soup.find("meta", property=p) or soup.find("meta", attrs={"name":p}) or {}).get("content","")
    canonical = (soup.find("link", rel="canonical") or {}).get("href", url)
    title = meta("og:title").split("|")[0].strip()
    m = re.match(r"(\d+)(?: or \d+)? Days? (.*)", title)
    days, name = (int(m.group(1)), m.group(2)) if m else (None, title)
    price = int(float(meta("product:price:amount") or 0))
    crumbs = [a.get_text(strip=True) for a in soup.select("a[href*='/destination/']")][:3]
    region = next((c for c in crumbs if c in {"Asia","Europe","Africa","Americas","North America","South America","Pacific","Middle East"}), "")
    if region in {"North America","South America"}: region = "Americas"
    body = text_of(soup)
    dates = (re.search(r"Dates?:\s*([^\n]+)", body) or [None, ""])[1].strip()
    headline = (re.search(re.escape(name) + r"\s*\n+\s*Operated by[^\n]*\n+\s*([^\n]+)", body) or [None, ""])[1].strip()
    save = (re.search(r"SAVE\s+(\$[\d,]+|\d+%)", body) or [None, ""])[1]
    was = re.search(r"WAS\s*~~\$?([\d,]+)~~", body)
    was = int(was.group(1).replace(",","")) if was else None
    kind = "Ocean cruise" if "Cruise" in title or "cruise" in name.lower() else ("Rail" if "Rail" in name else "Guided")
    if re.search(r"\bSmall Group\b", body): kind = "Small group"

    # itinerary: only the first itinerary block (extensions / alternative ships come as "Itinerary 2")
    it = re.split(r"\n\s*Itinerary 2\b", re.split(r"\n\s*## Itinerary\s*\n", body, maxsplit=1)[-1], maxsplit=1)[0]
    it = re.split(r"\n\s*## Important Info", it, maxsplit=1)[0]
    country = crumbs[-1] if crumbs else ""
    # photo gallery: hero images (eager) + lazy-loaded ones (data-src); alt text is the caption
    images, seen = [], set()
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("data-lazy") or img.get("src") or ""
        if "cstad.s3" not in src and "PUBS" not in src: continue
        if "MAP" in src or src in seen: continue
        seen.add(src); images.append(dict(src=src, caption=(img.get("alt") or img.get("title") or "").strip().rstrip(".")))
        if len(images) >= 12: break
    days_detail, stops = parse_days(it, country)
    out = []
    for c in stops:
        ll = geocode(c[0], country)
        if ll: out.append([ALIAS.get(c[0], c[0]), ll[0], ll[1], c[1], "", c[2]])
        else: print(f"  ! could not geocode {c[0]!r} in deal {deal_id}", file=sys.stderr)
    for d in days_detail:
        ll = geocode(d["city"], country) if d["city"] else None
        d["lng"], d["lat"] = (ll if ll else (None, None))

    months = month_range(dates)
    dep = re.search(r"Departure Cities\s*\n+\s*([^\n]+)", body)
    from_city = (dep.group(1).replace("*","").split(",")[0].strip() if dep else "Sydney")
    return dict(id=int(deal_id), name=name, url=canonical, days=days, price=price, was=was, save=save, per="for2" if "for 2" in name.lower() else "pp",
                dates=dates, region=region, type=kind, from_city=from_city, months=months, special=bool(save), special_label="Sale" if save else "",
                ends=0, itinerary="exact" if out else "none", tags=[], headline=headline, days_detail=days_detail, images=images,
                stops=[[from_city, *GAZ.get(from_city,(151.21,-33.87)), 0, "Depart Australia", "flight"]] + out)

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def norm_dates(d): return re.sub(r"\s*[–—-]\s*", " - ", (d or "").strip())
def month_range(dates):
    ds = re.findall(r"(\d{1,2}) (\w{3}) (\d{4})", dates)
    if not ds: return []
    if len(ds) == 1: return [ds[0][1]]
    (_, m1, y1), (_, m2, y2) = ds[0], ds[-1]
    a, b = MONTHS.index(m1) + 12*int(y1), MONTHS.index(m2) + 12*int(y2)
    return [MONTHS[i % 12] for i in range(a, min(b, a+11) + 1)]

def parse_cards(html):
    """Deal cards on a server-rendered TripADeal page (home, /destination/<x>). Returns {id: summary}."""
    soup = BeautifulSoup(html, "html.parser"); out = {}
    for a in soup.select('a[href*="/deals/"]'):
        m = re.search(r"/deals/(\d+)-([a-z0-9-]+)", a.get("href",""))
        if not m: continue
        did, slug = int(m.group(1)), m.group(2)
        txt = re.sub(r"\s+", " ", a.get_text(" ", strip=True))
        if len(txt) < 40: continue                      # nav/footer links, not a card
        if did in out: continue
        tags = set(re.findall(r"\b(Tour|Cruise|Flights|Rail|Hotel)\b", txt))
        kind = "tour" if "Tour" in tags else ("cruise" if "Cruise" in tags else "other")
        save = re.search(r"SAVE\s+(\$[\d,]+|\d+%)", txt, re.I)
        was = re.search(r"(?:WAS|Valued (?:up )?to)\s*~*\$?\s?([\d,]{3,7})", txt, re.I)
        clean = re.sub(r"(SAVE|WAS|Valued (?:up )?to)\s*~*\$?\s?[\d,]+", " ", txt, flags=re.I)
        clean = re.sub(r"[\d,]+\s*PTS", " ", clean)                     # Qantas points figures
        amounts = [int(x.replace(",","")) for x in re.findall(r"\$\s?([\d,]{3,7})", clean)]
        amounts = [x for x in amounts if x >= 100]
        dates = re.search(r"Dates?:\s*(\d{1,2} \w{3}(?: \d{4})?\s*[-–]\s*\d{1,2} \w{3} \d{4}|\d{1,2} \w{3} \d{4})", txt)
        days = re.search(r"(\d+)(?:, \d+)*(?: or \d+)? days", txt, re.I)
        out[did] = dict(id=did, slug=slug, kind=kind, price=min(amounts) if amounts else None,
                        was=int(was.group(1).replace(",","")) if was else None, save=save.group(1) if save else "",
                        dates=norm_dates(dates.group(1)) if dates else "", days=int(days.group(1)) if days else None,
                        per="for2" if re.search(r"(?<!booking )for 2 (?:people|persons)|\bfor 2\b(?! people)(?<!booking for 2)|per couple|Deals? for 2", re.sub(r"when booking for 2", "", txt, flags=re.I), re.I) else "pp",
                        trip_only=bool(re.search(r"Trip Only option", txt, re.I)))
    return out

def listing(limit=None, max_pages=80):
    """Walk every destination page (server-rendered, unlike /searchresults), biggest first.
    Returns an ordered dict id -> card summary (tours & cruise packages only)."""
    index = get(f"{BASE}/destination", fresh=True)
    dests = []
    for m in re.finditer(r'href="(?:https://www\.tripadeal\.com\.au)?/destination/([a-z0-9-]+)"[^>]*>(.*?)</a>', index, re.S):
        slug, inner = m.group(1), re.sub(r"<[^>]+>", " ", m.group(2))
        n = re.search(r"(\d+)\s*DEALS?", inner, re.I)
        if n: dests.append((int(n.group(1)), slug))
    dests = sorted(dict((s, n) for n, s in dests).items(), key=lambda x: -x[1])   # slug -> count, biggest first
    if not dests: dests = [("asia",0),("europe",0),("north-america",0),("south-america",0),("africa",0),("oceania",0),("middle-east",0)]
    found = {}
    for slug, n in dests[:max_pages]:
        before = len(found)
        try: cards = parse_cards(get(f"{BASE}/destination/{slug}", fresh=True))
        except Exception as e: print(f"  ! {slug}: {e}", file=sys.stderr); continue
        for did, c in cards.items():
            if c["kind"] != "other" and did not in found: found[did] = c
        added = len(found) - before; print(f"  /destination/{slug}: {len(cards)} cards, {added} new (total {len(found)})")
        if limit and len(found) >= limit: break
    if limit: found = dict(list(found.items())[:limit])
    return found

def listing_ids(limit=None):
    return [str(i) for i in listing(limit)]

# ---------------------------------------------------------------- nightly price mode ----
def load_tours():
    p = DATA/"tours.json"
    return json.load(open(p)) if p.exists() else []

def diff_tours(old, new):
    o = {t["id"]: t for t in old}; n = {t["id"]: t for t in new}
    ev = []
    for i in n.keys() - o.keys(): ev.append(dict(type="new", id=i, name=n[i]["name"], price=n[i]["price"]))
    for i in o.keys() - n.keys(): ev.append(dict(type="removed", id=i, name=o[i]["name"]))
    for i in n.keys() & o.keys():
        a, b = o[i], n[i]
        if a.get("price") != b.get("price") and b.get("price"):
            ev.append(dict(type="price_down" if b["price"] < (a.get("price") or 0) else "price_up", id=i, name=b["name"], **{"from": a.get("price"), "to": b["price"]}))
        if bool(a.get("special")) != bool(b.get("special")):
            ev.append(dict(type="sale_started" if b.get("special") else "sale_ended", id=i, name=b["name"]))
        if norm_dates(a.get("dates")) != norm_dates(b.get("dates")) and b.get("dates"):
            ev.append(dict(type="dates_changed", id=i, name=b["name"], **{"from": a.get("dates"), "to": b["dates"]}))
    return ev

def write_changelog(events, mode, counts):
    p = DATA/"changelog.json"
    log = json.load(open(p)) if p.exists() else []
    log.append(dict(run=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), mode=mode, **counts, events=events))
    json.dump(log[-60:], open(p,"w"), ensure_ascii=False, indent=1)

def featured_ids():
    """Deal IDs in homepage order — what TripADeal is featuring today."""
    try: return list(parse_cards(get(f"{BASE}/", fresh=True)))
    except Exception as e: print(f"  ! homepage: {e}", file=sys.stderr); return []

def price_run(full=False, limit=None):
    """Nightly: listing only. Update price/was/save/dates/per on known tours, full-parse new ones
    (and everything, if full=True), drop tours no longer listed, write changelog. Guard against a collapsed listing."""
    global NO_CACHE; NO_CACHE = bool(full)   # --full refetches every deal page; otherwise cached pages are reused
    old = load_tours(); old_by = {t["id"]: t for t in old}
    live = listing(limit)
    if old and not limit and len(live) < 0.5 * len(old):
        print(f"SAFETY GUARD: listing returned {len(live)} deals vs {len(old)} yesterday; not writing.", file=sys.stderr); sys.exit(2)
    new_ids = [i for i in live if i not in old_by]
    to_parse = list(live) if full else new_ids
    print(f"listing: {len(live)} tours & cruise packages · new: {len(new_ids)} · full-parsing: {len(to_parse)}")
    tours = []
    for i, card in live.items():
        if i in to_parse:
            try: t = parse_deal(i)
            except Exception as e:
                print(f"  ! parse failed for {i}: {e}", file=sys.stderr)
                if i in old_by: t = dict(old_by[i])
                else: continue
        else:
            t = dict(old_by[i])
        # listing card is the freshest source for the commercial fields
        for k in ("price", "was", "save", "dates", "per", "days"):
            if card.get(k) not in (None, ""): t[k] = card[k]
        t["special"] = bool(t.get("save")); t["special_label"] = t.get("special_label") or ("Sale" if t["special"] else "")
        t["featured"] = t.get("featured", 0)  # homepage order is set by --featured below
        t["last_seen"] = datetime.date.today().isoformat()
        tours.append(t)
    feat = featured_ids()
    for t in tours: t["featured"] = feat.index(t["id"]) + 1 if t["id"] in feat else 0
    events = diff_tours(old, tours)
    json.dump(tours, open(DATA/"tours.json","w"), ensure_ascii=False, indent=1)
    write_changelog(events, "full" if full else "prices", dict(listed=len(live), new=len(new_ids), parsed=len(to_parse)))
    print(f"wrote {len(tours)} tours; {len(events)} change events")
    for e in events[:30]: print("  ", e)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("ids", nargs="*"); ap.add_argument("--listing", action="store_true"); ap.add_argument("--limit", type=int)
    ap.add_argument("--prices", action="store_true", help="nightly mode: listing pages only, full-parse new deals"); ap.add_argument("--full", action="store_true", help="with --prices: re-parse every deal")
    a = ap.parse_args()
    if a.prices:
        try: price_run(full=a.full, limit=a.limit)
        except requests.RequestException as e:
            print(f"network failure: {e}", file=sys.stderr); sys.exit(3)
        sys.exit(0)
    ids = listing_ids(a.limit) if a.listing else a.ids
    tours = []
    for i in ids:
        print("deal", i); tours.append(parse_deal(i))
    out = pathlib.Path(__file__).resolve().parent.parent/"data"/"tours.json"
    json.dump(tours, open(out,"w"), ensure_ascii=False, indent=1)
    print(f"wrote {len(tours)} tours to {out}")
