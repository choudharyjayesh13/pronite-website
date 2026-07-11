# -*- coding: utf-8 -*-
"""Pronite blog content. Each P(...) is one story. Consumed by build_blog.py.
cat in: Pronite Recap | City Guide | Scene Report | Genre | Festival | Playbook | Upcoming
Dates are 2026 publish dates (the journal's schedule); content may reference events from any year.
img is optional (relative to site root) — used for the hero/card; omit for a gradient swatch."""

POSTS = []
def P(**k): POSTS.append(k)

PO = "assets/posters/"  # poster path prefix

# ============================================================
# PRONITE RECAPS — our own nights, and how they actually went
# ============================================================

P(slug="bollywood-nite-3-recap", date="2026-01-08", cat="Pronite Recap", city="Udaipur",
  img=PO+"biggest-bollywood-nite-3-0.jpg",
  title="Bollywood Nite 3.0: the night the lawn sang every word",
  excerpt="Our biggest Bollywood night yet turned The Udaisarovar into one giant singalong. Here's how the third edition went down.",
  tags=["Bollywood","Udaipur","recap"],
  body="""<p>There is a specific moment at a Bollywood night when the DJ doesn't need the speakers anymore — the crowd carries the song. At Bollywood Nite 3.0, that moment arrived somewhere around the second act and simply never left. The Udaisarovar's lawn, strung with warm light and framed by the lake, filled early and stayed packed until the last track.</p>
<p>The formula that made the first two editions sell out was left mostly untouched: a set that moves from 2000s throwbacks into current chartbusters, a visual wall syncing to every drop, and dhol breaks placed exactly where the energy needed a lift. What changed in 3.0 was scale — a bigger stage, a wider dancefloor, and a guest list that filled up days before the gates opened.</p>
<h2>What worked</h2>
<p>Pacing. Bollywood crowds want recognition, not obscurity, so the night was built around songs everyone already loved, mixed cleanly enough to keep dancers moving between them. The retro block — think early-2000s dancefloor anthems — got the loudest response of the evening.</p>
<p>If you missed it, 4.0 is already in motion. The guest list, as always, opens on WhatsApp long before anything hits Instagram.</p>""")

P(slug="rangilo-rajasthan-holi-2026-recap", date="2026-03-18", cat="Pronite Recap", city="Udaipur",
  img=PO+"f09f8e89-rangilo-rajasthan-holi-pool-par.jpg",
  title="Rangilo Rajasthan 2026: colour, water and a lakeside pool full of people",
  excerpt="Our headline Holi pool party returned bigger — organic gulal, rain dance, and a dancefloor that spilled into the water.",
  tags=["Holi","pool party","Udaipur","recap"],
  body="""<p>Holi in Udaipur has a Pronite address now. Rangilo Rajasthan 2026 took over The Udaisarovar's poolside from late morning, and by the first rain-dance burst the whole deck was a moving wall of colour. Skin-friendly, organic gulal only — a rule we've kept since the first edition, because nobody wants to be scrubbing chemical dye off for a week.</p>
<p>The set leaned festival-house and Bollywood-Holi classics, the kind of tracklist that keeps a daytime crowd bouncing without burning out before sundown. Rain showers overhead, cold drinks flowing, and the lake as a backdrop — it's the version of Holi people fly into Udaipur for.</p>
<h2>The vibe</h2>
<p>Daytime pool parties are a different discipline from club nights. The energy has to build in the heat, hydration matters, and the crowd skews mixed — friend groups, couples, travellers. Rangilo is designed around that: shaded chill zones, a proper bar, and a dancefloor you can wade into.</p>
<p>It sold out. It always does. Next Holi's list opens early — get on it before the city does.</p>""")

