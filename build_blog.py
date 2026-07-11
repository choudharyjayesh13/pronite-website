#!/usr/bin/env python3
"""Builds the Pronite blog: blog/index.html + blog/<slug>.html pages + homepage teaser.
Content lives in blogdata.py (POSTS). Run: python3 build_blog.py"""
import re, html, os, json

# Content is split across blogdata*.py modules so batches can be added independently.
POSTS = []
for _mod in ("blogdata", "blogdata_b", "blogdata_c", "blogdata_d", "blogdata_e"):
    try:
        POSTS += __import__(_mod).POSTS
    except ModuleNotFoundError:
        pass

ROOT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{ROOT}/blog", exist_ok=True)
posters = json.load(open(f"{ROOT}/data/posters.json"))

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# category -> (hero gradient, short label used on cards)
CATS = {
  "Pronite Recap": "linear-gradient(135deg,#2a0d12,#6a1f22 55%,#ff5c47)",
  "City Guide":    "linear-gradient(135deg,#140b26,#3a1d63 55%,#7b46ff)",
  "Scene Report":  "linear-gradient(135deg,#241206,#7a3d10 55%,#ffb347)",
  "Genre":         "linear-gradient(135deg,#04171a,#0b4a56 55%,#28c3d6)",
  "Festival":      "linear-gradient(135deg,#210a1e,#6a1256 55%,#ff4fb0)",
  "Playbook":      "linear-gradient(135deg,#07160c,#124a2a 55%,#2fd07a)",
  "Upcoming":      "linear-gradient(135deg,#2a0d12,#8a2b1a 55%,#ff7a3d)",
}
DEFAULT_GRAD = "linear-gradient(135deg,#14141f,#26263a)"

def nice_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m)]} {y}"

def read_time(body):
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    return max(2, round(words / 200))

def og_for(p):
    if p.get("img"):
        return f"https://www.pronite.in/{p['img']}"
    return "https://www.pronite.in/assets/icon-512.png"

def card(p, prefix=""):
    grad = CATS.get(p["cat"], DEFAULT_GRAD)
    if p.get("img"):
        media = f'<img src="{prefix}{p["img"]}" alt="{html.escape(p["title"])}" loading="lazy">'
    else:
        media = f'<div class="swatch" style="background:{grad}"><span class="krona">PRO<em>NITE</em></span></div>'
    city = f' · {html.escape(p["city"])}' if p.get("city") else ""
    return f'''<a class="pcard" data-cat="{p['cat']}" href="{prefix}blog/{p['slug']}.html">
  <div class="pcard-media">{media}</div>
  <div class="pcard-body">
    <span class="pcard-cat">{p['cat']}</span>
    <b>{html.escape(p['title'])}</b>
    <p>{html.escape(p['excerpt'])}</p>
    <em>{nice_date(p['date'])}{city}</em>
  </div>
</a>'''

SHELL = open(f"{ROOT}/blog_shell.html", encoding="utf-8").read()
posts = sorted(POSTS, key=lambda x: x["date"], reverse=True)

# ---- individual post pages ----
for i, p in enumerate(posts):
    grad = CATS.get(p["cat"], DEFAULT_GRAD)
    citychip = f'<span class="dot"></span><span>{html.escape(p["city"])}</span>' if p.get("city") else ""
    tags = "".join(f'<span class="tag">#{t}</span>' for t in p.get("tags", []))
    # related: same category first, then fill with nearest
    same = [q for q in posts if q["cat"] == p["cat"] and q["slug"] != p["slug"]]
    others = [q for q in posts if q["cat"] != p["cat"] and q["slug"] != p["slug"]]
    rel = (same + others)[:4]
    related = "".join(
        f'<a class="rc" href="{r["slug"]}.html"><span>{r["cat"]}</span><b>{html.escape(r["title"])}</b></a>'
        for r in rel)
    kws = ", ".join(p.get("tags", []) + [p.get("city", ""), "Pronite", "India nightlife"])
    page = (SHELL
        .replace("{HERO_STYLE}", grad)
        .replace("{TITLE}", html.escape(p["title"]))
        .replace("{DESC}", html.escape(p["excerpt"]))
        .replace("{CAT}", p["cat"])
        .replace("{DATE}", nice_date(p["date"]))
        .replace("{ISO}", p["date"])
        .replace("{READ}", str(read_time(p["body"])))
        .replace("{SLUG}", p["slug"])
        .replace("{OG_IMG}", og_for(p))
        .replace("{KEYWORDS}", html.escape(kws))
        .replace("{CITYCHIP}", citychip)
        .replace("{TAGS}", tags)
        .replace("{RELATED}", related)
        .replace("{BODY}", p["body"]))
    open(f"{ROOT}/blog/{p['slug']}.html", "w", encoding="utf-8").write(page)

