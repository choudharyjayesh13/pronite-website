# -*- coding: utf-8 -*-
"""Places batch E — NORTH INDIA: Delhi, Agra, Amritsar.
Must-visit landmarks + happening places (nightlife), happening food, happening streets.
Categories used here: Landmark, Temple, Palace & Fort, Nightlife, Food Street, Street & Bazaar."""
POSTS = []
def P(**k): POSTS.append(k)

# ======================= DELHI =======================

P(slug="red-fort-delhi", city="Delhi", region="Delhi", cat="Landmark",
  name="Red Fort (Lal Qila)", query="Red Fort Delhi",
  excerpt="The mighty Mughal fortress of red sandstone where India's Prime Minister raises the flag each Independence Day. A UNESCO site.",
  tags=["Delhi","Mughal","UNESCO","landmark"],
  info=dict(timings="9:30 AM – 4:30 PM (closed Mondays); evening light & sound show", entry="Approx ₹35 (Indian) / ₹500 (foreign)",
            best="October–March; mornings", duration="2 hours", reach="Old Delhi, near Chandni Chowk; nearest Metro Lal Qila / Chandni Chowk"),
  body="""<p>The Red Fort is the symbolic heart of India. Built by Shah Jahan in the 17th century as the palace-fort of his new capital Shahjahanabad, its massive red sandstone walls enclose a world of marble palaces, halls of audience and gardens. It's from its ramparts that the Prime Minister addresses the nation every Independence Day.</p>
<p>Inside, the Diwan-i-Aam (Hall of Public Audience) and the marble Diwan-i-Khas — once home to the fabled Peacock Throne — hint at the Mughal empire at its peak. The fort anchors Old Delhi and pairs perfectly with a wander through Chandni Chowk next door.</p>
<h2>Don't miss</h2>
<ul><li>The Lahori Gate and the grand Diwan-i-Aam.</li><li>The marble pavilions and the Nahr-i-Behisht (Stream of Paradise) channel.</li><li>The evening sound-and-light show on the fort's history.</li></ul>
<h2>Good to know</h2>
<p>Closed on Mondays. Security is tight — travel light. Combine with Chandni Chowk and Jama Masjid for a full Old Delhi day.</p>""")

P(slug="qutub-minar-delhi", city="Delhi", region="Delhi", cat="Landmark",
  name="Qutub Minar", query="Qutub Minar Delhi",
  excerpt="The world's tallest brick minaret — a 73-metre victory tower and UNESCO site rising over a complex of ancient ruins.",
  tags=["Delhi","UNESCO","landmark","history"],
  info=dict(timings="7 AM – 5 PM (daily)", entry="Approx ₹40 (Indian) / ₹600 (foreign)",
            best="Morning light; winter", duration="1.5 hours", reach="South Delhi, Mehrauli; nearest Metro Qutab Minar"),
  body="""<p>Soaring 73 metres over south Delhi, the Qutub Minar is the tallest brick minaret in the world and one of the capital's defining monuments. Begun in 1193 to mark the arrival of Muslim rule in India, its fluted red-sandstone shaft is carved with bands of intricate calligraphy and geometric detail.</p>
<p>The surrounding Qutub complex is a treasure trove: the ruins of India's first mosque, ornate gateways, and the famous Iron Pillar that has resisted rust for over 1,600 years — an enduring metallurgical mystery.</p>
<h2>Don't miss</h2>
<ul><li>The towering, carved minaret itself.</li><li>The rust-resistant Iron Pillar of Delhi.</li><li>The Alai Darwaza gateway and the Quwwat-ul-Islam mosque ruins.</li></ul>
<h2>Good to know</h2>
<p>Climbing the tower isn't permitted, but the complex rewards a slow wander. Beautifully lit and atmospheric in the low winter sun.</p>""")

P(slug="india-gate-delhi", city="Delhi", region="Delhi", cat="Landmark",
  name="India Gate", query="India Gate New Delhi",
  excerpt="Delhi's grand war memorial arch on the ceremonial Rajpath — floodlit at night and the city's favourite evening gathering spot.",
  tags=["Delhi","memorial","landmark","evening"],
  info=dict(timings="Open 24 hours; best in the evening", entry="Free",
            best="After dark, when it's floodlit", duration="45 minutes", reach="Central Delhi, Kartavya Path; nearest Metro Central Secretariat"),
  body="""<p>A 42-metre triumphal arch at the heart of Lutyens' Delhi, India Gate honours the tens of thousands of Indian soldiers who died in the First World War. Standing at the end of the ceremonial Kartavya Path (Rajpath), it's both a solemn memorial and the city's most beloved public space.</p>
<p>Come evening, the monument is floodlit and the surrounding lawns fill with families, ice-cream carts and street food — a quintessential Delhi scene. The eternal flame of the Amar Jawan and the nearby National War Memorial add to its significance.</p>
<h2>Don't miss</h2>
<ul><li>The illuminated arch after sunset.</li><li>The lawns and their lively evening street-food scene.</li><li>The adjacent National War Memorial.</li></ul>
<h2>Good to know</h2>
<p>It's free and open all hours — evenings are the magic time. A relaxed, only-in-Delhi people-watching spot.</p>""")

