#!/usr/bin/env python3
"""Builds index.html for the new pronite.in from extracted WordPress data."""
import json, re, html, os

ROOT = os.path.dirname(os.path.abspath(__file__))
events = json.load(open(f"{ROOT}/data/events-clean.json"))
posters = json.load(open(f"{ROOT}/data/posters.json"))

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

def poster_for(slug):
    key = re.sub(r'[^a-z0-9-]', '', slug.lower())[:40]
    hit = posters.get(key)
    return f"assets/posters/{hit['file']}" if hit else None

def nice_date(iso):
    y, m, _ = iso.split("-")
    return f"{MONTHS[int(m)]} {y}"

def clean_title(t):
    t = re.sub(r'[\U0001F300-\U0001FAFF☀-➿️]', '', t)  # strip emoji
    return re.sub(r'\s+', ' ', t).replace('"', '').replace('”', '').strip(' -–"')

cards = []
for e in sorted(events, key=lambda x: x["date"], reverse=True):
    img = poster_for(e["slug"])
    if not img:
        continue
    title = html.escape(clean_title(e["title"]))
    cards.append(f'''<figure class="mem">
  <img src="{img}" alt="{title} — Pronite event poster" loading="lazy">
  <figcaption><b>{title}</b><span>{nice_date(e["date"])}</span></figcaption>
</figure>''')
cards_html = "\n".join(cards)

page = open(f"{ROOT}/template.html", encoding="utf-8").read()
page = page.replace("<!--MEMORY_CARDS-->", cards_html)
page = page.replace("<!--EVENT_COUNT-->", str(len(events)))
open(f"{ROOT}/index.html", "w", encoding="utf-8").write(page)
print(f"built index.html with {len(cards)} poster cards")