# ---- blog index ----
cats_present = [c for c in CATS if any(p["cat"] == c for p in posts)]
chips = '<button class="chip active" data-f="all">All stories</button>' + "".join(
    f'<button class="chip" data-f="{c}">{c}</button>' for c in cats_present)
cards_html = "\n".join(card(p, prefix="../") for p in posts)

INDEX = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Pronite Journal — India Nightlife, Parties & Festival Stories</title>
<meta name="description" content="Stories from India's dancefloors: party recaps, city nightlife guides, festival previews and the culture behind the music. {len(posts)} stories and counting, updated through 2026.">
<meta name="keywords" content="India nightlife blog, party blog India, festival guide India, Goa nightlife, Udaipur pool party, techno India, Holi party, NYE party, Pronite">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.pronite.in/blog/">
<meta property="og:title" content="The Pronite Journal — India Nightlife & Party Stories">
<meta property="og:description" content="Party recaps, city nightlife guides and festival previews from across India.">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.pronite.in/assets/posters/biggest-bollywood-nite-3-0.jpg">
<meta name="theme-color" content="#07070b">
<link rel="icon" type="image/png" href="../assets/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Krona+One&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#07070b;--panel:#0e0e15;--line:#1e1e2a;--ink:#f2efe6;--dim:#9d9aa8;--coral:#ff5c47;--amber:#ffb347}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--bg);color:var(--ink);font-family:'Inter',-apple-system,sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}}
.krona{{font-family:'Krona One',sans-serif}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 22px}}
nav{{position:sticky;top:0;background:rgba(7,7,11,.9);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);z-index:60}}
nav .wrap{{display:flex;justify-content:space-between;align-items:center;height:60px}}
.logo{{font-size:.95rem;letter-spacing:.28em;text-decoration:none;color:var(--ink)}}
.logo em{{color:var(--coral);font-style:normal}}
nav a.back{{color:var(--dim);text-decoration:none;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}}
nav a.back:hover{{color:var(--ink)}}
.top{{padding:66px 0 30px;border-bottom:1px solid var(--line);background:radial-gradient(120% 140% at 80% -20%,rgba(255,92,71,.16),transparent 55%)}}
.eyebrow{{font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;color:var(--amber);font-weight:700}}
.top h1{{font-family:'Krona One';font-size:clamp(1.9rem,5.4vw,3.2rem);line-height:1.12;margin:16px 0 12px;text-wrap:balance}}
.top p{{color:var(--dim);max-width:600px;font-size:1.05rem}}
.filters{{display:flex;gap:10px;flex-wrap:wrap;padding:26px 0 4px;position:sticky;top:60px;background:var(--bg);z-index:40}}
.chip{{background:var(--panel);border:1px solid var(--line);color:var(--dim);border-radius:100px;padding:9px 18px;font-size:.8rem;font-family:inherit;cursor:pointer;transition:.2s;white-space:nowrap}}
.chip:hover{{color:var(--ink);border-color:#33333f}}
.chip.active{{background:linear-gradient(100deg,var(--coral),#ff7a3d);color:#0a0508;border-color:transparent;font-weight:700}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:24px 0 70px}}
@media(max-width:900px){{.grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:600px){{.grid{{grid-template-columns:1fr}}}}
.pcard{{display:flex;flex-direction:column;text-decoration:none;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--panel);transition:.22s}}
.pcard:hover{{transform:translateY(-4px);border-color:var(--coral)}}
.pcard-media{{aspect-ratio:16/10;overflow:hidden}}
.pcard-media img{{width:100%;height:100%;object-fit:cover;display:block}}
.swatch{{width:100%;height:100%;display:flex;align-items:center;justify-content:center}}
.swatch span{{letter-spacing:.3em;font-size:1rem;color:rgba(255,255,255,.92)}}
.swatch em{{color:#0a0508;font-style:normal;-webkit-text-stroke:.4px rgba(255,255,255,.8)}}
.pcard-body{{padding:17px 18px 20px;display:flex;flex-direction:column;flex:1}}
.pcard-cat{{font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--amber);font-weight:700}}
.pcard-body b{{font-family:'Krona One';font-size:.98rem;line-height:1.35;margin:9px 0 8px;color:var(--ink)}}
.pcard-body p{{color:var(--dim);font-size:.86rem;line-height:1.55;flex:1}}
.pcard-body em{{margin-top:13px;font-style:normal;font-size:.74rem;letter-spacing:.05em;color:#6f6c7b}}
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
  <span class="eyebrow">The Pronite Journal</span>
  <h1>Stories from India's dancefloors.</h1>
  <p>Party recaps, city-by-city nightlife guides, festival previews and the culture behind the music — from Goa's beaches to Udaipur's lakeside. {len(posts)} stories and growing.</p>
</div></header>
<div class="wrap">
  <div class="filters">{chips}</div>
  <div class="grid" id="grid">
{cards_html}
  </div>
  <div class="empty" id="empty">No stories in this category yet — check back soon.</div>
</div>
<footer><div class="wrap">
  <span>© 2026 Pronite · A JD Group company · Udaipur, Rajasthan</span>
  <span><a href="../index.html">Home</a> · <a href="../index.html#join">Join free</a> · <a href="../privacy.html">Privacy</a></span>
</div></footer>
<script>
const chips=document.querySelectorAll('.chip'),cards=document.querySelectorAll('.pcard'),empty=document.getElementById('empty');
chips.forEach(c=>c.addEventListener('click',()=>{{
  chips.forEach(x=>x.classList.remove('active'));c.classList.add('active');
  const f=c.dataset.f;let shown=0;
  cards.forEach(card=>{{const ok=f==='all'||card.dataset.cat===f;card.style.display=ok?'':'none';if(ok)shown++;}});
  empty.style.display=shown?'none':'block';
}}));
</script>
</body>
</html>'''
open(f"{ROOT}/blog/index.html", "w", encoding="utf-8").write(INDEX)

# ---- homepage teaser (latest 3) + count ----
teaser = "\n".join(card(p, prefix="") for p in posts[:3])
open(f"{ROOT}/data/blog-teaser.html", "w", encoding="utf-8").write(teaser)
open(f"{ROOT}/data/blog-count.txt", "w").write(str(len(posts)))

# ---- sitemap.xml + robots.txt (SEO / discoverability) ----
BASE = "https://www.pronite.in"
newest = posts[0]["date"] if posts else "2026-07-01"
urls = [(f"{BASE}/", newest, "1.0"), (f"{BASE}/blog/", newest, "0.9")]
for p in posts:
    urls.append((f"{BASE}/blog/{p['slug']}.html", p["date"], "0.7"))
try:
    for path in json.load(open(f"{ROOT}/data/event-links.json")).values():
        urls.append((f"{BASE}/{path}", newest, "0.6"))
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

print(f"built {len(posts)} blog posts + index + teaser + sitemap ({len(urls)} urls)")
