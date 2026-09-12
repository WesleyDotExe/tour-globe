"""
scrape_tripadeal.py — turn TripADeal deal pages into tours.json for the globe.

Usage:
    pip install requests beautifulsoup4
    python scrape_tripadeal.py 5836 6363 6380            # specific deal IDs
    python scrape_tripadeal.py --listing                 # every tour on the search results page
    python scrape_tripadeal.py --listing --limit 30

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

Be a good citizen: one request per second, cache pages, identify yourself in the UA.
Check TripADeal's terms before running this at scale; the affiliate feed is the
proper long-term source.
"""
import re, sys, json, time, pathlib, argparse
import requests
from bs4 import BeautifulSoup

BASE = "https://www.tripadeal.com.au"
CACHE = pathlib.Path(".cache"); CACHE.mkdir(exist_ok=True)
UA = {"User-Agent": "tour-globe-prototype/0.1 (personal project; contact: you@example.com)"}
DEP = {"Sydney","Melbourne","Brisbane","Perth","Adelaide","Auckland","Australia","New Zealand","Australia (or New Zealand)"}

# --- gazetteer: extend freely; anything missing falls back to Nominatim ---------------
sys.path.insert(0, str(pathlib.Path(__file__).parent))
try:
    from build_data import G as GAZ
except Exception:
    GAZ = {}
ALIAS = {"Nagano Region":"Nagano","Xi'An":"Xi'an","Xian":"Xi'an","Mount Fuji":"Mt Fuji","Ho Chi Minh":"Ho Chi Minh City","Saigon":"Ho Chi Minh City"}

def get(url):
    key = CACHE / (re.sub(r"[^a-z0-9]+","_",url.lower()) + ".html")
    if key.exists(): return key.read_text()
    r = requests.get(url, headers=UA, timeout=30); r.raise_for_status()
    key.write_text(r.text); time.sleep(1.0)
    return r.text

_geo_cache_path = CACHE / "geocode.json"
_geo = json.loads(_geo_cache_path.read_text()) if _geo_cache_path.exists() else {}
def geocode(city, country_hint=""):
    city = ALIAS.get(city, city)
    if city in GAZ: return GAZ[city]
    if city in _geo: return tuple(_geo[city])
    q = f"{city}, {country_hint}" if country_hint else city
    r = requests.get("https://nominatim.openstreetmap.org/search", params={"q":q,"format":"json","limit":1}, headers=UA, timeout=30).json()
    time.sleep(1.1)  # Nominatim usage policy
    if not r: return None
    ll = (round(float(r[0]["lon"]),2), round(float(r[0]["lat"]),2))
    _geo[city] = ll; _geo_cache_path.write_text(json.dumps(_geo, indent=1))
    return ll

# --- parsing --------------------------------------------------------------------------
def text_of(soup):  # itinerary is plain text with bold overnight lines; flatten
    for br in soup.find_all("br"): br.replace_with("\n")
    return soup.get_text("\n")


GENERIC = re.compile(r"(sightseeing|free day|at leisure|day at|cruising|scenic|tour|experience|embark|disembark|in-transit|in transit|arrive|depart|optional|museum|warriors|great wall|grottoes|terracotta|bullet train|&)", re.I)
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
    p = re.sub(r"\s+(Region|Area|National Park|Free Day|Free Morning|Sightseeing)$", "", p, flags=re.I).strip()
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
                city = clean_place(o.split(",")[-1])
        if not city:
            city = place_from_header(header)
        if not city and over and SHIP.search(over.group(1)):
            city = last_city                        # day at sea: keep the previous port
        body_txt = re.split(r"\n\s*(?:Please note|\*\*Overnight|\*\*Meals|Overnight:|Meals included)", rest.strip(), 1)[0]
        body_txt = re.sub(r"\s+", " ", body_txt).strip()
        # first sentence as the one-liner; the full day copy as `detail` (your own site should rewrite this before publishing)
        text = re.split(r"(?<=[.!?])\s", body_txt, 1)[0][:220]
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
    it = re.split(r"\n\s*Itinerary 2\b", re.split(r"\n\s*## Itinerary\s*\n", body, 1)[-1], 1)[0]
    it = re.split(r"\n\s*## Important Info", it, 1)[0]
    days_detail, stops = parse_days(it, country := (crumbs[-1] if crumbs else ""))
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
def month_range(dates):
    ds = re.findall(r"(\d{1,2}) (\w{3}) (\d{4})", dates)
    if not ds: return []
    if len(ds) == 1: return [ds[0][1]]
    (_, m1, y1), (_, m2, y2) = ds[0], ds[-1]
    a, b = MONTHS.index(m1) + 12*int(y1), MONTHS.index(m2) + 12*int(y2)
    return [MONTHS[i % 12] for i in range(a, min(b, a+11) + 1)]

def listing_ids(limit=None):
    html = get(f"{BASE}/searchresults?categories=Tours")
    ids = list(dict.fromkeys(re.findall(r"/deals/(\d+)-", html)))
    return ids[:limit] if limit else ids

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("ids", nargs="*"); ap.add_argument("--listing", action="store_true"); ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    ids = listing_ids(a.limit) if a.listing else a.ids
    tours = []
    for i in ids:
        print("deal", i); tours.append(parse_deal(i))
    out = pathlib.Path(__file__).resolve().parent.parent/"data"/"tours.json"
    json.dump(tours, open(out,"w"), ensure_ascii=False, indent=1)
    print(f"wrote {len(tours)} tours to {out}")
