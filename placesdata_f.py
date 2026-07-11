# -*- coding: utf-8 -*-
"""Places batch F — WEST INDIA: Mumbai, Goa, Pune.
Landmarks + beaches + nightlife + food streets + markets.
New category here: Beach."""
POSTS = []
def P(**k): POSTS.append(k)

# ======================= MUMBAI =======================

P(slug="gateway-of-india-mumbai", city="Mumbai", region="Maharashtra", cat="Landmark",
  name="Gateway of India", query="Gateway of India Mumbai",
  excerpt="Mumbai's grand seafront arch — the city's most iconic landmark, gazing out over the Arabian Sea beside the Taj hotel.",
  tags=["Mumbai","landmark","seafront","colonial"],
  info=dict(timings="Open all day; best morning or evening", entry="Free",
            best="Early morning or sunset", duration="1 hour", reach="Colaba, South Mumbai; nearest station CSMT / Churchgate"),
  body="""<p>The Gateway of India is Mumbai's signature monument — a majestic basalt arch built in the early 20th century to commemorate a royal visit, standing proudly on the waterfront where the city meets the Arabian Sea. It was, symbolically, the last British troops' exit point from India.</p>
<p>Today it's the beating heart of tourist Mumbai: boats depart from here to Elephanta Island, photographers and balloon-sellers work the crowds, and the grand Taj Mahal Palace hotel provides a spectacular backdrop. At dawn, before the crowds, it's genuinely serene.</p>
<h2>Don't miss</h2>
<ul><li>The arch framed against the sea and the Taj hotel.</li><li>A ferry ride from the adjacent jetty to Elephanta.</li><li>The buzzing evening atmosphere on the plaza.</li></ul>
<h2>Good to know</h2>
<p>It gets very crowded midday — go early. Combine with a stroll through the colonial architecture of Colaba and Fort.</p>""")

P(slug="marine-drive-mumbai", city="Mumbai", region="Maharashtra", cat="Landmark",
  name="Marine Drive", query="Marine Drive Mumbai",
  excerpt="Mumbai's glittering seafront promenade — the 'Queen's Necklace', where the whole city comes to watch the sunset.",
  tags=["Mumbai","promenade","sunset","seafront"],
  info=dict(timings="Open 24 hours", entry="Free",
            best="Sunset into evening", duration="1–2 hours", reach="South Mumbai; nearest station Charni Road / Churchgate"),
  body="""<p>Marine Drive is Mumbai in a single sweep — a 3.6 km curve of seafront boulevard along the Arabian Sea, backed by Art Deco buildings and lined with a wide promenade where the entire city seems to gather at dusk. Its arc of streetlights, glowing at night, earned it the nickname the 'Queen's Necklace'.</p>
<p>This is the city's collective living room: couples, families, joggers, dreamers and vendors all sharing the sea wall as waves crash below and the sun sinks into the water. Few urban sunsets anywhere are as beloved.</p>
<h2>Don't miss</h2>
<ul><li>Sunset from the sea wall, with the city lighting up behind you.</li><li>The 'Queen's Necklace' curve of lights after dark.</li><li>The Art Deco skyline (a UNESCO-listed ensemble) along the drive.</li></ul>
<h2>Good to know</h2>
<p>It's free, open always, and pure people-watching gold. Grab a coffee or bhelpuri and claim a spot on the wall for sunset.</p>""")

P(slug="elephanta-caves-mumbai", city="Mumbai", region="Maharashtra", cat="Landmark",
  name="Elephanta Caves", query="Elephanta Caves",
  excerpt="Ancient rock-cut cave temples on an island in Mumbai harbour — a UNESCO site crowned by a colossal three-headed Shiva.",
  tags=["Mumbai","UNESCO","caves","island"],
  info=dict(timings="Caves ~9 AM – 5 PM (closed Mondays); ferries from Gateway", entry="Approx ₹40 (Indian) / ₹600 (foreign) + ferry fare",
            best="Weekday morning; October–March", duration="Half day (incl. ferry)", reach="Island in Mumbai harbour — ~1 hr ferry from the Gateway of India"),
  body="""<p>A short ferry ride across Mumbai harbour delivers you to Elephanta Island and its extraordinary rock-cut cave temples, carved between the 5th and 8th centuries. A UNESCO World Heritage Site, the caves are hewn directly from the basalt hillside and dedicated to Lord Shiva.</p>
<p>The masterpiece is the Trimurti — a colossal, serene three-headed sculpture of Shiva that ranks among the greatest works of Indian art. The boat journey, the hilltop setting and the ancient carvings together make a rewarding escape from the city.</p>
<h2>Don't miss</h2>
<ul><li>The magnificent three-headed Trimurti Sadashiva sculpture.</li><li>The carved panels of Shiva in the main cave.</li><li>The harbour ferry ride and island views.</li></ul>
<h2>Good to know</h2>
<p>Closed on Mondays. Ferries run from the Gateway of India; check the last return boat. There's a steep climb (and a small toy train) up to the caves. Watch out for the island's cheeky monkeys.</p>""")

