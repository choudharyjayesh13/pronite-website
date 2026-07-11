# Pronite Platform — Architecture Roadmap

Goal: one Pronite platform — website today, mobile app tomorrow — with a single
customer identity (Pronite ID) shared across both.

## Phase 1 — this repo (LIVE NOW)
Fast static PWA. No database, no login.
- All 22 events + posters migrated from the old WordPress site
- Guest list & partner enquiries via WhatsApp (+91 91160 20099)
- Installable on phones (PWA manifest + service worker) — this is the app shell
- SEO: Organization schema, correct titles/descriptions, share previews

## Phase 2 — accounts & ticketing (needs Jayesh's go)
Backend: **Supabase** (free tier to start, scales to millions of rows)
- `users` — Pronite ID (uuid), phone (login via SMS OTP — no passwords), name, city
- `events` — title, venue, datetime, poster, ticket tiers, capacity
- `tickets` — user_id, event_id, tier, QR code, check-in status
- `orders` — Razorpay payment id, amount, status
- `partners` — venue/brand accounts with their own dashboard (their events, sales)
- `memberships` — free / pro, validity, perks
Frontend stays this repo (static + Supabase JS client) — no servers to manage.
Payments: **Razorpay** (UPI/cards; needs Jayesh's KYC + bank account).
Door check-in: QR scan page usable on any phone.

## Phase 3 — the app
Same Supabase backend, zero rework:
- Option A (fast): wrap the PWA with Capacitor → Play Store / App Store
- Option B (native feel): React Native app on the same APIs
Push notifications for event drops via Firebase Cloud Messaging.

## Data migrated from old WordPress (wp-json export, 11 Jul 2026)
- 22 events (2023-12 → 2026-03) with full descriptions — `data/events-clean.json`
- 21 posters — `assets/posters/`
- About / membership / policy copy — `data/pages.json`
- 535 attendee registrations exist in the old DB — **NOT in this repo** (private
  data; export via wp-admin → Eventin → Attendees CSV once logged in, then seed
  Phase-2 `users` table)

## Old site (keep until Phase 2)
WordPress on Hostinger (LiteSpeed), Eventin + WooCommerce. Domain pronite.in
DNS is at Hostinger. Cutover = point pronite.in at GitHub Pages (CNAME), same
process as theudaisarovar.com. Do NOT cut over until Jayesh approves, since the
old checkout dies with it.
