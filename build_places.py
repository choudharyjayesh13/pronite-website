#!/usr/bin/env python3
"""Builds the Places to Visit guide: places/index.html + places/<slug>.html + homepage teaser.
Photos & credits come from data/place-photos.json (run fetch_place_photos.py first).
Also regenerates the site sitemap (home + blog + places + events). Run: python3 build_places.py"""
import json, html, os, re, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{ROOT}/places", exist_ok=True)

PLACES = []
for m in ("placesdata", "placesdata_b", "placesdata_c", "placesdata_d", "placesdata_e", "placesdata_f", "placesdata_g", "placesdata_h", "placesdata_i"):
    try:
        PLACES += __import__(m).POSTS
    except ModuleNotFoundError:
        pass

photos = json.load(open(f"{ROOT}/data/place-photos.json")) if os.path.exists(f"{ROOT}/data/place-photos.json") else {}

CAT_GRAD = {
  "Palace & Fort": "linear-gradient(135deg,#2a0d12,#7a2a1e 60%,#ff7a3d)",
  "Lake & Ghat":   "linear-gradient(135deg,#04171a,#0b4a56 60%,#28c3d6)",
  "Temple":        "linear-gradient(135deg,#241206,#7a3d10 60%,#ffb347)",
  "Garden & Park": "linear-gradient(135deg,#07160c,#124a2a 60%,#2fd07a)",
  "Museum":        "linear-gradient(135deg,#140b26,#3a1d63 60%,#7b46ff)",
  "Viewpoint":     "linear-gradient(135deg,#210a1e,#6a1256 60%,#ff4fb0)",
  "Wildlife":      "linear-gradient(135deg,#0a1607,#2f4a12 60%,#8fd02f)",
  "Desert":        "linear-gradient(135deg,#241a06,#7a5a10 60%,#ffcf47)",
  "Heritage Site": "linear-gradient(135deg,#1a0f22,#4a2d5a 60%,#c46bff)",
}
DEF_GRAD = "linear-gradient(135deg,#14141f,#26263a)"

def hero_of(slug):
    p = photos.get(slug, {})
    return p.get("hero")

def credit_line(rec, prefix=""):
    if not rec:
        return ""
    art = html.escape(rec.get("artist", "Wikimedia Commons"))
    lic = html.escape(rec.get("license", ""))
    src = rec.get("source", "")
    label = f"Photo: {art}"
    if lic:
        label += f" · {lic}"
    label += " — via Wikimedia Commons"
    if src:
        return f'<a href="{src}" target="_blank" rel="noopener">{label}</a>'
    return label

def card(p, prefix=""):
    hero = hero_of(p["slug"])
    grad = CAT_GRAD.get(p["cat"], DEF_GRAD)
    if hero:
        media = f'<img src="{prefix}{hero["file"]}" alt="{html.escape(p["name"])}, {html.escape(p["city"])}" loading="lazy">'
    else:
        media = f'<div class="swatch" style="background:{grad}"></div>'
    return f'''<a class="pcard" data-cat="{p['cat']}" data-region="{p['region']}" href="{prefix}places/{p['slug']}.html">
  <div class="pcard-media">{media}</div>
  <div class="pcard-body">
    <span class="pcard-cat">{p['cat']}</span>
    <b>{html.escape(p['name'])}</b>
    <p>{html.escape(p['excerpt'])}</p>
    <em>{html.escape(p['city'])} · {html.escape(p['region'])}</em>
  </div>
</a>'''

SHELL = open(f"{ROOT}/place_shell.html", encoding="utf-8").read()

QF_KEYS = [("timings", "Timings"), ("entry", "Entry"), ("best", "Best time"), ("duration", "Duration")]
ROW_KEYS = [("timings", "Timings"), ("entry", "Entry fee"), ("best", "Best time to visit"),
            ("duration", "Time needed"), ("reach", "How to reach")]