P(slug="colaba-causeway-mumbai", city="Mumbai", region="Maharashtra", cat="Street & Bazaar",
  name="Colaba Causeway", query="Colaba Causeway Mumbai",
  excerpt="Mumbai's most famous shopping street — a bustling stretch of street stalls, cafés, antiques and the legendary Leopold Café.",
  tags=["Mumbai","shopping","street","Colaba"],
  info=dict(timings="Street stalls roughly 11 AM – 10 PM", entry="Free",
            best="Late afternoon into evening", duration="2–3 hours", reach="Colaba, South Mumbai; near the Gateway of India"),
  body="""<p>Colaba Causeway is the buzzing retail spine of South Mumbai — a long, crowded street where pavement stalls spill over with cheap jewellery, clothes, sunglasses, handicrafts and curios, all to be haggled over with gusto. It's the city's classic street-shopping experience.</p>
<p>Between the bargains, the causeway is dotted with atmospheric institutions: the historic Leopold Café, antique shops, bookstores and some of Mumbai's best-loved eateries. It's tourist-central, but genuinely fun.</p>
<h2>Don't miss</h2>
<ul><li>Bargaining for clothes, jewellery and souvenirs at the street stalls.</li><li>A beer at the historic Leopold Café.</li><li>The nearby Kala Ghoda arts precinct and galleries.</li></ul>
<h2>Good to know</h2>
<p>Haggle hard — starting prices are inflated for tourists. Keep an eye on belongings in the crowds. Easily paired with the Gateway of India.</p>""")

P(slug="mohammed-ali-road-mumbai", city="Mumbai", region="Maharashtra", cat="Food Street",
  name="Mohammed Ali Road (food)", query="Mohammed Ali Road Mumbai",
  excerpt="Mumbai's most famous food street — a carnival of kebabs, biryani and sweets that comes alive after dark, especially during Ramadan.",
  tags=["Mumbai","street food","food","Ramadan"],
  info=dict(timings="Evenings till late; legendary during Ramadan nights", entry="Free (pay as you eat)",
            best="After dark; the Ramadan season is peak", duration="An evening of grazing", reach="Near Crawford Market / Bhendi Bazaar, South Mumbai"),
  body="""<p>When the sun goes down, Mohammed Ali Road lights up as Mumbai's most legendary food destination. This is carnivore heaven — a smoky, sizzling stretch of stalls and century-old eateries turning out seekh kebabs, tandoori meats, rich biryanis, nihari, and a dazzling array of sweets.</p>
<p>The scene reaches its glorious peak during the holy month of Ramadan, when the street transforms into a nightly food festival and crowds descend for post-fast feasting. Even outside Ramadan, it's one of India's great eating streets.</p>
<h2>Don't miss</h2>
<ul><li>Seekh kebabs, tandoori meats and rich mutton biryani.</li><li>Malpua and other syrupy sweets for dessert.</li><li>The electric Ramadan-night atmosphere, if you visit then.</li></ul>
<h2>Good to know</h2>
<p>Come hungry and after dark. It's busiest and best during Ramadan. Predominantly a meat-lover's paradise, though sweets abound for everyone.</p>""")