P(slug="humayuns-tomb-delhi", city="Delhi", region="Delhi", cat="Landmark",
  name="Humayun's Tomb", query="Humayun's Tomb Delhi",
  excerpt="The garden-tomb that inspired the Taj Mahal — a serene UNESCO masterpiece of Mughal architecture in the heart of Delhi.",
  tags=["Delhi","Mughal","UNESCO","garden tomb"],
  info=dict(timings="Sunrise – sunset (daily)", entry="Approx ₹40 (Indian) / ₹600 (foreign)",
            best="Golden hour; winter", duration="1.5 hours", reach="Nizamuddin, central Delhi; nearest Metro JLN Stadium"),
  body="""<p>Built in the 1560s for the Mughal emperor Humayun, this magnificent garden-tomb was the first of its kind in India and the direct architectural ancestor of the Taj Mahal. Set within formal charbagh gardens divided by water channels, its red sandstone and white marble dome is a study in perfect symmetry.</p>
<p>A UNESCO World Heritage Site beautifully restored in recent years, it's one of Delhi's most peaceful and photogenic monuments — far calmer than the city's busier landmarks.</p>
<h2>Don't miss</h2>
<ul><li>The grand central dome and the symmetrical charbagh gardens.</li><li>The intricate stone lattice screens (jaalis).</li><li>The surrounding tombs and the restored waterways.</li></ul>
<h2>Good to know</h2>
<p>Go early or late for the best light and fewer crowds. Pair it with the nearby Nizamuddin Dargah for its evening qawwali.</p>""")

P(slug="lotus-temple-delhi", city="Delhi", region="Delhi", cat="Temple",
  name="Lotus Temple", query="Lotus Temple Delhi",
  excerpt="A breathtaking Bahá'í house of worship shaped like a giant white lotus — open to all faiths, and one of the world's most-visited buildings.",
  tags=["Delhi","architecture","temple","modern"],
  info=dict(timings="Approx 9 AM – 5:30 PM (closed Mondays)", entry="Free",
            best="Morning; avoid weekends for smaller queues", duration="1 hour", reach="South Delhi, Kalkaji; nearest Metro Kalkaji Mandir"),
  body="""<p>One of the most striking modern buildings in India, the Lotus Temple unfurls like a vast white marble flower with 27 petals. Completed in 1986 as a Bahá'í house of worship, it welcomes people of every religion to sit in silence in its serene central hall — there are no idols, sermons or rituals, just peace.</p>
<p>Set amid landscaped gardens and pools, it has become one of the most-visited buildings on earth, and a symbol of Delhi as memorable as any Mughal monument.</p>
<h2>Don't miss</h2>
<ul><li>The lotus-shaped exterior against the sky.</li><li>The tranquil, silent prayer hall inside.</li><li>The reflecting pools and gardens.</li></ul>
<h2>Good to know</h2>
<p>Silence is observed inside — phones off. Queues can be long on weekends; go on a weekday morning. Closed Mondays.</p>""")

P(slug="chandni-chowk-delhi", city="Delhi", region="Delhi", cat="Street & Bazaar",
  name="Chandni Chowk", query="Chandni Chowk Delhi",
  excerpt="One of India's oldest and most chaotic bazaars — a sensory overload of spice, silver, sarees and street life in the heart of Old Delhi.",
  tags=["Delhi","bazaar","shopping","Old Delhi"],
  info=dict(timings="Most shops ~11 AM – 8 PM (many closed Sundays)", entry="Free",
            best="Late morning to evening; go hungry", duration="Half day", reach="Old Delhi; nearest Metro Chandni Chowk"),
  body="""<p>There is nowhere quite like Chandni Chowk. Laid out in the 17th century by Shah Jahan's daughter, this is one of the oldest and busiest markets in India — a labyrinth of lanes crammed with wedding finery, silver, spices, books, electronics and every kind of street food, all in a glorious tangle of rickshaws, wires and noise.</p>
<p>Each lane has a specialty: Kinari Bazaar for wedding trims, Dariba Kalan for silver, Khari Baoli for spices (Asia's largest spice market). It's overwhelming, exhausting and utterly unforgettable — the beating heart of Old Delhi.</p>
<h2>Don't miss</h2>
<ul><li>Khari Baoli, Asia's largest wholesale spice market.</li><li>Dariba Kalan (silver) and Kinari Bazaar (wedding finery).</li><li>The street food — this is one of India's great eating streets.</li></ul>
<h2>Good to know</h2>
<p>Go on foot or by cycle-rickshaw; cars are hopeless here. Many shops shut on Sundays. Keep valuables secure in the crush, and come hungry.</p>""")