P(slug="pronite-vh1-supersonic-recap", date="2026-02-24", cat="Pronite Recap", city="Pune",
  img=PO+"supersonic-x-pronite.jpg",
  title="Pronite × VH1 Supersonic: taking Udaipur's energy to the big stage",
  excerpt="Our collaboration with one of India's biggest festival brands — what it meant and what we brought to it.",
  tags=["VH1 Supersonic","festival","collaboration"],
  body="""<p>When a homegrown Udaipur collective gets to put its name next to VH1 Supersonic, you show up differently. Our collaboration with the festival was a milestone — proof that the sound we've been building lakeside translates to one of the country's largest dance-music stages.</p>
<p>Supersonic, held in Pune, is where India's festival crowd goes for a weekend of international headliners across genres — techno, house, bass, and everything adjacent. Slotting into that world meant bringing the intimacy and curation Pronite is known for into a much larger canvas.</p>
<h2>Why it mattered</h2>
<p>Festivals like Supersonic set the calendar for serious dance-music fans in India. Being part of it connected our Udaipur community to that national circuit and told our regulars something simple: the parties you love at home are playing in the same league as the big ones.</p>
<p>Watch this space — collaborations like this are exactly where Pronite is headed next.</p>""")

P(slug="offgrid-udaisarovar-recap", date="2026-01-22", cat="Pronite Recap", city="Udaipur",
  img=PO+"offgrid-udai-sarovar-edition.jpg",
  title="OFFGRID Udaisarovar Edition: techno by the lake, till the sun came up",
  excerpt="A pure underground night — no Bollywood, no requests, just long-form techno and afro house on the water's edge.",
  tags=["techno","afro house","underground","Udaipur","recap"],
  body="""<p>OFFGRID is the night we make for the heads. No sing-along block, no crowd-pleasing detours — just a long, patient build of techno and afro house that rewards the people who stay. The Udaisarovar edition put that sound where it belongs: outdoors, by the lake, under the stars.</p>
<p>The magic of an underground night is the arc. It doesn't peak in the first hour; it climbs. By the deep middle of the set, the dancefloor had thinned to the true believers and tightened into that hypnotic, heads-down groove that only happens when the DJ is trusted to take their time.</p>
<h2>The sound</h2>
<p>Afro house has quietly become the heartbeat of India's outdoor scene — melodic, percussive, made for open air. Paired with rolling techno, it gave OFFGRID a texture that Bollywood nights can't touch. Different crowd, different intention, same obsession with the details.</p>
<p>OFFGRID moves cities. If deep, driving, no-compromise dance music is your thing, this is the Pronite night to watch.</p>""")

P(slug="a-new-start-nye-recap", date="2026-01-02", cat="Pronite Recap", city="Udaipur",
  img=PO+"a-new-start.jpg",
  title="A New Start: how Pronite rang in 2026 lakeside",
  excerpt="Our New Year's Eve flagship — a countdown on the water, a headline set, and the city's most-wanted guest list.",
  tags=["NYE","New Year","Udaipur","recap"],
  body="""<p>New Year's Eve is the one night every venue in the country competes for the same crowd. A New Start was our answer in Udaipur — a lakeside countdown with production values to match the moment, and a guest list that was effectively closed weeks in advance.</p>
<p>The night was paced for the clock. Warm, familiar sets early to fill the floor, a climb through the evening, and a peak engineered to land exactly at midnight — countdown, cold spark fountains, and a drop that took the roof off an open-air venue that technically has no roof.</p>
<h2>Why NYE in Udaipur hits different</h2>
<p>Goa and the metros get the headlines, but Udaipur's lake city setting gives New Year a romance the club circuit can't fake. A New Start leaned into that: the view, the air, the sense of the whole city exhaling into a new year at once.</p>
<p>2027's edition will open its list before the year even turns. If you want in, you already know where to message us.</p>""")