P(slug="bandra-mumbai", city="Mumbai", region="Maharashtra", cat="Nightlife",
  name="Bandra", query="Bandra Mumbai Bandstand",
  excerpt="Mumbai's coolest neighbourhood — sea-facing promenades, street art, indie cafés, buzzing bars and Bollywood-star addresses.",
  tags=["Mumbai","nightlife","hip","suburb"],
  info=dict(timings="Cafés from morning; bars and live venues till late", entry="Free to explore; venues priced individually",
            best="Evening into night", duration="An evening (or a full day)", reach="Western suburbs; nearest station Bandra"),
  body="""<p>If South Mumbai is the city's grand old face, Bandra is its cool, creative heart. This western suburb blends old Portuguese-era villas and colourful street art with a thriving scene of indie cafés, boutiques, gastropubs, live-music venues and some of the city's best bars.</p>
<p>By day, wander the mural-covered lanes of Chapel Road, the sea-facing Bandstand and Carter Road promenades (and spot the odd Bollywood mansion). By night, Bandra is one of Mumbai's premier destinations for a drink, a gig or a long dinner.</p>
<h2>Don't miss</h2>
<ul><li>The street art and murals around Chapel Road.</li><li>Sunset along the Bandstand and Carter Road promenades.</li><li>The neighbourhood's celebrated cafés, gastropubs and live-music bars.</li></ul>
<h2>Good to know</h2>
<p>Weekend nights are liveliest. It's spread out — pick a pocket (Bandstand, Hill Road, Pali) and explore on foot. A great base for Mumbai's contemporary side.</p>""")

P(slug="juhu-beach-mumbai", city="Mumbai", region="Maharashtra", cat="Beach",
  name="Juhu Beach", query="Juhu Beach Mumbai",
  excerpt="Mumbai's most famous beach — less about swimming, more about sunsets, street food and the full-throttle energy of the city at play.",
  tags=["Mumbai","beach","street food","sunset"],
  info=dict(timings="Open all day; liveliest in the evening", entry="Free",
            best="Evening, for sunset and chaat", duration="1–2 hours", reach="Juhu, western suburbs; near Vile Parle / Andheri"),
  body="""<p>Juhu Beach isn't for swimming — it's for soaking up Mumbai at its most exuberant. This long stretch of sand in the western suburbs is where the city comes to unwind: families paddling, kids on ponies, cricket games, and above all, food.</p>
<p>The beach is famous for its chaat — pav bhaji, bhelpuri, pani puri and dosas served from a line of stalls — best enjoyed as the sun sets over the Arabian Sea. It's chaotic, colourful and quintessentially Mumbai.</p>
<h2>Don't miss</h2>
<ul><li>Sunset over the Arabian Sea.</li><li>The legendary beach chaat — pav bhaji, bhelpuri, pani puri.</li><li>The buzzing evening carnival atmosphere.</li></ul>
<h2>Good to know</h2>
<p>The water isn't clean enough for swimming — this is a hangout-and-eat beach. Evenings are best. Eat at busy, high-turnover stalls.</p>""")

# ======================= GOA =======================

P(slug="baga-calangute-beach-goa", city="Goa", region="Goa", cat="Beach",
  name="Baga & Calangute Beaches", query="Baga Beach Goa",
  excerpt="North Goa's buzzing beach heartland — water sports by day, shacks and famous nightlife by night. Goa at full volume.",
  tags=["Goa","beach","nightlife","water sports"],
  info=dict(timings="Open all day; shacks & clubs till late", entry="Free (activities & venues charged)",
            best="November–February; sunset onwards for the party", duration="A day into night", reach="North Goa; ~40 min from Panaji or the airport"),
  body="""<p>Baga and neighbouring Calangute are the loud, lively heart of North Goa's beach scene — long golden strands packed with shacks, sun-loungers, water-sports operators and, come evening, some of the state's most famous nightlife. This is Goa at its most full-on.</p>
<p>By day, try parasailing, jet-skis or banana boats, then settle into a beach shack for seafood and a cold beer. By night, the area around Tito's Lane erupts into clubs and bars. It's touristy and boisterous — and enormous fun if that's the Goa you're after.</p>
<h2>Don't miss</h2>
<ul><li>Water sports — parasailing, jet-skiing, banana boats.</li><li>Fresh seafood and sunset drinks at a beach shack.</li><li>The nightlife around Tito's Lane after dark.</li></ul>
<h2>Good to know</h2>
<p>Peak season (Dec–Jan) is crowded and pricey; quieter beaches lie further north (Ashwem, Morjim) and south. For calm, this isn't it — for buzz, it's perfect.</p>""")