P(slug="paranthe-wali-gali-delhi", city="Delhi", region="Delhi", cat="Food Street",
  name="Paranthe Wali Gali & Old Delhi eats", query="Paranthe Wali Gali Delhi",
  excerpt="The legendary fried-paratha lane of Old Delhi — the tip of a street-food iceberg that includes some of India's most famous eats.",
  tags=["Delhi","street food","Old Delhi","food"],
  info=dict(timings="Roughly midday – late evening", entry="Free (pay as you eat)",
            best="Lunch or evening; come with an appetite", duration="2–3 hours (a food crawl)", reach="Off Chandni Chowk, Old Delhi; Metro Chandni Chowk"),
  body="""<p>Old Delhi is arguably the greatest street-food destination in India, and Paranthe Wali Gali is its most storied lane — a narrow alley where families have been frying stuffed parathas in ghee for over a century. But the paratha lane is just the beginning of a legendary food crawl.</p>
<p>Within a few minutes' walk you'll find century-old shops serving butter chicken and korma, syrup-soaked jalebis fried in giant woks, spicy chaat, kebabs near Jama Masjid, and creamy kulfi. Eating your way through Old Delhi is a rite of passage for any food lover.</p>
<h2>Don't miss</h2>
<ul><li>Stuffed parathas at the historic Paranthe Wali Gali shops.</li><li>Jalebis and daulat ki chaat (a winter-only milk-froth dessert).</li><li>The kebabs and korma around Jama Masjid.</li></ul>
<h2>Good to know</h2>
<p>Eat where the crowds are — turnover means freshness. Pace yourself across many small plates. Best explored on a guided food walk if it's your first time.</p>""")

P(slug="hauz-khas-village-delhi", city="Delhi", region="Delhi", cat="Nightlife",
  name="Hauz Khas Village", query="Hauz Khas Delhi",
  excerpt="Delhi's coolest hangout — medieval ruins and a lake wrapped in a warren of rooftop bars, cafés, boutiques and late-night energy.",
  tags=["Delhi","nightlife","bars","hangout"],
  info=dict(timings="Cafés from noon; bars till late (peak Thu–Sat)", entry="Free to wander; venues priced individually",
            best="Evening into night", duration="An evening", reach="South Delhi; nearest Metro Hauz Khas / Green Park"),
  body="""<p>Hauz Khas Village is where Delhi's history and its nightlife collide. Set around a 13th-century reservoir, madrasa ruins and a deer park, this maze of narrow lanes has become the city's most characterful going-out district — packed with rooftop bars, live-music venues, art galleries, boutiques and cafés.</p>
<p>By day you can wander the atmospheric medieval monuments and the lake; by night the same lanes buzz with a young, creative crowd bar-hopping between rooftops with views over the ruins. It's Delhi at its most eclectic.</p>
<h2>Don't miss</h2>
<ul><li>The rooftop bars overlooking the historic lake and ruins.</li><li>The Hauz Khas medieval monuments and deer park by day.</li><li>The indie boutiques, galleries and cafés.</li></ul>
<h2>Good to know</h2>
<p>Thursday to Saturday nights are busiest. The lanes are narrow and can get packed — go with the flow. Nearby Hauz Khas Social is a perennial favourite.</p>""")

# ======================= AGRA =======================