# order for related: keep declaration order
for i, p in enumerate(PLACES):
    slug = p["slug"]
    ph = photos.get(slug, {})
    hero = ph.get("hero")
    grad = CAT_GRAD.get(p["cat"], DEF_GRAD)
    hero_img = f'../{hero["file"]}' if hero else ""
    hero_css = f"../{hero['file']}" if hero else ""
    info = p.get("info", {})
    qf = "".join(f'<div class="qfi"><span>{lab}</span><b>{html.escape(info.get(k,"—"))}</b></div>'
                 for k, lab in QF_KEYS if info.get(k))
    rows = "".join(f'<div class="row"><span>{lab}</span><b>{html.escape(info.get(k,"—"))}</b></div>'
                   for k, lab in ROW_KEYS if info.get(k))
    tags = "".join(f'<span class="tag">#{t}</span>' for t in p.get("tags", []))
    # gallery
    gitems = []
    for g in ph.get("gallery", []):
        gitems.append(f'<div class="gitem"><img src="../{g["file"]}" alt="{html.escape(p["name"])}" loading="lazy"><em>{credit_line(g)}</em></div>')
    gallery = "\n".join(gitems) or '<p style="color:#6f6c7b;font-size:.85rem">More photos coming soon.</p>'
    # related: same region first, then same category
    same_r = [q for q in PLACES if q["region"] == p["region"] and q["slug"] != slug]
    same_c = [q for q in PLACES if q["cat"] == p["cat"] and q["slug"] != slug and q not in same_r]
    rel = (same_r + same_c)[:4]
    rcards = ""
    for r in rel:
        rh = hero_of(r["slug"])
        rimg = f'<img src="../{rh["file"]}" alt="{html.escape(r["name"])}" loading="lazy">' if rh else f'<div style="height:110px;background:{CAT_GRAD.get(r["cat"],DEF_GRAD)}"></div>'
        rcards += f'<a class="rc" href="{r["slug"]}.html">{rimg}<div><span>{r["cat"]}</span><b>{html.escape(r["name"])}</b></div></a>'
    mapq = urllib.parse.quote(f"{p['name']} {p['city']} India")
    kws = ", ".join(p.get("tags", []) + [p["name"], p["city"], p["region"], "India", "places to visit", "travel guide"])
    og = f"https://www.pronite.in/{hero['file']}" if hero else "https://www.pronite.in/assets/icon-512.png"
    page = (SHELL
        .replace("{HERO_IMG}", hero_css or "")
        .replace("{NAME}", html.escape(p["name"]))
        .replace("{CITY}", html.escape(p["city"]))
        .replace("{REGION}", html.escape(p["region"]))
        .replace("{CAT}", p["cat"])
        .replace("{EXCERPT}", html.escape(p["excerpt"]))
        .replace("{HERO_CREDIT}", credit_line(hero))
        .replace("{QUICKFACTS}", qf)
        .replace("{INFO_ROWS}", rows)
        .replace("{BODY}", p["body"])
        .replace("{TAGS}", tags)
        .replace("{GALLERY}", gallery)
        .replace("{RELATED}", rcards)
        .replace("{MAPQ}", mapq)
        .replace("{SLUG}", slug)
        .replace("{OG_IMG}", og)
        .replace("{KEYWORDS}", html.escape(kws)))
    open(f"{ROOT}/places/{slug}.html", "w", encoding="utf-8").write(page)

# ---- index page ----
cats = []
for p in PLACES:
    if p["cat"] not in cats:
        cats.append(p["cat"])
regions = []
for p in PLACES:
    if p["region"] not in regions:
        regions.append(p["region"])
catchips = '<button class="chip active" data-f="all">All</button>' + "".join(
    f'<button class="chip" data-f="{c}">{c}</button>' for c in cats)
cards_html = "\n".join(card(p, prefix="../") for p in PLACES)