P(slug="offgrid-techno-afro-recap", date="2026-02-11", cat="Pronite Recap", city="Udaipur",
  img=PO+"offgrid-techno-x-afro-night.jpg",
  title="OFFGRID: Techno × Afro — the night two sounds became one groove",
  excerpt="A back-to-back journey through rolling techno and melodic afro house that showed just how deep Udaipur's underground goes.",
  tags=["techno","afro house","underground","recap"],
  body="""<p>Some nights are about the hits. This one was about the groove. OFFGRID's Techno × Afro edition set out to prove that Udaipur has a crowd for the long, patient, hypnotic end of dance music — and the floor answered by staying full deep into the early hours.</p>
<p>Afro house brought the melody and the percussion; techno brought the drive and the darkness. Blended across a single flowing set, the two created something that never quite resolved and never needed to — a continuous, rolling momentum that pulled dancers into the classic heads-down trance.</p>
<h2>Reading the room</h2>
<p>Underground nights live or die on trust. You can't cut to a familiar chorus every ten minutes; you have to let the tension build and hold. The OFFGRID crowd gets that, which is exactly why we keep making these nights for them.</p>
<p>If this is your frequency, OFFGRID is your home on the Pronite calendar.</p>""")

P(slug="hypnosis-open-air-recap", date="2026-02-04", cat="Pronite Recap", city="Udaipur",
  img=PO+"f09f92ab-hypnosis-f09f92abopen-air.jpg",
  title="Hypnosis Open Air: an outdoor trance-out under Udaipur's sky",
  excerpt="Open-air production, a hypnotic set and a crowd that came to lose track of time — Hypnosis did exactly what its name promised.",
  tags=["open air","techno","recap"],
  body="""<p>Hypnosis is built around a single idea: put a great sound system outdoors, program a set that never breaks the spell, and let the crowd disappear into it. The open-air edition delivered that in full — a long, immersive night where the music did the talking and nobody was watching the clock.</p>
<p>Outdoor nights have a texture indoor clubs can't replicate. Sound behaves differently in open air, the sky becomes part of the production, and the crowd relaxes into a looser, freer state. Hypnosis leaned all the way into that.</p>
<h2>Production first</h2>
<p>The lights and staging were tuned for immersion, not spectacle — deep, moody, wrapping the floor rather than blinding it. That restraint is what made the set land. It's the same philosophy behind everything we label OFFGRID and Hypnosis: the experience over the flash.</p>
<p>Outdoor season in Udaipur is short and precious. When Hypnosis returns, it goes fast.</p>""")

P(slug="hypnotica-7-recap", date="2026-02-18", cat="Pronite Recap", city="Udaipur",
  img=PO+"hypnotica-7-0.jpg",
  title="Hypnotica 7.0: seven editions deep and still climbing",
  excerpt="A series that's become a Udaipur institution — the seventh edition proved why Hypnotica keeps selling out.",
  tags=["techno","series","recap"],
  body="""<p>Reaching a seventh edition means you've built something people trust. Hypnotica 7.0 carried that weight lightly — a confident, well-drilled night from a series that has quietly become one of Udaipur's most reliable dancefloors.</p>
<p>The strength of a long-running series is the crowd. Regulars know the sound, arrive ready, and set the tone for newcomers. By the time the headline set hit its stride, the floor was already locked in — no warm-up friction, just momentum.</p>
<h2>The staying power</h2>
<p>Seven editions is rare in a scene where most party brands fade after two or three. Hypnotica lasted because it never chased trends — it stuck to a sound, refined the production each time, and let word of mouth do the rest.</p>
<p>Edition eight is coming. If you've never done a Hypnotica night, this is your cue.</p>""")

P(slug="dark-dimensions-recap", date="2026-01-29", cat="Pronite Recap", city="Udaipur",
  img=PO+"dark-dimensions.jpg",
  title="Dark Dimensions: the heavier, darker side of the Pronite floor",
  excerpt="A night built for the peak-time techno crowd — harder, faster, and unapologetically underground.",
  tags=["techno","underground","recap"],
  body="""<p>Not every night is meant to be pretty. Dark Dimensions is where Pronite goes heavier — driving, hypnotic, peak-time techno for a crowd that wants intensity over singalongs. It's the counterweight to our Bollywood and Holi events, and it draws a devoted following of its own.</p>
<p>The night was programmed as a slow descent into the harder end of the spectrum. Restrained early, relentless late. That kind of set demands a crowd that came specifically for it — and this one did.</p>
<h2>Why the dark stuff matters</h2>
<p>A healthy scene needs range. If every night is a crowd-pleaser, you never build the core of true dance-music fans who show up for the sound itself. Dark Dimensions is our commitment to that core — and to the idea that Udaipur can hold a proper underground night.</p>
<p>Consider this your warning for the next one.</p>""")

