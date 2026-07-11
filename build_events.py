#!/usr/bin/env python3
"""Generates events/<slug>.html detail pages + featured cards from the migrated WordPress data."""
import json, re, html, os

ROOT = os.path.dirname(os.path.abspath(__file__))
embed = json.load(open(f"{ROOT}/data/events-embed.json"))
posters = json.load(open(f"{ROOT}/data/posters.json"))
os.makedirs(f"{ROOT}/events", exist_ok=True)

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# flagship (most successful) nights, in display order (matched as slug substrings)
FEATURED = ["biggest-bollywood-nite-3-0",
            "rangilo-rajasthan",
            "supersonic",
            "offgrid-udai-sarovar",
            "a-new-start",
            "christmas-festival"]

def featured_rank(slug):
    for i, k in enumerate(FEATURED):
        if k in slug: return i
    return None

def clean_title(t):
    t = html.unescape(t)
    t = re.sub(r'[\U0001F300-\U0001FAFF☀-➿️♥]', '', t)
    return re.sub(r'\s+', ' ', t).replace('"','').replace('”','').strip(' -–"')

def fname(e):
    base = re.sub(r'[^a-z0-9]+', '-', clean_title(e["title"]["rendered"]).lower()).strip('-')[:50]
    return base or str(e["id"])

def poster_for(slug):
    key = re.sub(r'[^a-z0-9-]', '', slug.lower())[:40]
    hit = posters.get(key)
    return f"../assets/posters/{hit['file']}" if hit else None

def venue_of(e):
    blob = (e["title"]["rendered"] + " " + e["content"]["rendered"]).lower()
    for k, v in [("ramada","Ramada Udaipur"),("regenta","Hotel Regenta, Udaipur"),
                 ("raffles","Raffles Resort Udaipur"),("southland","Southland's, Udaipur"),
                 ("inde hotel","The Artist House × Inde Hotel"),("artist house","The Artist House × Inde Hotel"),
                 ("supersonic","VH1 Supersonic collaboration")]:
        if k in blob: return v
    return "The Udaisarovar – Lakeside Paradise"

def clean_content(raw):
    c = re.sub(r'<script.*?</script>|<style.*?</style>', '', raw, flags=re.S)
    c = re.sub(r'<img[^>]*>', '', c)
    c = re.sub(r'\[[^\]]{1,60}\]', '', c)              # shortcodes
    # keep only text with light structure
    c = re.sub(r'</(p|div|h\d|li)>', '\n', c)
    c = re.sub(r'<br[^>]*>', '\n', c)
    c = re.sub(r'<[^>]+>', ' ', c)
    c = html.unescape(c)
    lines = [re.sub(r'\s+', ' ', l).strip() for l in c.split('\n')]
    out, seen = [], set()
    for l in lines:
        if len(l) < 3 or l in seen: continue
        seen.add(l); out.append(l)
    return out[:26]

SHELL = open(f"{ROOT}/event_shell.html", encoding="utf-8").read()

featured_cards, mem_links = [], {}
for e in embed:
    title = clean_title(e["title"]["rendered"])
    img = poster_for(e["slug"])
    f = fname(e)
    y, m, _ = e["date"][:10].split("-")
    nice = f"{MONTHS[int(m)]} {y}"
    venue = venue_of(e)
    paras = clean_content(e["content"]["rendered"])
    body = "\n".join(f"<p>{html.escape(p)}</p>" for p in paras) or "<p>One of the nights that built the Pronite name.</p>"
    page = (SHELL.replace("{TITLE}", html.escape(title))
                 .replace("{DATE}", nice).replace("{VENUE}", html.escape(venue))
                 .replace("{IMG}", img or "../assets/icon-512.png")
                 .replace("{BODY}", body))
    open(f"{ROOT}/events/{f}.html", "w", encoding="utf-8").write(page)
    mem_links[e["slug"]] = f"events/{f}.html"
    rank = featured_rank(e["slug"])
    if rank is not None and img:
        featured_cards.append((rank, f'''<a class="feat" href="events/{f}.html">
  <img src="{img[3:]}" alt="{html.escape(title)} poster" loading="lazy">
  <div><span class="fb">Signature night</span><b>{html.escape(title)}</b><em>{nice} · {html.escape(venue)}</em></div>
</a>'''))

featured_html = "\n".join(c for _, c in sorted(featured_cards))
json.dump(mem_links, open(f"{ROOT}/data/event-links.json", "w"))
open(f"{ROOT}/data/featured.html", "w", encoding="utf-8").write(featured_html)
print(f"built {len(embed)} event pages, {len(featured_cards)} featured")