P(slug="palolem-beach-goa", city="Goa", region="Goa", cat="Beach",
  name="Palolem Beach", query="Palolem Beach Goa",
  excerpt="South Goa's postcard crescent — a calm, palm-fringed bay of colourful huts, gentle waters and famous silent-disco nights.",
  tags=["Goa","beach","south goa","relaxed"],
  info=dict(timings="Open all day", entry="Free",
            best="November–March", duration="A day (or a lazy week)", reach="South Goa; ~1.5–2 hrs from the airport"),
  body="""<p>If North Goa is the party, Palolem is the postcard. This perfect crescent of soft sand in the far south, fringed by swaying palms and calm, swimmable waters, is the image most people have of a dream Goan beach — relaxed, scenic and blissfully laid-back.</p>
<p>Colourful beach huts line the shore, kayaks drift on the gentle bay, and the vibe is unhurried by day. By night, Palolem is famous for its 'silent disco' parties, where dancers wear wireless headphones so the beach stays legally quiet — a uniquely Goan experience.</p>
<h2>Don't miss</h2>
<ul><li>The palm-fringed crescent and calm swimming water.</li><li>Kayaking on the bay and dolphin-spotting trips.</li><li>The famous silent-disco headphone parties at night.</li></ul>
<h2>Good to know</h2>
<p>Much of Palolem's beach-hut scene is seasonal (roughly Nov–Apr) and dismantled in the monsoon. Quieter and more scenic than the north — ideal for slowing down.</p>""")

P(slug="basilica-bom-jesus-goa", city="Old Goa", region="Goa", cat="Landmark",
  name="Basilica of Bom Jesus", query="Basilica of Bom Jesus Goa",
  excerpt="A UNESCO-listed baroque basilica in Old Goa holding the relics of St Francis Xavier — the finest of the region's grand churches.",
  tags=["Goa","church","UNESCO","heritage"],
  info=dict(timings="Approx 9 AM – 6:30 PM (Sun from ~10:30 AM)", entry="Free",
            best="Morning; October–March", duration="1 hour", reach="Old Goa, ~10 km east of Panaji"),
  body="""<p>There's another Goa beyond the beaches — the grand Catholic heritage of Old Goa, once the glittering capital of Portuguese India. Its churches are collectively a UNESCO World Heritage Site, and the greatest of them is the Basilica of Bom Jesus, a masterpiece of baroque architecture completed in 1605.</p>
<p>Inside its weathered laterite façade lies the ornate, gilded tomb of St Francis Xavier, whose remarkably preserved remains draw pilgrims from around the world. It's a striking reminder of Goa's unique blend of Indian and European history.</p>
<h2>Don't miss</h2>
<ul><li>The gilded tomb and relics of St Francis Xavier.</li><li>The ornate baroque interior and altars.</li><li>The nearby Se Cathedral, one of Asia's largest churches.</li></ul>
<h2>Good to know</h2>
<p>Dress modestly (shoulders and knees covered). Old Goa's churches cluster together — see several in one visit. A calm, cultural contrast to the coast.</p>""")

P(slug="anjuna-flea-market-goa", city="Goa", region="Goa", cat="Street & Bazaar",
  name="Anjuna Flea Market", query="Anjuna Flea Market Goa",
  excerpt="Goa's legendary hippie-era market — a sprawling weekly bazaar of clothes, jewellery, crafts and characters above Anjuna beach.",
  tags=["Goa","market","shopping","hippie"],
  info=dict(timings="Wednesdays, roughly 9 AM – 6 PM (season only)", entry="Free",
            best="Wednesday during the season (Nov–Apr); go early or late to beat the heat", duration="2–3 hours", reach="Anjuna, North Goa"),
  body="""<p>Born in Goa's 1970s hippie heyday, the Anjuna Flea Market is a Wednesday institution — a vast, colourful sprawl of stalls above the cliffs of Anjuna beach, selling everything from bohemian clothes and silver jewellery to Tibetan crafts, spices, souvenirs and psychedelic art.</p>
<p>As much a scene as a shop, the market draws travellers, traders and long-staying free spirits from across India and beyond. Haggling is expected, the atmosphere is festive, and it's a brilliant place to pick up gifts and soak up Goa's alternative side.</p>
<h2>Don't miss</h2>
<ul><li>Bargaining for clothes, jewellery and handicrafts.</li><li>The eclectic mix of traders and travellers.</li><li>The cliff-top setting above Anjuna beach.</li></ul>
<h2>Good to know</h2>
<p>It runs on Wednesdays during the tourist season only. Bargain hard and go early or late to dodge the midday heat. The Saturday Night Market at Arpora is a lively alternative.</p>""")