P(slug="techno-tales-recap", date="2026-01-15", cat="Pronite Recap", city="Udaipur",
  img=PO+"techno-tales.jpg",
  title="Techno Tales: a storytelling set for Udaipur's underground",
  excerpt="Less about drops, more about journey — Techno Tales treated the DJ set like a narrative from first track to last.",
  tags=["techno","underground","recap"],
  body="""<p>The best techno sets tell a story, and Techno Tales made that its entire premise. No shortcuts to the peak, no crowd-baiting — just a carefully sequenced journey that took the floor somewhere over the course of the night and brought it back.</p>
<p>That approach filters the crowd in the best way. The people who stay for a narrative set are the ones who genuinely love the music, and their energy is different — patient early, then fully committed once the story finds its climax.</p>
<h2>The craft</h2>
<p>Programming a set like this is a skill most casual listeners never notice, which is the point. Done right, it feels effortless — one track flowing into the next as if it could only ever have gone that way. Techno Tales is our tribute to that craft.</p>
<p>For the heads who get it, this is essential Pronite.</p>""")

P(slug="rang-e-udaipur-holi-2025-recap", date="2026-03-11", cat="Pronite Recap", city="Udaipur",
  img=PO+"rang-e-holi-2025.jpg",
  title="Rang-e-Udaipur: the Holi session that set the template",
  excerpt="Before Rangilo Rajasthan there was Rang-e-Udaipur — the daytime colour party that proved the format works lakeside.",
  tags=["Holi","pool party","Udaipur","recap"],
  body="""<p>Every signature event has an origin, and Rang-e-Udaipur is where our Holi format found its feet. Colour, water, a daytime dancefloor and a lakeside setting — the ingredients that Rangilo Rajasthan would later scale up all came together here first.</p>
<p>What made it click was the balance. Holi parties can tip into chaos; this one stayed joyful and controlled — organic colours, a proper sound setup, and enough space to dance, cool off, and go again.</p>
<h2>Setting the standard</h2>
<p>Udaipur has plenty of Holi gatherings, but few treat it as a properly produced event. Rang-e-Udaipur did, and the response told us there was real appetite for a premium, well-run colour party in the city. Everything we do at Holi now traces back to this session.</p>
<p>The lineage continues every March. You know when to message us.</p>""")

P(slug="southlands-holi-recap", date="2026-03-04", cat="Pronite Recap", city="Udaipur",
  img=PO+"southlands-holi-festival.jpg",
  title="Southland's Holi Festival: colour in the heart of the city",
  excerpt="A Holi festival edition at Southland's — proof the Pronite colour party travels beyond the lakeside.",
  tags=["Holi","festival","Udaipur","recap"],
  body="""<p>Not every Holi party needs a pool to work. The Southland's edition took our colour-festival format into a city venue and kept every bit of the energy — a reminder that the crowd, the music and the gulal matter more than the postcard backdrop.</p>
<p>City venues bring their own advantages: easier access, a different crowd, and a more compact, high-density dancefloor that concentrates the energy. Southland's delivered exactly that kind of tightly packed, all-in Holi session.</p>
<h2>Range by design</h2>
<p>Running Holi across multiple venues lets us serve different crowds — the lakeside spectacle for travellers and big groups, the city session for locals who want colour without the commute. Southland's is the city-side of that coin.</p>
<p>Wherever it lands next March, the rule stays the same: skin-friendly colours, real sound, zero compromise.</p>""")

