#!/usr/bin/env python3
"""Fetch free-licensed photos for each place from Wikimedia Commons (with attribution).
Saves images to assets/places/ and credits to data/place-photos.json.
Idempotent: skips places already fetched (unless --force). Run: python3 fetch_place_photos.py"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
IMGDIR = f"{ROOT}/assets/places"
os.makedirs(IMGDIR, exist_ok=True)
CREDITS_PATH = f"{ROOT}/data/place-photos.json"
UA = "ProniteTravelGuide/1.0 (https://pronite.in; proniteexperience@gmail.com)"
FORCE = "--force" in sys.argv

PLACES = []
for m in ("placesdata", "placesdata_b", "placesdata_c", "placesdata_d", "placesdata_e", "placesdata_f", "placesdata_g", "placesdata_h", "placesdata_i", "placesdata_j", "placesdata_k"):
    try:
        PLACES += __import__(m).POSTS
    except ModuleNotFoundError:
        pass

credits = {}
if os.path.exists(CREDITS_PATH):
    credits = json.load(open(CREDITS_PATH))

BAD = re.compile(r'(map|locator|coat|flag|logo|icon|seal|diagram|plan_of|\.svg|\.pdf|\.tif|panorama_of_india)', re.I)

def _get(url, timeout, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=timeout)
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))  # backoff on rate-limit / transient errors
    raise last

def api(params):
    params.update({"action": "query", "format": "json"})
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    with _get(url, 40) as r:
        return json.load(r)

def clean(s):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).strip()

def search_images(query, want):
    """Return list of dicts: {title, thumburl, artist, license, source} up to `want`."""
    d = api({"generator": "search", "gsrsearch": f"filetype:bitmap {query}",
             "gsrnamespace": "6", "gsrlimit": str(want + 8),
             "prop": "imageinfo", "iiprop": "url|extmetadata", "iiurlwidth": "1280"})
    pages = list(d.get("query", {}).get("pages", {}).values())
    pages.sort(key=lambda p: p.get("index", 99))
    out = []
    for p in pages:
        title = p.get("title", "")
        if BAD.search(title):
            continue
        ii = (p.get("imageinfo") or [{}])[0]
        thumb = ii.get("thumburl")
        if not thumb:
            continue
        em = ii.get("extmetadata", {})
        out.append({
            "title": title,
            "thumburl": thumb,
            "artist": clean(em.get("Artist", {}).get("value", "")) or "Wikimedia Commons",
            "license": clean(em.get("LicenseShortName", {}).get("value", "")) or "See source",
            "source": ii.get("descriptionurl", ""),
        })
        if len(out) >= want:
            break
    return out

def download(url, path):
    with _get(url, 60) as r:
        data = r.read()
    open(path, "wb").write(data)
    return len(data)

def main():
    done = ok = 0
    for pl in PLACES:
        slug = pl["slug"]
        if slug in credits and not FORCE:
            done += 1
            continue
        gwant = pl.get("gallery", 3)
        try:
            imgs = search_images(pl["query"], 1 + gwant)
        except Exception as e:
            print(f"  ! {slug}: search failed ({e})")
            continue
        if not imgs:
            print(f"  ! {slug}: no images found for '{pl['query']}'")
            continue
        entry = {"hero": None, "gallery": []}
        for i, im in enumerate(imgs):
            fn = f"{slug}.jpg" if i == 0 else f"{slug}-g{i}.jpg"
            try:
                sz = download(im["thumburl"], f"{IMGDIR}/{fn}")
            except Exception as e:
                print(f"  ! {slug}: download failed ({e})")
                continue
            rec = {"file": f"assets/places/{fn}", "artist": im["artist"],
                   "license": im["license"], "source": im["source"]}
            if i == 0:
                entry["hero"] = rec
            else:
                entry["gallery"].append(rec)
        if entry["hero"]:
            credits[slug] = entry
            ok += 1
            print(f"  ✓ {slug}: hero + {len(entry['gallery'])} gallery")
        json.dump(credits, open(CREDITS_PATH, "w"), indent=1, ensure_ascii=False)
        time.sleep(0.4)
    print(f"done. fetched {ok} new, {done} already had photos, {len(credits)} total.")

if __name__ == "__main__":
    main()