P(slug="taj-mahal-agra", city="Agra", region="Uttar Pradesh", cat="Landmark",
  name="Taj Mahal", query="Taj Mahal Agra",
  excerpt="The greatest monument to love ever built — a flawless white-marble mausoleum, one of the New Seven Wonders of the World.",
  tags=["Agra","UNESCO","Mughal","wonder"],
  info=dict(timings="Sunrise – sunset (closed Fridays); night viewing on select dates", entry="Approx ₹50 (Indian) / ₹1100 (foreign) + ₹200 for the main mausoleum",
            best="Sunrise, for soft light and fewer crowds", duration="2–3 hours", reach="Agra, Uttar Pradesh; ~3–4 hrs from Delhi by expressway/train"),
  body="""<p>No photograph prepares you for it. The Taj Mahal, built by Shah Jahan in the 17th century as a tomb for his beloved wife Mumtaz Mahal, is widely considered the most beautiful building in the world — a perfectly symmetrical vision of white marble that seems to change colour with the light, from soft pink at dawn to dazzling white at noon.</p>
<p>Up close, the marble is inlaid with semi-precious stones in delicate floral patterns, and the calligraphy and gardens are as exquisite as the famous dome. A UNESCO World Heritage Site and one of the New Seven Wonders of the World, it's the single most iconic sight in India.</p>
<h2>Don't miss</h2>
<ul><li>The Taj at sunrise, when the marble glows and crowds are thinnest.</li><li>The intricate pietra dura (inlaid stone) work up close.</li><li>The view from across the river at Mehtab Bagh at sunset.</li></ul>
<h2>Good to know</h2>
<p>Closed on Fridays. Go at sunrise. Large bags and many items are banned — travel light. Book tickets online to skip queues.</p>""")

P(slug="agra-fort", city="Agra", region="Uttar Pradesh", cat="Palace & Fort",
  name="Agra Fort", query="Agra Fort",
  excerpt="A vast red-sandstone Mughal fortress and palace — a UNESCO site with a poignant view across the river to the Taj Mahal.",
  tags=["Agra","Mughal","UNESCO","fort"],
  info=dict(timings="Sunrise – sunset (daily)", entry="Approx ₹50 (Indian) / ₹650 (foreign)",
            best="Morning; combine with the Taj", duration="1.5–2 hours", reach="Agra, ~2.5 km from the Taj Mahal"),
  body="""<p>Before the Taj, there was Agra Fort — the great red-sandstone stronghold that served as the main residence of the Mughal emperors for generations. Behind its massive double walls lies a city of palaces, mosques, audience halls and gardens blending red sandstone with delicate white marble.</p>
<p>It's also a place of poignant history: it was here that Shah Jahan, who built the Taj, spent his final years imprisoned by his own son, gazing out at his wife's tomb across the river. A UNESCO World Heritage Site, it's the perfect companion to a Taj visit.</p>
<h2>Don't miss</h2>
<ul><li>The view of the Taj Mahal from the marble Musamman Burj.</li><li>The Diwan-i-Khas and the mirror-work Sheesh Mahal.</li><li>The grand Amar Singh and Delhi gates.</li></ul>
<h2>Good to know</h2>
<p>Only part of the fort is open (the rest is a military area). Visit alongside the Taj for the full Mughal Agra story.</p>""")

P(slug="fatehpur-sikri", city="Fatehpur Sikri", region="Uttar Pradesh", cat="Landmark",
  name="Fatehpur Sikri", query="Fatehpur Sikri",
  excerpt="The perfectly preserved ghost capital of the Mughals — a UNESCO red-sandstone city abandoned almost as soon as it was built.",
  tags=["Mughal","UNESCO","history","day trip"],
  info=dict(timings="Sunrise – sunset; Jama Masjid open separately", entry="Approx ₹50 (Indian) / ₹610 (foreign)",
            best="Morning; October–March", duration="2 hours", reach="~40 km west of Agra — a common half-day trip"),
  body="""<p>For a brief, glorious period in the 16th century, Fatehpur Sikri was the capital of the mighty Mughal Empire — a magnificent planned city built by Emperor Akbar in red sandstone. Then, almost as soon as it was finished, it was abandoned, likely due to water shortages, leaving one of the best-preserved 'ghost cities' in the world.</p>
<p>Today its palaces, courtyards, the vast Jama Masjid and the stunning Buland Darwaza (Gate of Victory) stand almost exactly as they were left, offering an extraordinarily intact window into Mughal life at its height.</p>
<h2>Don't miss</h2>
<ul><li>The towering Buland Darwaza, one of the highest gateways in the world.</li><li>The delicate marble Tomb of Salim Chishti.</li><li>The Panch Mahal and Diwan-i-Khas palace buildings.</li></ul>
<h2>Good to know</h2>
<p>Usually visited as a half-day trip from Agra, often en route to Jaipur. Beware persistent 'guides' at the entrance — agree terms first.</p>""")

# ======================= AMRITSAR =======================