P(slug="white-night-christmas-recap", date="2026-01-05", cat="Pronite Recap", city="Udaipur",
  img=PO+"white-night-christmas.jpg",
  title="White Night: Pronite's Christmas dressed all in white",
  excerpt="An all-white Christmas party that turned the season's biggest weekend into a full-on Pronite dancefloor.",
  tags=["Christmas","theme night","recap"],
  body="""<p>A dress code changes a room. White Night's all-in-white theme turned our Christmas edition into something that photographed as well as it partied — a sea of white under coloured light, with the season's warmth built into every set.</p>
<p>Christmas week is prime party season in India, sitting right before the New Year's rush, and the crowd comes out in full holiday mood. White Night gave that mood a canvas: festive, celebratory, and just glamorous enough to feel like an occasion.</p>
<h2>Theme nights work</h2>
<p>A strong theme gives people a reason to commit — to dress up, to post, to show up early. White Night proved how much a simple, striking concept adds to a party. It's a lever we'll keep pulling.</p>
<p>The Christmas-to-NYE stretch is the busiest on our calendar. Plan early, because these lists close fast.</p>""")

P(slug="ramada-nye-recap", date="2026-01-03", cat="Pronite Recap", city="Udaipur",
  img=PO+"new-years-eve-at-ramada-hotel.jpg",
  title="New Year's Eve at Ramada: a five-star countdown",
  excerpt="Bringing the Pronite New Year to a premium hotel ballroom — polished, packed, and perfectly timed to midnight.",
  tags=["NYE","New Year","hotel","recap"],
  body="""<p>Some New Year's crowds want the open-air lakeside; others want a five-star ballroom with everything handled. Our Ramada edition served the second — a polished, premium NYE with hotel-grade production and a countdown engineered to the second.</p>
<p>Hotel partnerships let us offer a different tier of New Year: valet, indoor comfort, food and beverage sorted, and the security of a marquee venue. For couples and groups who want a refined night out, it's the ideal format.</p>
<h2>Two flavours of NYE</h2>
<p>Running both a lakeside flagship and a hotel edition means nobody in Udaipur has to compromise on New Year's. Ramada is the dressed-up, indoor option — same Pronite programming, different setting.</p>
<p>Both editions sell out. Whichever is your speed, get on the list early.</p>""")

P(slug="raffles-nye-2024-recap", date="2026-01-07", cat="Pronite Recap", city="Udaipur",
  img=PO+"nye-2024-raffles.jpg",
  title="Raffles NYE: New Year at one of Udaipur's finest addresses",
  excerpt="A luxury-resort New Year's Eve that matched Pronite's sound to a genuinely spectacular setting.",
  tags=["NYE","luxury","resort","recap"],
  body="""<p>Venue is half the party, and Raffles is a venue that does a lot of the work for you. Our New Year's edition there paired a genuinely stunning resort setting with the Pronite touch — a night that felt as premium as the address on the invite.</p>
<p>Luxury-resort events attract a specific crowd: people who want the experience elevated end to end, from arrival to the midnight moment. The programming reflected that — refined, celebratory, and never crossing into chaos.</p>
<h2>The setting sells itself</h2>
<p>When the backdrop is this good, the job is to complement it, not compete with it. Clean sound, tasteful production, and impeccable timing to midnight — that's the brief for a night like this, and Raffles delivered on its side too.</p>
<p>Premium New Year's editions are limited by capacity. That's exactly why the list matters.</p>""")

P(slug="afterall-music-tour-recap", date="2026-02-27", cat="Pronite Recap", city="Udaipur",
  img=PO+"afterallmusic-all-india-tour.jpg",
  title="AfterAll Music All-India Tour: Udaipur on the national map",
  excerpt="When a touring music brand routes through your city, it means the scene has arrived — and Udaipur showed up.",
  tags=["tour","collaboration","recap"],
  body="""<p>A city earns a stop on an all-India tour by proving it has a crowd worth the trip. Hosting the AfterAll Music tour was exactly that kind of validation — Udaipur slotted onto a national route alongside the metros, and the turnout backed it up.</p>
<p>Touring brands bring a curated sound and an outside energy, and pairing that with Pronite's local knowledge — the right venue, the right crowd, the right timing — is how you make a tour date land instead of fizzle.</p>
<h2>Why touring dates matter</h2>
<p>They connect a local scene to the national circuit and give regulars access to acts they'd otherwise have to travel to catch. Every tour stop we host makes the case that Udaipur belongs on the map.</p>
<p>More national collaborations are on the way. Being on our list is how you hear first.</p>""")