INDEX = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Places to Visit in India — {len(PLACES)} Attractions, Forts, Beaches, Food & Nightlife | Pronite</title>
<meta name="description" content="A complete guide to the best places to visit across India — {len(PLACES)} forts, palaces, lakes, temples, beaches, hill stations, plus the most happening streets, food and nightlife in Delhi, Mumbai, Jaipur, Goa, Varanasi and beyond. Photos, timings, entry fees and how to reach.">
<meta name="keywords" content="places to visit India, India travel guide, must visit places, happening places India, food streets, nightlife India, Delhi Mumbai Goa Jaipur Varanasi, Pronite">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.pronite.in/places/">
<meta property="og:title" content="Places to Visit in India — Pronite Travel Guide">
<meta property="og:description" content="{len(PLACES)} of India's best sights, beaches, food streets and nightlife — with photos, timings and travel info.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.pronite.in/assets/places/city-palace-udaipur.jpg">
<meta name="theme-color" content="#07070b">
<link rel="icon" type="image/png" href="../assets/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Krona+One&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#07070b;--panel:#0e0e15;--line:#1e1e2a;--ink:#f2efe6;--dim:#9d9aa8;--coral:#ff5c47;--amber:#ffb347}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--ink);font-family:'Inter',-apple-system,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}}
.krona{{font-family:'Krona One',sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 22px}}
nav{{position:sticky;top:0;background:rgba(7,7,11,.9);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);z-index:60}}
nav .wrap{{display:flex;justify-content:space-between;align-items:center;height:60px}}
.logo{{font-size:.95rem;letter-spacing:.28em;text-decoration:none;color:var(--ink)}}
.logo em{{color:var(--coral);font-style:normal}}
nav a.back{{color:var(--dim);text-decoration:none;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}}
.top{{padding:66px 0 26px;border-bottom:1px solid var(--line);background:radial-gradient(120% 150% at 82% -20%,rgba(255,92,71,.16),transparent 55%)}}
.eyebrow{{font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;color:var(--amber);font-weight:700}}
.top h1{{font-family:'Krona One';font-size:clamp(1.9rem,5.2vw,3.1rem);line-height:1.12;margin:16px 0 12px;text-wrap:balance}}
.top p{{color:var(--dim);max-width:640px;font-size:1.05rem}}
.filters{{display:flex;gap:9px;flex-wrap:wrap;padding:22px 0 4px;position:sticky;top:60px;background:var(--bg);z-index:40}}
.chip{{background:var(--panel);border:1px solid var(--line);color:var(--dim);border-radius:100px;padding:9px 16px;font-size:.78rem;font-family:inherit;cursor:pointer;transition:.2s;white-space:nowrap}}
.chip:hover{{color:var(--ink);border-color:#33333f}}
.chip.active{{background:linear-gradient(100deg,var(--coral),#ff7a3d);color:#0a0508;border-color:transparent;font-weight:700}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:24px 0 70px}}
@media(max-width:900px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:600px){{.grid{{grid-template-columns:1fr}}}}
.pcard{{display:flex;flex-direction:column;text-decoration:none;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--panel);transition:.22s}}
.pcard:hover{{transform:translateY(-4px);border-color:var(--coral)}}
.pcard-media{{aspect-ratio:16/10;overflow:hidden}}
.pcard-media img{{width:100%;height:100%;object-fit:cover;display:block;transition:.35s}}
.pcard:hover .pcard-media img{{transform:scale(1.05)}}
.swatch{{width:100%;height:100%}}
.pcard-body{{padding:16px 18px 20px;display:flex;flex-direction:column;flex:1}}
.pcard-cat{{font-size:.64rem;letter-spacing:.15em;text-transform:uppercase;color:var(--amber);font-weight:700}}
.pcard-body b{{font-family:'Krona One';font-size:.95rem;line-height:1.35;margin:9px 0 8px;color:var(--ink)}}
.pcard-body p{{color:var(--dim);font-size:.85rem;line-height:1.55;flex:1}}
.pcard-body em{{margin-top:12px;font-style:normal;font-size:.72rem;letter-spacing:.04em;color:#6f6c7b}}
.empty{{display:none;color:var(--dim);padding:30px 0 80px;text-align:center}}
footer{{border-top:1px solid var(--line);padding:34px 0;color:#5d5a68;font-size:.8rem;background:var(--panel)}}
footer .wrap{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}}
footer a{{color:#8b8894;text-decoration:none}}
</style>
</head>
<body>
<nav><div class="wrap">
  <a class="logo krona" href="../index.html">PRO<em>NITE</em></a>
  <a class="back" href="../index.html">← Home</a>
</div></nav>
<header class="top"><div class="wrap">
  <span class="eyebrow">Places to Visit</span>
  <h1>Explore India</h1>
  <p>{len(PLACES)} of India's most spectacular sights — forts, palaces, lakes, temples, beaches and hill stations, plus the most happening streets, food and nightlife from Delhi to Goa to Varanasi. Real photos, timings, entry fees and how to get there.</p>
</div></header>
<div class="wrap">
  <div class="filters">{catchips}</div>
  <div class="grid" id="grid">
{cards_html}
  </div>
  <div class="empty" id="empty">Nothing in this category yet.</div>
</div>
<footer><div class="wrap">
  <span>© 2026 Pronite · A JD Group company · Udaipur, Rajasthan</span>
  <span><a href="../index.html">Home</a> · <a href="../blog/index.html">Journal</a> · <a href="../index.html#join">Join free</a></span>
</div></footer>
<script>
const chips=document.querySelectorAll('.chip'),cards=document.querySelectorAll('.pcard'),empty=document.getElementById('empty');
chips.forEach(c=>c.addEventListener('click',()=>{{
  chips.forEach(x=>x.classList.remove('active'));c.classList.add('active');
  const f=c.dataset.f;let n=0;
  cards.forEach(card=>{{const ok=f==='all'||card.dataset.cat===f;card.style.display=ok?'':'none';if(ok)n++;}});
  empty.style.display=n?'none':'block';
}}));
</script>
</body>
</html>'''
open(f"{ROOT}/places/index.html", "w", encoding="utf-8").write(INDEX)

# ---- homepage teaser (6 marquee picks) + count ----
PICK_SLUGS = ["taj-mahal-agra", "gateway-of-india-mumbai", "golden-temple-amritsar",
              "city-palace-udaipur", "hampi", "baga-calangute-beach-goa"]
_by_slug = {p["slug"]: p for p in PLACES}
picks = [_by_slug[s] for s in PICK_SLUGS if s in _by_slug]
picks = picks or PLACES[:6]
teaser = "\n".join(card(p, prefix="") for p in picks)
open(f"{ROOT}/data/places-teaser.html", "w", encoding="utf-8").write(teaser)
open(f"{ROOT}/data/place-count.txt", "w").write(str(len(PLACES)))

# ---- complete sitemap (home + blog + places + events + policies) ----
BASE = "https://www.pronite.in"
BUILD = "2026-07-11"
urls = [(f"{BASE}/", BUILD, "1.0"), (f"{BASE}/blog/", BUILD, "0.9"), (f"{BASE}/places/", BUILD, "0.9")]
for p in PLACES:
    urls.append((f"{BASE}/places/{p['slug']}.html", BUILD, "0.7"))
try:
    import blogdata, blogdata_b, blogdata_c, blogdata_d, blogdata_e
    BP = blogdata.POSTS + blogdata_b.POSTS + blogdata_c.POSTS + blogdata_d.POSTS + blogdata_e.POSTS
    for b in BP:
        urls.append((f"{BASE}/blog/{b['slug']}.html", b["date"], "0.6"))
except Exception:
    pass
try:
    for path in json.load(open(f"{ROOT}/data/event-links.json")).values():
        urls.append((f"{BASE}/{path}", BUILD, "0.6"))
except Exception:
    pass
for pg in ("privacy.html", "refunds.html"):
    urls.append((f"{BASE}/{pg}", "2026-01-01", "0.3"))
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, mod, pr in urls:
    sm.append(f"  <url><loc>{loc}</loc><lastmod>{mod}</lastmod><priority>{pr}</priority></url>")
sm.append("</urlset>")
open(f"{ROOT}/sitemap.xml", "w", encoding="utf-8").write("\n".join(sm))
open(f"{ROOT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")

print(f"built {len(PLACES)} place pages + index + teaser; sitemap {len(urls)} urls")
