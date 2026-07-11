# Pronite — Turning on Data Capture & Visitor Analytics

The site is live and **already collecting leads today**: when someone submits the
"Join the Movement" form, it opens a pre-filled WhatsApp message to +91 91160 20099
with all their details — so no lead is ever lost, even before the steps below.

To store leads in a real database and see visitor numbers, do these two 5-minute setups
and paste the values into `PRONITE_CONFIG` at the top of `template.html`, then rebuild.

## 1. Visitor analytics — Google Analytics 4 (free)
1. Go to analytics.google.com → Admin → Create Property → "Pronite".
2. Add a **Web** data stream for `pronite.in`.
3. Copy the **Measurement ID** (looks like `G-XXXXXXXXXX`).
4. Paste it into `ga4Id` in `PRONITE_CONFIG`.
→ You'll then see live visitors, cities, devices, traffic sources, and which events
  people view — plus a "join_list" event every time someone signs up.

## 2. Lead database — Supabase (free tier, scales to millions)
1. Go to supabase.com → New project (name it "pronite").
2. In the SQL editor, run:
   ```sql
   create table leads (
     id uuid default gen_random_uuid() primary key,
     created_at timestamptz default now(),
     name text, phone text, email text, dob date,
     city text, instagram text, interest text, source text,
     tastes text, page text, ref text, ts text
   );
   alter table leads enable row level security;
   create policy "anon can insert" on leads for insert to anon with check (true);
   ```
3. Project Settings → API → copy the **Project URL** and the **anon public key**.
4. Paste them into `supabaseUrl` and `supabaseAnonKey` in `PRONITE_CONFIG`.
→ Every signup now lands as a row you can view, filter and export from Supabase.
  This same table becomes the Pronite ID `users` base for the app (Phase 2).

## After editing config
Run `python3 build.py && python3 build_events.py`, commit, push. Done.

## Data points captured per signup
name · WhatsApp phone · email · birthday · city · Instagram handle ·
interest (guest list / pro / VIP table / partner / group) ·
how-they-heard · music vibe (multi) · page · referrer · timestamp