P(slug="lakeside-camping-night-recap", date="2026-02-07", cat="Pronite Recap", city="Udaipur",
  img=PO+"f09f8c99-a-night-to-remember-lakeside-ca.jpg",
  title="A Night to Remember: camping and music on the lakeside",
  excerpt="Tents, a bonfire, a sky full of stars and a dancefloor by the water — Pronite's camping night is a different kind of party.",
  tags=["camping","outdoor","experience","recap"],
  body="""<p>Not every Pronite night ends when the music stops. The lakeside camping edition wrapped the party inside a full overnight experience — tents pitched by the water, a bonfire, food, and a dancefloor under open sky that rolled straight into a starlit wind-down.</p>
<p>Camping events attract people who want more than a few hours on a dancefloor. It's a weekend, a getaway, a reset — and it turns a crowd of strangers into something closer to a community by morning.</p>
<h2>The experience economy</h2>
<p>Music is the anchor, but the memory is the whole package: the fire, the tents, the sunrise over the lake. That's the direction we keep leaning — nights you don't just attend, but remember.</p>
<p>Camping editions have limited spots by nature. When one drops, it goes quickly.</p>""")

P(slug="camping-night-lakeside-recap", date="2026-02-14", cat="Pronite Recap", city="Udaipur",
  img=PO+"f09f8c99-camping-night-near-lakeside-f09.jpg",
  title="Camping Night near the Lakeside: bonfire, beats and a starlit reset",
  excerpt="Our second take on the camping format — proof that the getaway party is becoming a Pronite signature.",
  tags=["camping","outdoor","experience","recap"],
  body="""<p>Once is an experiment; twice is a format. Our second lakeside camping night confirmed that Udaipur's crowd wants the overnight, out-of-town version of a Pronite party — bonfire, tents, open sky, and music that soundtracks the whole thing.</p>
<p>The pacing of a camping night is unlike a club: it breathes. High energy on the dancefloor, then a slow drift toward the fire, conversation, and the quiet of a lakeside dawn. It's as much retreat as rave.</p>
<h2>Where this goes</h2>
<p>The Udaisarovar's villas-and-camps setup makes Udaipur one of the few places you can run a proper camping party with real infrastructure behind it. Expect more of these — bigger, and further off-grid.</p>
<p>Follow the list. The camping drops are the first to sell out.</p>""")

P(slug="udaisarovar-villas-camps-recap", date="2026-01-19", cat="Pronite Recap", city="Udaipur",
  img=PO+"the-udaisarovar-villas-resort-special-of.jpg",
  title="The Udaisarovar villas & camps: where the party has a home",
  excerpt="Behind every Pronite lakeside night is a venue built for it. A look at the home base — and why it changes what we can do.",
  tags=["venue","Udaisarovar","experience"],
  body="""<p>Great parties need great venues, and having The Udaisarovar as a home base is a large part of the Pronite story. Villas, camps, a lakeside setting and the space to build a proper dancefloor — it's an events canvas most collectives would kill for.</p>
<p>The advantage is control. When you own the setting, you can shape the whole experience — where the stage goes, how late it runs, whether guests stay over. That's how camping nights, pool parties and open-air techno all live under one roof.</p>
<h2>Stay-and-party</h2>
<p>The villas-and-camps model unlocks something rare: the ability to make the party a destination. Come for the music, stay for the lake, wake up somewhere beautiful. It's the backbone of where Pronite is heading.</p>
<p>Special stay-and-party offers surface on our list first — another reason to be on it.</p>""")