P(slug="golden-temple-amritsar", city="Amritsar", region="Punjab", cat="Temple",
  name="Golden Temple (Harmandir Sahib)", query="Golden Temple Amritsar",
  excerpt="The holiest shrine of Sikhism — a golden sanctuary shimmering on a sacred pool, radiating peace and welcoming all.",
  tags=["Amritsar","Sikh","pilgrimage","landmark"],
  info=dict(timings="Open 24 hours (darshan from very early morning)", entry="Free (heads covered; shoes removed)",
            best="Dawn or after dark, when it glows on the water", duration="1.5–2 hours", reach="Old city of Amritsar, Punjab"),
  body="""<p>Few places in the world move visitors like the Golden Temple. The holiest gurdwara of the Sikh faith, its gilded sanctuary appears to float at the centre of the Amrit Sarovar (Pool of Nectar), reflected in the still water and reached by a marble causeway. Around it flows a constant, serene tide of pilgrims.</p>
<p>The atmosphere is one of profound peace and radical equality — everyone, of every background, is welcome. The temple's langar (community kitchen) serves free meals to up to 100,000 people a day, one of the great humanitarian sights on earth.</p>
<h2>Don't miss</h2>
<ul><li>The temple glowing gold at dawn and after dark.</li><li>The langar — the world's largest free community kitchen.</li><li>The continuous devotional singing (kirtan) from the sanctum.</li></ul>
<h2>Good to know</h2>
<p>Cover your head, remove shoes and wash your feet before entering (facilities provided). Dress modestly. It's open around the clock — the pre-dawn and late-night hours are especially magical.</p>""")

P(slug="wagah-border-amritsar", city="Amritsar", region="Punjab", cat="Landmark",
  name="Wagah Border Ceremony", query="Wagah border ceremony",
  excerpt="The theatrical daily flag-lowering ceremony at the India–Pakistan border — high-kicking soldiers, roaring crowds and patriotic spectacle.",
  tags=["Amritsar","border","ceremony","spectacle"],
  info=dict(timings="Daily, late afternoon before sunset (arrive ~1.5 hrs early)", entry="Free",
            best="Any evening; arrive early for seating", duration="1.5–2 hours (plus travel)", reach="~30 km from Amritsar toward the Pakistan border (Attari)"),
  body="""<p>Every evening, at the only road crossing between India and Pakistan, the two nations stage one of the most extraordinary daily rituals in the world: the Beating Retreat ceremony. Border Security Force soldiers in fan-plumed turbans face off against their Pakistani counterparts in a gloriously theatrical routine of high kicks, stamping and flag-lowering.</p>
<p>The real spectacle is the crowd — thousands of spectators on each side, waving flags, chanting and dancing to patriotic songs in a stadium-like atmosphere. It's part military drill, part sporting event, part national celebration.</p>
<h2>Don't miss</h2>
<ul><li>The synchronised high-kicking drill by both nations' guards.</li><li>The roaring, flag-waving crowd energy.</li><li>The simultaneous lowering of both flags at sunset.</li></ul>
<h2>Good to know</h2>
<p>Arrive well ahead for a seat; it gets packed. Carry minimal belongings (bag restrictions apply). Combine with the Golden Temple and Jallianwala Bagh for a full Amritsar day.</p>""")

P(slug="amritsari-food-street", city="Amritsar", region="Punjab", cat="Food Street",
  name="Amritsar food trail", query="Amritsari kulcha food",
  excerpt="Punjab on a plate — buttery kulchas, rich chole, tandoori everything and thick lassi in the birthplace of North Indian comfort food.",
  tags=["Amritsar","street food","Punjabi","food"],
  info=dict(timings="Breakfast through late night (varies by eatery)", entry="Free (pay as you eat)",
            best="Any meal; breakfast for kulcha", duration="A day of grazing", reach="Old city lanes around the Golden Temple, Amritsar"),
  body="""<p>Amritsar is a pilgrimage for food lovers as much as for the faithful. This is the home of some of North India's most beloved dishes, served in legendary shops that have perfected a single thing over generations. Eating here is rich, unapologetic and deeply satisfying.</p>
<p>The signature is the Amritsari kulcha — a crisp, stuffed, ghee-laden bread served with spicy chole and butter. Add tandoori fish, creamy dal, thick sweet lassi served in giant glasses, and freshly fried jalebis, and you have one of India's great regional food scenes, best explored in the lanes around the Golden Temple.</p>
<h2>Don't miss</h2>
<ul><li>Amritsari kulcha with chole and a dollop of butter.</li><li>Amritsari fish (tandoori/fried) and rich dal.</li><li>Thick, sweet lassi in a giant glass, and hot jalebis.</li></ul>
<h2>Good to know</h2>
<p>Come hungry and eat where the locals queue. Many iconic shops are near the Golden Temple. And don't skip the langar meal at the temple itself — humbling and delicious.</p>""")
