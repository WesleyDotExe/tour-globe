"""Country lookup against data/world.json (Natural Earth outlines; properties.n = name).

The scraper uses country_at(lng, lat) to tag each stop with the country it falls in
(so tours get a `countries` list for the world-level dots), and this module also
generates data/countries_pts.json — one representative point per country for those dots.

Run directly to (re)generate the points file:
    python3 scripts/world_geo.py
"""
import json, pathlib
DATA = pathlib.Path(__file__).resolve().parent.parent / "data"
_world = json.loads((DATA / "world.json").read_text())

# tidy a couple of Natural Earth names to TripADeal's house style
DISPLAY = {"United States of America": "USA", "Turkey": "Türkiye"}
def _name(f):
    n = f["properties"]["n"]
    return DISPLAY.get(n, n)

def _ext_rings(geom):
    """Exterior rings only (holes don't matter for a country-membership test)."""
    if geom["type"] == "Polygon":
        yield geom["coordinates"][0]
    elif geom["type"] == "MultiPolygon":
        for poly in geom["coordinates"]:
            yield poly[0]

def _in_ring(x, y, ring):
    inside = False; n = len(ring); j = n - 1
    for i in range(n):
        xi, yi = ring[i]; xj, yj = ring[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside

def _ring_area(ring):
    a = 0.0; n = len(ring)
    for i in range(n):
        x0, y0 = ring[i]; x1, y1 = ring[(i + 1) % n]
        a += x0 * y1 - x1 * y0
    return abs(a) / 2

def _ring_centroid(ring):
    a = cx = cy = 0.0; n = len(ring)
    for i in range(n):
        x0, y0 = ring[i]; x1, y1 = ring[(i + 1) % n]
        cross = x0 * y1 - x1 * y0
        a += cross; cx += (x0 + x1) * cross; cy += (y0 + y1) * cross
    if a == 0:
        xs = [p[0] for p in ring]; ys = [p[1] for p in ring]
        return [round(sum(xs) / n, 2), round(sum(ys) / n, 2)]
    a *= 0.5
    return [round(cx / (6 * a), 2), round(cy / (6 * a), 2)]

# precompute (name, exterior rings, bbox) per country for fast lookup
_COUNTRIES = []
for _f in _world["features"]:
    _rings = list(_ext_rings(_f["geometry"]))
    if not _rings: continue
    _xs = [p[0] for r in _rings for p in r]; _ys = [p[1] for r in _rings for p in r]
    _COUNTRIES.append((_name(_f), _rings, (min(_xs), min(_ys), max(_xs), max(_ys))))

def country_at(lng, lat):
    """Name of the country whose polygon contains (lng, lat), or None."""
    for name, rings, (x0, y0, x1, y1) in _COUNTRIES:
        if lng < x0 or lng > x1 or lat < y0 or lat > y1: continue
        for ring in rings:
            if _in_ring(lng, lat, ring): return name
    return None

def _bbox_dist2(lng, lat, bbox):
    x0, y0, x1, y1 = bbox
    dx = 0 if x0 <= lng <= x1 else min(abs(lng - x0), abs(lng - x1))
    dy = 0 if y0 <= lat <= y1 else min(abs(lat - y0), abs(lat - y1))
    return dx * dx + dy * dy

def nearest_country(lng, lat):
    """Country with the nearest boundary vertex — a fallback for small islands and
    coastal points the simplified 50m coastline doesn't enclose. Bounding boxes are
    checked nearest-first so only the closest few countries are scanned in full."""
    best, bestd = None, float("inf")
    for name, rings, bbox in sorted(_COUNTRIES, key=lambda c: _bbox_dist2(lng, lat, c[2])):
        if _bbox_dist2(lng, lat, bbox) >= bestd: break   # sorted: everything after is farther
        for ring in rings:
            for x, y in ring:
                d = (x - lng) ** 2 + (y - lat) ** 2
                if d < bestd: bestd, best = d, name
    return best

def country_of(lng, lat):
    """country_at with the nearest-country fallback."""
    return country_at(lng, lat) or nearest_country(lng, lat)

def centroids():
    """One representative point per country (area-centroid of its largest landmass)."""
    out = {}
    for name, rings, _bbox in _COUNTRIES:
        pt = _ring_centroid(max(rings, key=_ring_area))
        out.setdefault(name, pt)
    return out

if __name__ == "__main__":
    pts = centroids()
    json.dump(pts, open(DATA / "countries_pts.json", "w"), ensure_ascii=False)
    print(f"wrote {len(pts)} country points to data/countries_pts.json")
