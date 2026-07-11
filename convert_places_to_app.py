#!/usr/bin/env python3
"""Convert placesdata*.py + place-photos.json (static site) into the Next.js app's
content/places.json, and copy the images into the app's public/places/.
Run from ~/pronite-website: python3 convert_places_to_app.py"""
import json, os, re, shutil, html

SRC = os.path.dirname(os.path.abspath(__file__))
APP = os.path.expanduser("~/Downloads/pronite-app")
IMG_SRC = f"{SRC}/assets/places"
IMG_DST = f"{APP}/public/places"
os.makedirs(IMG_DST, exist_ok=True)

PLACES = []
for m in ("placesdata", "placesdata_b", "placesdata_c", "placesdata_d", "placesdata_e", "placesdata_f", "placesdata_g", "placesdata_h", "placesdata_i"):
    PLACES += __import__(m).POSTS
photos = json.load(open(f"{SRC}/data/place-photos.json"))

def parse_body(h):
    """Turn the HTML body string into ordered blocks for React rendering."""
    blocks = []
    # tokenize by top-level tags in order
    for m in re.finditer(r'<(p|h2|ul)>(.*?)</\1>', h, re.S):
        tag, inner = m.group(1), m.group(2)
        if tag == "ul":
            items = [re.sub(r'<[^>]+>', '', x).strip() for x in re.findall(r'<li>(.*?)</li>', inner, re.S)]
            items = [html.unescape(re.sub(r'\s+', ' ', x)) for x in items if x.strip()]
            blocks.append({"t": "ul", "items": items})
        else:
            text = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', inner)).strip())
            blocks.append({"t": tag, "c": text})
    return blocks

def rel(rec):
    """Map a photo credit record's file path into the app's /places/<file>, copy the image."""
    if not rec:
        return None
    fn = os.path.basename(rec["file"])
    src = f"{IMG_SRC}/{fn}"
    if os.path.exists(src):
        shutil.copy2(src, f"{IMG_DST}/{fn}")
    return {"src": f"/places/{fn}", "artist": rec.get("artist", "Wikimedia Commons"),
            "license": rec.get("license", ""), "source": rec.get("source", "")}

out = []
for p in PLACES:
    ph = photos.get(p["slug"], {})
    out.append({
        "slug": p["slug"],
        "name": p["name"],
        "city": p["city"],
        "region": p["region"],
        "cat": p["cat"],
        "excerpt": p["excerpt"],
        "info": p.get("info", {}),
        "tags": p.get("tags", []),
        "mapQuery": f"{p['name']} {p['city']} India",
        "hero": rel(ph.get("hero")),
        "gallery": [rel(g) for g in ph.get("gallery", []) if g],
        "body": parse_body(p["body"]),
    })

os.makedirs(f"{APP}/content", exist_ok=True)
json.dump(out, open(f"{APP}/content/places.json", "w"), indent=1, ensure_ascii=False)
copied = len(os.listdir(IMG_DST))
print(f"wrote {len(out)} places to app content/places.json; {copied} images in public/places/")