P(slug="tito-lane-goa", city="Goa", region="Goa", cat="Nightlife",
  name="Tito's Lane (Baga nightlife)", query="Baga Beach Goa night",
  excerpt="The most famous nightlife strip in India — a neon lane of clubs and bars that turns North Goa's Baga into a dancefloor after dark.",
  tags=["Goa","nightlife","clubs","Baga"],
  info=dict(timings="Bars from evening; clubs peak late night", entry="Free to walk; clubs have covers/table minimums",
            best="Peak season nights (Dec–Jan); weekends", duration="A big night out", reach="Off Baga Beach, North Goa"),
  body="""<p>Tito's Lane is shorthand for Goa's party reputation. This short, neon-lit strip running back from Baga Beach is packed with the clubs and bars that made North Goa India's nightlife capital — from the legendary Tito's and Café Mambo to a string of thumping dancefloors.</p>
<p>Come night, the lane fills with a boisterous, up-for-it crowd bouncing between commercial club nights, cocktail bars and beachfront parties. It's loud, unpretentious and packed in peak season — the very definition of a big Goa night out.</p>
<h2>Don't miss</h2>
<ul><li>Club-hopping along the neon strip.</li><li>The beachfront clubs where the sand meets the dancefloor.</li><li>The peak-season and New Year party energy.</li></ul>
<h2>Good to know</h2>
<p>It's mainstream and commercial — for underground techno and sunrise sets, head to the clubs around Vagator, Anjuna and Morjim. Watch your tab and drink responsibly; New Year's here is legendary but wild.</p>""")

# ======================= PUNE =======================

P(slug="shaniwar-wada-pune", city="Pune", region="Maharashtra", cat="Palace & Fort",
  name="Shaniwar Wada", query="Shaniwar Wada Pune",
  excerpt="The fortified palace-seat of the Maratha Peshwas — grand gateways, legend and a haunting history at the heart of Pune.",
  tags=["Pune","Maratha","fort","history"],
  info=dict(timings="8 AM – 6:30 PM; evening light & sound show", entry="Approx ₹25 (Indian) / ₹300 (foreign)",
            best="Morning or the evening show", duration="1–1.5 hours", reach="Central Pune old city"),
  body="""<p>Shaniwar Wada was the seat of the Peshwas, the powerful prime ministers of the Maratha Empire, and once the centre of Indian political power in the 18th century. Though a great fire in 1828 destroyed much of the wooden palace within, its massive fortification walls and grand gateways still stand as a proud symbol of Pune.</p>
<p>The imposing Delhi Gate, studded with anti-elephant spikes, and the palace's dramatic (and reputedly haunted) history make it an atmospheric window into the Maratha era. An evening sound-and-light show brings the story alive.</p>
<h2>Don't miss</h2>
<ul><li>The spiked Delhi Gate and the fortified ramparts.</li><li>The foundations and gardens within the walls.</li><li>The evening sound-and-light show on Maratha history.</li></ul>
<h2>Good to know</h2>
<p>Much of the interior palace is gone — it's the walls, gates and history you come for. It anchors Pune's old city, near lively markets and temples.</p>""")

P(slug="koregaon-park-pune", city="Pune", region="Maharashtra", cat="Nightlife",
  name="Koregaon Park", query="Koregaon Park Pune",
  excerpt="Pune's leafy, upscale nightlife district — tree-lined lanes packed with cafés, breweries, clubs and the famous Osho ashram.",
  tags=["Pune","nightlife","cafés","upscale"],
  info=dict(timings="Cafés from morning; bars & clubs till late", entry="Free to explore; venues priced individually",
            best="Evening into night", duration="An evening", reach="East-central Pune, off the river"),
  body="""<p>Koregaon Park — 'KP' to locals — is Pune's most cosmopolitan neighbourhood and the centre of its going-out scene. Its leafy, tree-lined lanes are dotted with stylish cafés, craft breweries, restaurants, lounges and clubs that draw the city's large student and young-professional crowd.</p>
<p>The area also holds the famous Osho International Meditation Resort, lending KP an unusual mix of spiritual seekers and party-goers. Whether you want a long café brunch, a craft beer or a late club night, this is Pune's address for it.</p>
<h2>Don't miss</h2>
<ul><li>The craft breweries and gastropubs.</li><li>The café and brunch scene along the numbered lanes.</li><li>The nearby Osho ashram and its serene gardens.</li></ul>
<h2>Good to know</h2>
<p>Weekend nights are busiest, especially in term time and around the VH1 Supersonic festival weekend. It's walkable — pick a lane and wander.</p>""")
